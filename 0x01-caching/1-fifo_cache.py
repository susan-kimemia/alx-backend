#!/usr/bin/python3
"""
FIFO caching module
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache that inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """
        overloading and to calling the parent init
        """
        super().__init__()

    def put(self, key, item):
        """
        Method that assign to the dictionary self.cache_data the
        item value for the key keyIf key or item is None,
        this method will not do anything.
        If the number of items in self.cache_data is higher that MAX_ITEMS:
        you must discard the first item put in cache (FIFO algorithm)
        you must print DISCARD: with the key discarded and following by newline
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS and \
                key not in self.cache_data.keys():
            # Find the first item inserted and remove it
            first_item_key = next(iter(self.cache_data.keys()))
            del self.cache_data[first_item_key]
            print(f"DISCARD: {first_item_key}")

        self.cache_data[key] = item

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
