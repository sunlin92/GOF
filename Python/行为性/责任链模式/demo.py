#!/usr/bin/env python3

import sys
import event
import functools


def coroutine(function):
    @functools.wraps(function)
    def wrapper(*args, **kw):
        generator = function(*args, **kw)
        next(generator)
        return generator

    return wrapper


# 利用coroutine将无限循环的生成器变成协程
@coroutine
def debug_handler(successor, file=sys.stdout):
    while True:
        e = yield
        file.write("*DEBUG*: {}\n".format(e))
        successor.send(e)


@coroutine
def mouse_handler(successor=None):
    while True:
        e = yield
        if e.kind == event.MOUSE:
            print("Click:   {}".format(e))
        elif successor is not None:
            successor.send(e)


@coroutine
def key_handler(successor=None):
    while True:
        e = yield
        if e.kind == event.KEYPRESS:
            print("Press:   {}".format(e))
        elif successor is not None:
            successor.send(e)


@coroutine
def timer_handler(successor=None):
    while True:
        e = yield
        if e.kind == event.TIMER:
            print("Timeout: {}".format(e))
        elif successor is not None:
            successor.send(e)


def main():
    print("Handler Chain #1")
    pipeline = key_handler(mouse_handler(timer_handler()))
    while True:
        e = event.next()
        if e.kind == event.TERMINATE:
            break
        pipeline.send(e)

    print("\n")

    print("Handler Chain #2 (debugging)")
    pipeline = debug_handler(pipeline)
    while True:
        e = event.next()
        if e.kind == event.TERMINATE:
            break
        pipeline.send(e)


if __name__ == "__main__":
    main()
