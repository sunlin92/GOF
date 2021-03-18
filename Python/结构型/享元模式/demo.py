#!/usr/bin/env python3

import atexit
import os
import shelve
import sys


class Point:

    __slots__ = ()
    __dbm = shelve.open(os.path.join("point.db"))

    def __init__(self, x=0, y=0, z=0, color=None):
        self.x = x
        self.y = y
        self.z = z
        self.color = color

    def __key(self, name):
        return "{:X}:{}".format(id(self), name)

    def __getattr__(self, name):
        return Point.__dbm[self.__key(name)]

    def __setattr__(self, name, value):
        Point.__dbm[self.__key(name)] = value

    def __repr__(self):
        return "Point({0.x!r}, {0.y!r}, {0.z!r}, {0.color!r})".format(self)

    atexit.register(__dbm.close)


def main():
    regression = False
    size = 100
    if len(sys.argv) > 2 and sys.argv[1] == "-P":
        regression = True
        size = int(sys.argv[2])
    if len(sys.argv) > 1 and sys.argv[1] != "-P":
        size = int(sys.argv[1])
    points = []
    for i in range(size):
        points.append(Point(i, i ** 2, i // 2))
    assert points[size - 1].x == size - 1
    if not regression:
        print("create {:,} points".format(size))
        input("wait until we can see how much memory is used")
    else:
        print(points)
        input("wait until we can see how much memory is used")


if __name__ == "__main__":
    main()
