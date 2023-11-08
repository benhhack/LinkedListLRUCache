from functools import wraps

from lru_cache import LruCache


class LruCacheDecorator:
    """
    Implementation of a linked list based LRU Cache decorator for single argument functions.
    """

    def __init__(self, capacity):
        self.cache = LruCache(capacity)

    def __call__(self, func):
        @wraps(func)
        def wrapped(key):
            if key in self.cache.cache:
                print("Getting key from cache")
                res = self.cache.get(key)
            else:
                print("Running function")
                res = func(key)
                self.cache.put(key, res)
            self.cache.print_cache()
            return res


        return wrapped