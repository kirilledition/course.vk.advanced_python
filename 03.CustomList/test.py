from custom_list import CustomList


def compare_values(a, b):
    for i, j in zip(a, b):
        if i != j:
            return False
    return True


def test_add():
    true_result = [6, 3, 10, 7]
    a = [5, 1, 3, 7]
    b = [1, 2, 7]
    custom_result = CustomList(a) + CustomList(b)
    assert compare_values(true_result, custom_result)

    ladd_result = a + CustomList(b)
    assert compare_values(true_result, ladd_result)

    radd_result = CustomList(a) + b
    assert compare_values(true_result, radd_result)


def test_substract():
    true_result = [4, -1, -4, 7]
    a = [5, 1, 3, 7]
    b = [1, 2, 7]
    custom_result = CustomList(a) - CustomList(b)
    assert compare_values(true_result, custom_result)

    ladd_result = a - CustomList(b)
    assert compare_values(true_result, ladd_result)

    radd_result = CustomList(a) - b
    assert compare_values(true_result, radd_result)


def test_comparison():
    assert CustomList([2, 2]) == CustomList([1, 3])
    assert CustomList([2, 2]) >= CustomList([1, 3])
    assert CustomList([2, 2]) <= CustomList([1, 3])
    assert CustomList([1, 2]) < CustomList([1, 3])
    assert CustomList([3, 2]) > CustomList([1, 3])


def test_str():
    a = CustomList([1, 2])
    assert str(a) == "1, 2: 3"
    b = CustomList([])
    assert str(b) == ": 0"
