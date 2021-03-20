#!/usr/bin/env python3

import collections
import random
import functools

CARS, VANS, TRUCKS = ("cars", "vans", "trucks")


def coroutine(function):
    """
    根据参数创建对应的生成器对象
    进行next调用,并返回生成器对象
    """

    @functools.wraps(function)
    def wrapper(*args, **kw):
        generator = function(*args, **kw)
        next(generator)
        return generator

    return wrapper


def generate_random_events(count):
    """
    随机事件生成器
    """
    vehicles = ((CARS,) * 11) + ((VANS,) * 3) + (TRUCKS,)
    for _ in range(count):
        yield Event(random.choice(vehicles), random.randint(1, 3))


class Counter:
    """
    计数器
    """

    def __init__(self, *names):
        self.anonymous = not bool(names)
        if self.anonymous:
            self.count = 0
        else:
            for name in names:
                if not name.isidentifier():
                    raise ValueError("names must be valid identifiers")
                setattr(self, name, 0)

    def __call__(self, e):
        """
        调用计数器对象时累加调用次数
        """
        if self.anonymous:
            self.count += e.count
        else:
            count = getattr(self, e.name)
            setattr(self, e.name, count + e.count)


class Event:
    """
    事件对象
    """

    def __init__(self, name, count=1):
        if not name.isidentifier():
            raise ValueError("names must be valid identifiers")
        self.name = name
        self.count = count


class Multiplexer:
    """
    状态-多路复用器
    """

    # 享元模式，变量引用字符串压缩内存
    ACTIVE, DORMANT = ("ACTIVE", "DORMANT")

    def __init__(self):
        self.callbacksFore = collections.defaultdict(list)
        # 默认设定复用器的状态为ACTIVE
        self.state = Multiplexer.ACTIVE

    # 被coroutine修饰成为协程管道，保持循环
    @coroutine
    def pipeline(self):
        """
        复用器协程管道
        根据复用器的状态， 对传入的事件进行相响应
        响应的内容是，复用器callbacksFore字典记录的一对多映射关系
        """
        while True:
            e = yield
            if self.state == Multiplexer.ACTIVE:
                for callback in self.callbacksFore.get(e.name, ()):
                    callback(e)

    def connect(self, eName, callback):
        if self.state == Multiplexer.ACTIVE:
            self.callbacksFore[eName].append(callback)

    def disconnect(self, eName, callback=None):
        if self.state == Multiplexer.ACTIVE:
            if callback is None:
                del self.callbacksFore[eName]
            else:
                self.callbacksFore[eName].remove(callback)


def main():
    def show(discription, car_counter, commercial_counter, total_counter):
        print(
            "After 100 {} events: cars={} vans={} trucks={} total={}".format(
                discription,
                car_counter.cars,
                commercial_counter.vans,
                commercial_counter.trucks,
                total_counter.count,
            )
        )

    # 生成计数器对象, 其被调用时记录调用次数
    total_counter = Counter()
    car_counter = Counter(CARS)
    commercial_counter = Counter(TRUCKS, VANS)

    multiplexer = Multiplexer()
    # 为事件绑定对应的计数器
    for eName, callback in (
        (CARS, car_counter),
        (VANS, commercial_counter),
        (TRUCKS, commercial_counter),
    ):
        multiplexer.connect(eName, callback)
        multiplexer.connect(eName, total_counter)

    # 解绑事件计数器
    # multiplexer.disconnect(TRUCKS, commercial_counter)

    pipeline = multiplexer.pipeline()

    multiplexer.state = Multiplexer.DORMANT
    for e in generate_random_events(100):
        pipeline.send(e)
    show("dormant", car_counter, commercial_counter, total_counter)

    multiplexer.state = Multiplexer.ACTIVE
    for e in generate_random_events(100):
        pipeline.send(e)
    show("active", car_counter, commercial_counter, total_counter)

    multiplexer.state = Multiplexer.DORMANT
    for e in generate_random_events(100):
        pipeline.send(e)
    show("dormant", car_counter, commercial_counter, total_counter)


if __name__ == "__main__":
    main()
