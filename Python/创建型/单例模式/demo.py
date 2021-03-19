#!/usr/bin/env python3

import time
import random


def do_something():
    """
    我是一个非常消耗资源的函数
    """
    s = random.randint(1, 5)
    time.sleep(s)
    return s


def get(refresh=False):

    if refresh:
        get.resource = ""

    if get.resource:
        return get.resource

    get.resource = do_something()

    return get.resource


# 把全局状态放到私有变量中
get.resource = {}


def main():
    print(get())


if __name__ == "__main__":
    main()
