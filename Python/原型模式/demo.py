#!/bin/bash/env python3
import sys
import copy


def make_object(cls, *args, **kwargs):
    return cls(*args, **kwargs)


class Point(object):
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point({},{})".format(self.x, self.y)


def main():
    # 创建Point对象的7个方式

    p1 = Point(1, 2)
    p2 = eval("{}({}, {})".format("Point", 2, 4))
    p3 = getattr(sys.modules[__name__], "Point")(3, 6)
    p4 = globals()["Point"](4, 8)
    p5 = make_object(Point, 5, 10)
    p6 = copy.deepcopy(p5)
    p6.x, p6.y = (6, 12)
    # python 原型模式
    p7 = p1.__class__(7, 14)
    print(p1, p2, p3, p4, p5, p6, p7)


if __name__ == "__main__":
    main()
