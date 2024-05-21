#!/usr/bin/python3
"""
LRU caching module
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache that inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """
        Initializes the LRUCache instance.
        """
        super().__init__()
        self.usedKeys = []

    def put(self, key, item):
        """
        Assigns the item value for the key key.
        If key or item is None, this method will not do anything.
        If the number of items in self.cache_data is higher than MAX_ITEMS:
        the least recently used item (LRU) will be removed.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.usedKeys:
                self.usedKeys.append(key)
            else:
                self.usedKeys.append(self.usedKeys.pop(
                    self.usedKeys.index(key)))
            if len(self.usedKeys) > BaseCaching.MAX_ITEMS:
                terminate = self.usedKeys.pop(0)
                del self.cache_data[terminate]
                print('DISCARD: {:s}'.format(terminate))

    def get(self, key):
        """
        Returns the value in self.cache_data linked to key and marks it as
        most recently used.
        """
        if key is not None and key in self.cache_data.keys():
            self.usedKeys.append(self.usedKeys.pop(self.usedKeys.index(key)))
            return self.cache_data.get(key)
        return None
