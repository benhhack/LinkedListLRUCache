from typing import Union

from node import Node


class LruCacheLL:
    """
    Doubly linked list implementation of and LRU cache.
    """

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = {}

        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node: Node) -> None:
        """
        Removes a node from the linked list.

        :param node: Node
        :return: None
        """
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert_right(self, node: Node) -> None:
        """
        Inserts a node at the tail of the list.

        :param node:
        :return: None
        """
        prev, nxt = self.tail.prev, self.tail
        prev.next, node.prev = node, prev
        node.next, nxt.prev = nxt, node

    def get(self, key: int) -> Union[int, None]:
        """
        Returns value if in cache, reorders the list.

        :param key: int
        :return: int or None
        """
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert_right(self.cache[key])
            return self.cache[key].val

        return None

    def put(self, key: int, val: int) -> None:
        """

        :param key: int
        :param val: int
        :return: None
        """
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, val)
        self.insert_right(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]

    def print_cache(self) -> None:
        """
        To ensure our cache is being used correctly
        :return:
        """
        node = self.head.next
        out = []
        while node.next:
            out.append(node.key)
            node = node.next
        print(out)
