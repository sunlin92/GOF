#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import collections
import abc


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


# 抽象软件类
@has_methods("run")
class App(metaclass=abc.ABCMeta):
    pass


# 手游
class Game(App):
    def run(self):
        print("运行手机游戏")


# 通讯录
class AddressList(App):
    def run(self):
        print("运行通信录")


# 抽象手机品牌类
@has_methods("runapp")
class Phone(metaclass=abc.ABCMeta):
    def set_handle_app(self, app):
        if not isinstance(app, App):
            raise TypeError(
                "Expected object of type App, got {}".format(type(app).__name__)
            )
        self.app = app

    pass


class GooglePixel(Phone):
    def do_something_for_android(self):
        print("google pixel is doing something")

    def runapp(self):
        self.do_something_for_android()
        self.app.run()


class AppleIphone(Phone):
    def do_something_for_ios(self):
        print("apple iphone is doing something")

    def runapp(self):
        self.do_something_for_ios()
        self.app.run()


def main():
    pixel5 = GooglePixel()
    pixel5.set_handle_app(Game())
    pixel5.runapp()
    pixel5.set_handle_app(AddressList())
    pixel5.runapp()

    iphone12 = AppleIphone()
    iphone12.set_handle_app(Game())
    iphone12.runapp()
    iphone12.set_handle_app(AddressList())
    iphone12.runapp()


if __name__ == "__main__":
    main()
