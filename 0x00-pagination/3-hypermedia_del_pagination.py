#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Deletion-resilient hypermedia pagination
        """
        # Validate index argument
        assert index is None or (isinstance(index, int) and index >= 0)
        # Calculate start index of the return page
        start_index = index if index is not None else 0

        # Calculate next index to query with
        next_index = start_index + page_size

        # Retrieve the actual page of the dataset
        dataset_page = self.__dataset[start_index:next_index]

        # Construct dictionary with hypermedia information
        hyper_index_dict = {
                'index': start_index,
                'next_index': next_index,
                'page_size': page_size,
                'data': dataset_page
        }
        return hyper_index_dict
