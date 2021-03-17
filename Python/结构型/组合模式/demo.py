#!/usr/bin/env python3

import itertools
import sys


class Item:
    def __init__(self, name, *items, price=0.00):
        self.name = name
        self.price = price
        self.children = []
        if items:
            self.add(*items)

    def add(self, first, *items):
        self.children.extend(itertools.chain((first,), items))

    def remove(self, item):
        self.children.remove(item)

    def __iter__(self):
        return iter(self.children)

    @property
    def price(self):
        return sum(item.price for item in self) if self.children else self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    def print(self, indent="", file=sys.stdout):
        print("{}${:.2f} {}".format(indent, self.price, self.name), file=file)
        for child in self:
            child.print(indent + "      ")


def main():
    pencil = Item("Pencil", price=0.40)
    ruler = Item("Ruler", price=1.60)
    eraser = Item("Eraser", price=0.20)
    box = Item("Box", price=1.00)

    pencilSet = Item("Pencil Set", pencil, ruler, eraser)
    boxedPencilSet = Item("Boxed Pencil Set", box, pencilSet)

    boxedPencilSet.add(pencilSet)

    for item in (pencil, ruler, eraser, pencilSet, boxedPencilSet):
        item.print()


if __name__ == "__main__":
    main()
