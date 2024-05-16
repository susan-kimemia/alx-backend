#!/usr/bin/env python3
"""
simple helper function
"""
import csv
import math
from typing import List, Dict


def index_range(page, page_size):
    """
    The function should return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes to return in a
    list for those particular pagination parameters
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Simple pagination
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start_index, end_index = index_range(page, page_size)
        data = self.dataset()
        if start_index > len(data):
            return []
        return data[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        method that takes the same arguments (and defaults) as
        get_page and returns a dictionary
        containing the following key-value pairs
        """
        # Call get_page method to retrieve dataset page
        dataset_page = self.get_page(page, page_size)

        # Calculate total number of pages
        total_pages = math.ceil(len(self.__dataset) / page_size)

        # determinig the next page
        next_page = page + 1 if page < total_pages else None

        # determing the previous page
        prev_page = page - 1 if page > 1 else None

        hyper_dict = {
                'page_size': len(dataset_page),
                'page': page,
                'data': dataset_page,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages
                }
        return hyper_dict
