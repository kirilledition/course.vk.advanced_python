import collections


class LRUCache:
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
