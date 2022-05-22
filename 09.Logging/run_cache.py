import argparse
import collections
import logging
import sys


class LRUCache:
    def __init__(self, capacity: int, logger=None):
        self.capacity = capacity
        self.cache = {}
        self.order = collections.deque()

        if logger is not None:
            self.logger = logger
        else:
            self.logger = logging.getLogger(__name__)

    def get(self, key: int) -> int:
        if key not in self.cache:
            self.logger.debug("object at the key %s is not found", key)
            return None
        self.order.remove(key)
        self.order.append(key)
        self.logger.info("Object at the key %s is accessed", key)
        return self.cache[key]

    def set(self, key: int, value: int) -> None:
        if key in self.cache:
            self.order.remove(key)
            self.logger.debug("Key %s is moved to the end of the order", key)
        self.order.append(key)
        self.cache[key] = value
        self.logger.info("Object is set at the key %s", key)
        if len(self.cache) > self.capacity:
            self.cache.pop(self.order[0])
            self.order.remove(self.order[0])
            self.logger.debug("Object is at the key %s is popped", key)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--stdout", action="store_true")
    parser.add_argument(
        "-o", "--outfile", type=str, default="output.log", help="output file"
    )
    return parser.parse_args()


def main():
    args = parse_args()
    logging.basicConfig(
        filename=args.outfile,
        level=logging.DEBUG,
    )
    logger = logging.getLogger(__name__)

    if args.stdout:
        streamHandler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "%(asctime)s\t%(levelname)s\t%(message)s", datefmt="%d.%m.%Y %I:%M:%S"
        )
        streamHandler.setFormatter(formatter)
        logger.addHandler(streamHandler)

    cache = LRUCache(2, logger)
    cache.set("k1", "val1")
    cache.set("k2", "val2")
    cache.get("k3")
    cache.get("k1")
    cache.set("k3", "val3")
    cache.get("k3")
    cache.get("k2")
    cache.get("k1")


if __name__ == "__main__":
    main()
