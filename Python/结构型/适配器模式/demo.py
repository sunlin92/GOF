#!/usr/bin/env python3

import abc
import sys
import textwrap
from html import escape
import collections


def has_methods(*methods):
    def decorator(Base):
        def __subclasshook__(cls, Subclass):
            if cls is Base:
                attributes = collections.ChainMap(
                    *(Superclass.__dict__ for Superclass in Subclass.__mro__)
                )
                if all(method in attributes for method in methods):
                    return True
            return NotImplemented

        Base.__subclasshook__ = classmethod(__subclasshook__)
        return Base

    return decorator


@has_methods("header", "paragraph", "footer")
class Renderer(metaclass=abc.ABCMeta):
    pass


class Page:
    def __init__(self, title, renderer):
        if not isinstance(renderer, Renderer):
            raise TypeError(
                "Expected object of type Renderer, got {}".format(
                    type(renderer).__name__
                )
            )
        self.title = title
        self.renderer = renderer
        self.paragraphs = []

    def add_paragraph(self, paragraph):
        self.paragraphs.append(paragraph)

    def render(self):
        self.renderer.header(self.title)
        [self.renderer.paragraph(paragraph) for paragraph in self.paragraphs]
        self.renderer.footer()


class TextRenderer:
    def __init__(self, width=80, file=sys.stdout):
        self.width = width
        self.file = file
        self.previous = False

    def header(self, title):
        self.file.write(
            "{0:^{2}}\n{1:^{2}}\n".format(title, "=" * len(title), self.width)
        )

    def paragraph(self, text):
        if self.previous:
            self.file.write("\n")
        self.file.write(textwrap.fill(text, self.width))
        self.file.write("\n")
        self.previous = True

    def footer(self):
        pass


class HtmlWriter:
    """
    被适配的类
    """

    def __init__(self, file=sys.stdout):
        self.file = file

    def header(self):
        self.file.write("<!doctype html>\n<html>\n")

    def title(self, title):
        self.file.write(
            "<head><title>{}</title></head>\n".format(escape(title))
        )

    def start_body(self):
        self.file.write("<body>\n")

    def body(self, text):
        self.file.write("<p>{}</p>\n".format(escape(text)))

    def end_body(self):
        self.file.write("</body>\n")

    def footer(self):
        self.file.write("</html>\n")


class HtmlRenderer:
    def __init__(self, htmlWriter):
        self.htmlWriter = htmlWriter

    def header(self, title):
        self.htmlWriter.header()
        self.htmlWriter.title(title)
        self.htmlWriter.start_body()

    def paragraph(self, text):
        self.htmlWriter.body(text)

    def footer(self):
        self.htmlWriter.end_body()
        self.htmlWriter.footer()


def main():
    MESSAGE = """
    This is a very short {} paragraph that demonstrates the simple {} cls.
    """
    paragraph1 = MESSAGE.format("plain-text", "TextRenderer")
    paragraph2 = "This is another short paragraph."
    title = "Plain Text"
    textPage = Page(title, TextRenderer(22))
    textPage.add_paragraph(paragraph1)
    textPage.add_paragraph(paragraph2)
    textPage.render()

    print()

    paragraph1 = MESSAGE.format("HTML", "HtmlRenderer")
    title = "HTML"
    file = sys.stdout
    htmlPage = Page(title, HtmlRenderer(HtmlWriter(file)))
    htmlPage.add_paragraph(paragraph1)
    htmlPage.add_paragraph(paragraph2)
    htmlPage.render()

    try:
        page = Page(title, HtmlWriter())
        page.render()
        print("ERROR! rendering with an invalid renderer")
    except TypeError as err:
        print(err)


if __name__ == "__main__":
    main()
