"""
Декоратор который получает один параметр число
и засыпает на это число секунд
"""

import functools
import time


def sleeper(seconds):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            time.sleep(seconds)
            return result

        return wrapper

    return decorator


@sleeper(1.34)
def return_five():
    return 5


def main():
    start = time.time()
    print(return_five())
    print("Execution time:", time.time() - start)


if __name__ == "__main__":
    main()
