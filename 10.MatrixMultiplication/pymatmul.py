def multiply(a, b):
    num_rows = len(a)
    num_cols = len(b[0])

    result = [[0 for _ in range(num_cols)] for _ in range(num_rows)]

    for i in range(num_rows):
        for j in range(num_cols):
            for k in range(num_cols):
                result[i][k] += a[i][j] * b[j][k]

    return result


def multiply_chain(chain):
    result = chain[0]

    for elem in chain[1:]:
        result = multiply(result, elem)

    return result
