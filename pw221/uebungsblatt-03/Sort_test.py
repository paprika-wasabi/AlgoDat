"""
//  Test Implemantation of RadixSort and BucketSort.
//  Copyright 2022, University of Freiburg.
//  Sort_test.py
//  AlgoDat
//
//  Created by Paramie Willmann on 17.05.22.
//
"""

import unittest
from BucketSort import bucket_sort
from RadixSort import radix_sort


class SortTest(unittest.TestCase):
    def test_bucket_sort(self):
        array1 = [10 - i for i in range(10)]
        self.assertEqual(bucket_sort(array1, 10), [i for i in range(1, 11)])
        array2 = [7, 2, 3, 1, 8, 9, 4, 5, 10, 6]
        self.assertEqual(bucket_sort(array2, 10), [i for i in range(1, 11)])
        array3 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        self.assertEqual(bucket_sort(array3, 10), [i for i in range(0, 10)])

    def test_radix_sort(self):
        array1 = [100 - i for i in range(100)]
        self.assertEqual(radix_sort(array1, 100), [i for i in range(1, 101)])
        array2 = [99, 100, 300, 2, 5, 7, 24, 20, 69, 75, 222, 111, 150, 250]
        self.assertEqual(radix_sort(array2, 300), [2, 5, 7, 20, 24, 69, 75,
                         99, 100, 111, 150, 222, 250, 300])
        array3 = [10 - i for i in range(10)]
        self.assertEqual(radix_sort(array3, 10), [i for i in range(1, 11)])
