import itertools
import operator
import functools


class CustomList(list):
    def __str__(self):
        return ", ".join([str(i) for i in self]) + ": " + str(sum(self))

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __operation(self, other, operation):
        res = []
        for i, j in itertools.zip_longest(self, other, fillvalue=0):
            r = operation(i, j)
            res.append(r)

        return CustomList(res)

    __add__ = functools.partialmethod(__operation, operation=operator.add)
    __radd__ = __add__

    __sub__ = functools.partialmethod(__operation, operation=operator.sub)
    __rsub__ = functools.partialmethod(__operation, operation=lambda a, b: b - a)
