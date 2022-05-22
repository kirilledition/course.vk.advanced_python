import collections
import cProfile
import io
import pstats
import weakref

import memory_profiler


class CacheOriginal:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.order = collections.deque()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache[key]

    def set(self, key: int, value: int) -> None:
        if key in self.cache:
            self.order.remove(key)
        self.order.append(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.pop(self.order[0])
            self.order.remove(self.order[0])


class CacheSlot(CacheOriginal):
    __slots__ = ("capacity", "cache", "order")


class CacheWeakRef(CacheOriginal):
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = weakref.WeakValueDictionary()
        self.order = collections.deque()


def create_original():
    [CacheOriginal(4) for _ in range(100_000)]


def create_slots():
    [CacheSlot(4) for _ in range(100_000)]


def create_weakref():
    [CacheWeakRef(4) for _ in range(100_000)]


@memory_profiler.profile
def mem_stat():
    create_original()
    create_slots()
    create_weakref()


def cpu_stat():
    path = "/Users/kirilldenisov/Desktop/course.vk.deep_python/08.Profiling/"
    pr = cProfile.Profile()
    pr.enable()

    create_original()
    create_slots()
    create_weakref()

    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats(pstats.SortKey.CUMULATIVE)
    ps.print_stats()
    print("```\n", s.getvalue().replace(path, ""), "```")


if __name__ == "__main__":
    mem_stat()
    cpu_stat()
