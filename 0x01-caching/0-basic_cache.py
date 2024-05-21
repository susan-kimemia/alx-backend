#!/usr/bin/python3
"""
 Basic dictionary for caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    a class BasicCache that inherits from BaseCaching and is a caching system
    """
    def put(self, key, item):
        """
        method  assign to the dictionary self.cache_data the
        item value for the key key
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
