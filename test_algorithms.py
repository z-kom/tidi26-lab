import random

from algorithms import (
    two_pointers,
    binary_search,
    exponential_search,
    double_binary_search,
)

ALGOS = {
    "two_pointers": two_pointers,
    "binary_search": binary_search,
    "exponential_search": exponential_search,
    "double_binary": double_binary_search,
}


def brute(a, b):
    return bool(set(a) & set(b))


def check(a, b, expected):
    for name, func in ALGOS.items():
        got = func(a, b)
        assert got == expected, (
            f"{name}: a={a}, b={b}, expected={expected}, got={got}"
        )


def test_examples():
    check([1, 2, 3], [3, 4, 5], True)
    check([2, 4, 6], [3, 5, 7], False)
    check([], [], False)
    check([], [1, 2, 3], False)
    check([1, 2, 3], [], False)


def test_edges():
    check([1], [1], True)
    check([1], [2], False)
    check([1, 1, 1], [1], True)
    check([1, 1, 1], [2], False)
    check([-5, -3, 0, 4], [-3, 10], True)
    check([-5, -3, 0, 4], [-4, -2, 1], False)
    check([1, 2, 2, 3], [2, 2, 4], True)
    check([1, 2, 2, 3], [4, 5, 6], False)


def random_sorted(n, maxx=100):
    return sorted(random.randint(-maxx, maxx) for _ in range(n))


def test_random():
    random.seed(67)
    for _ in range(5000):
        m = random.randint(0, 40)
        n = random.randint(0, 40)
        a = random_sorted(m)
        b = random_sorted(n)
        check(a, b, brute(a, b))


if __name__ == "__main__":
    test_examples()
    test_edges()
    test_random()
    print("Все тесты пройдены.")
