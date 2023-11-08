import threading

from lru_decorator import LruCacheDecorator

cache_decorator = LruCacheDecorator(capacity=3)


@cache_decorator
def square(number: int) -> int:
    return number * number


def test_decorator():

    assert square(1) == 1  # expected print: Running function, [1]

    assert square(2) == 4  # expected print: Running function, [1,2]

    assert square(2) == 4  # expected print: Getting key from cache, [1,2]

    assert square(3) == 9  # expected print: Running function, [1,2,3]

    assert square(1) == 1  # expected print: Getting key from cache, [2,3,1]

    assert square(4) == 16  # expected print: Running function, [3,1,4]

    assert square(2) == 4  # expected print: Running function, [1,4,2]


if __name__ == '__main__':
    line = "Basic Tests"
    print(f"{line:-^60}")

    test_decorator()