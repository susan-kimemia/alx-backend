#!/usr/bin/python3
"""
MRU models
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache that inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """
        Initializes the MRUCache instance.
        """
        super().__init__()
        self.usedKeys = []

    def put(self, key, item):
        """
        Assigns the item value for the key key.
        If key or item is None, this method will not do anything.
        If the number of items in self.cache_data is higher than MAX_ITEMS:
        the most recently used item (MRU) will be removed.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.usedKeys:
                self.usedKeys.append(key)
            else:
                self.usedKeys.remove(key)
                self.usedKeys.append(key)
            if len(self.usedKeys) > BaseCaching.MAX_ITEMS:
                #  Pop the second-to-last used key
                discard_key = self.usedKeys.pop(-2)
                del self.cache_data[discard_key]
                print('DISCARD: {:s}'.format(discard_key))

    def get(self, key):
        """
        Returns the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in
        self.cache_data, return None.
        """
        if key is not None and key in self.cache_data:
            self.usedKeys.remove(key)
            self.usedKeys.append(key)
            return self.cache_data.get(key)
        return None
