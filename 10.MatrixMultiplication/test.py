from timeit import timeit
import os

os.system("python setup.py build_ext --inplace")

if __name__ == "__main__":
    chain = "[[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[5, 6], [7, 8]]]"
    cmd = f"multiply_chain({chain})"

    cres = timeit(
        cmd,
        setup="from cmatmul import multiply_chain",
        number=1000,
    )

    res = timeit(
        cmd,
        setup="from pymatmul import multiply_chain",
        number=1000,
    )

    print(f"timeit results:\npy: {res:.5f} cpp: {cres:.5f} diff {res - cres:.5f}")
