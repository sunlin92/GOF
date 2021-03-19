#!/usr/bin/env python3
import functools


def coroutine(function):
    @functools.wraps(function)
    def wrapper(*args, **kw):
        generator = function(*args, **kw)
        next(generator)
        return generator

    return wrapper


class Form:
    def __init__(self):
        self.create_widgets()
        self.create_mediator()

    def create_widgets(self):
        self.nameText = Text()
        self.emailText = Text()
        self.okButton = Button("OK")
        self.cancelButton = Button("Cancel")

    def create_mediator(self):
        self.mediator = self._update_ui_mediator(self._clicked_mediator())
        for widget in (self.nameText, self.emailText, self.okButton, self.cancelButton):
            widget.mediator = self.mediator
        self.mediator.send(None)

    @coroutine
    def _update_ui_mediator(self, successor=None):
        while True:
            widget = yield
            self.okButton.enabled = bool(self.nameText.text) and bool(
                self.emailText.text
            )
            if successor is not None:
                successor.send(widget)

    @coroutine
    def _clicked_mediator(self, successor=None):
        while True:
            widget = yield
            if widget == self.okButton:
                print("OK")
            elif widget == self.cancelButton:
                print("Cancel")
            elif successor is not None:
                successor.send(widget)


def mediated(cls):
    setattr(cls, "mediator", None)

    def on_change(self):
        if self.mediator is not None:
            self.mediator.send(self)

    setattr(cls, "on_change", on_change)
    return cls


@mediated
class Button:
    def __init__(self, text=""):
        self.enabled = True
        self.text = text

    def click(self):
        if self.enabled:
            self.on_change()

    def __str__(self):
        return "Button({!r}) {}".format(
            self.text, "enabled" if self.enabled else "disabled"
        )


@mediated
class Text:
    def __init__(self, text=""):
        self.__text = text

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text):
        if self.text != text:
            self.__text = text
            self.on_change()

    def __str__(self):
        return "Text({!r})".format(self.text)


def main():
    form = Form()
    form.okButton.click()  # Ignored because it is disabled
    print(form.okButton.enabled)  # False
    form.nameText.text = "Fred"
    print(form.okButton.enabled)  # False
    form.emailText.text = "fred@bloggers.com"
    print(form.okButton.enabled)  # True
    form.okButton.click()  # OK
    form.emailText.text = ""
    print(form.okButton.enabled)  # False
    form.cancelButton.click()  # Cancel


if __name__ == "__main__":
    main()
