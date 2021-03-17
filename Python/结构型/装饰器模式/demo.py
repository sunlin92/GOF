#!/usr/bin/env python3

import numbers
import re


def is_non_empty_str(name, value):
    if not isinstance(value, str):
        raise ValueError("{} must be of type str".format(name))
    if not bool(value):
        raise ValueError("{} may not be empty".format(name))


def is_in_range(minimum=None, maximum=None):
    assert minimum is not None or maximum is not None

    def is_in_range(name, value):
        if not isinstance(value, numbers.Number):
            raise ValueError("{} must be a number".format(name))
        if minimum is not None and value < minimum:
            raise ValueError("{} {} is too small".format(name, value))
        if maximum is not None and value > maximum:
            raise ValueError("{} {} is too big".format(name, value))

    return is_in_range


def is_valid_isbn(name, isbn):
    regex = re.compile(
        r"^(?:ISBN(?:-1[03])?:? )?(?=[-0-9 ]{17}$|"
        r"[-0-9X ]{13}$|[0-9X]{10}$)(?:97[89][- ]?)?[0-9]{1,5}[- ]?"
        r"(?:[0-9]+[- ]?){2}[0-9X]$"
    )
    if regex.match(isbn):
        digits = list(re.sub("[^0-9X]", "", isbn))
        checkSumDigit = digits.pop()
        if len(digits) == 9:  # ISBN-10
            value = sum((x + 2) * int(y) for x, y in enumerate(reversed(digits)))
            check = 11 - (value % 11)
            if check == 10:
                check = "X"
            elif check == 11:
                check = "0"
        else:  # ISBN-13
            value = sum((x % 2 * 2 + 1) * int(y) for x, y in enumerate(digits))
            check = 10 - (value % 10)
            if check == 10:
                check = "0"
        if str(check) != checkSumDigit:
            raise ValueError("{} is not a valid ISBN".format(isbn))
        return
    raise ValueError("{} is not a valid ISBN".format(isbn))


def ensure(name, validate, doc=None):
    def decorator(cls):
        private_name = "__" + name

        def getter(self):
            return getattr(self, private_name)

        def setter(self, value):
            validate(name, value)
            setattr(self, private_name, value)

        setattr(cls, name, property(getter, setter, doc=doc))
        return cls

    return decorator


class Ensure:
    def __init__(self, validate, doc=None):
        self.validate = validate
        self.doc = doc


def do_ensure(cls):
    def make_property(name, attribute):
        private_name = "__" + name

        def getter(self):
            return getattr(self, private_name)

        def setter(self, value):
            attribute.validate(name, value)
            setattr(self, private_name, value)

        return property(getter, setter, doc=attribute.doc)

    for name, attribute in cls.__dict__.items():
        if isinstance(attribute, Ensure):
            setattr(cls, name, make_property(name, attribute))
    return cls


@ensure("title", is_non_empty_str)
@ensure("isbn", is_valid_isbn)
@ensure("price", is_in_range(1, 10000))
@ensure("quantity", is_in_range(0, 1000000))
class BookA:
    def __init__(self, title, isbn, price, quantity):
        self.title = title
        self.isbn = isbn
        self.price = price
        self.quantity = quantity

    @property
    def value(self):
        return self.price * self.quantity

    def __repr__(self):
        return "Book({0.title!r}, {0.isbn!r}, {0.price!r}, " "{0.quantity!r})".format(
            self
        )


@do_ensure
class BookB:

    title = Ensure(is_non_empty_str)
    isbn = Ensure(is_valid_isbn)
    price = Ensure(is_in_range(1, 10000))
    quantity = Ensure(is_in_range(0, 1000000))

    def __init__(self, title, isbn, price, quantity):
        self.title = title
        self.isbn = isbn
        self.price = price
        self.quantity = quantity

    @property
    def value(self):
        return self.price * self.quantity

    def __repr__(self):
        return "Book({0.title!r}, {0.isbn!r}, {0.price!r}, " "{0.quantity!r})".format(
            self
        )


def main():

    books = []
    for title, isbn, price, quantity in (
        ("Advanced Qt Programming", "ISBN 0321635906", 54.99, 7830),
        ("Programming in Go", "ISBN 0321774639", 44.99, 5220),
        ("Programming in Python 3", "ISBN-13: 9780321680563", 49.99, 10960),
        ("Rapid GUI Programming with Python and Qt", "ISBN 0132354187", 54.99, 11735),
        ("C++ GUI Programming with Qt 4", "0132354160", 69.99, 15872),
    ):
        books.append(BookA(title, isbn, price, quantity))
        books.append(BookB(title, isbn, price, quantity))
    for book in books:
        print(book)


if __name__ == "__main__":
    main()
