#!/usr/bin/env python
# -*- coding:utf-8 -*-


def has_methods(*methods):
    def decorator(Base):
        def __subclasshook__(cls, Subclass):
            if cls is Base:
                import collections

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
class HandsetSoft(object):
    pass


# 手游
class HandsetGame(HandsetSoft):
    def run(self):
        print("运行手机游戏")


# 通讯录
class HandsetAddressList(HandsetSoft):
    def run(self):
        print("运行通信录")


# 抽象手机品牌类
@has_methods("runapp")
class Phone(object):
    pass


class GooglePixel(Phone):
    def do_something_for_android(self):
        print("google pixel is doing something")

    def runapp(self, app):
        self.do_something_for_android()
        app.run()


class AppleIphone(Phone):
    def do_something_for_ios(self):
        print("apple iphone is doing something")

    def runapp(self, app):
        self.do_something_for_ios()
        app.run()


def main():
    pixel5 = GooglePixel()
    pixel5.runapp(HandsetGame())
    pixel5.runapp(HandsetAddressList())

    iphone12 = AppleIphone()
    iphone12.runapp(HandsetGame())
    iphone12.runapp(HandsetAddressList())


if __name__ == "__main__":
    main()
