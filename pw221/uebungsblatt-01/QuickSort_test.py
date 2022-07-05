"""
//  Test Implemantation of QuickSort
//  Copyright 2022, University of Freiburg.
//  QuickSort_test.py
//  AlgoDat
//
//  Created by Paramie Willmann on 01.05.22.
//
"""

import unittest
from QuickSort import quicksort_divide, quicksort_recursive


class QuickSortTest(unittest.TestCase):
    def test_quicksort_dive(self):
        arr1 = [8, 1, 3, 5, 20, 2, 18, 15, 11, 100]
        self.assertEqual(quicksort_divide(arr1, 0, len(arr1) - 1, False), 4)
        arr2 = [0]
        self.assertEqual(quicksort_divide(arr2, 0, len(arr2) - 1, False), 0)
        arr3 = []
        self.assertEqual(quicksort_divide(arr3, 0, len(arr3) - 1, False), 0)
        arr4 = [41, 20, 32, 58, 69, 70, 71, 23, 84, 1, 2, 3]
        self.assertEqual(quicksort_divide(arr4, 0, len(arr4) - 1, False), 6)
        arr5 = [1, 20]
        self.assertEqual(quicksort_divide(arr5, 0, len(arr5) - 1, False), 1)

    def test_quicksort_recursive(self):
        arr1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20, 21, 30]
        self.assertEqual(quicksort_recursive(arr1, 0, len(arr1), False), [
                         1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 21, 30
                         ])
        arr2 = [80, 1, 3, 5, 30, 2, 18, 15, 11, 100]
        self.assertEqual(quicksort_recursive(arr2, 0, len(arr2), False), [
                         1, 2, 3, 5, 11, 15, 18, 30, 80, 100
                         ])
        arr3 = [21, 1, 300, 7, 20, 2, 19, 15, 31, 110]
        self.assertEqual(quicksort_recursive(arr3, 0, len(arr3), False), [
                         1, 2, 7, 15, 19, 20, 21, 31, 110, 300
                         ])
        arr4 = [1, 20]
        self.assertEqual(quicksort_recursive(arr4, 0, len(arr4), False), [
                         1, 20
                         ])
        arr5 = [20, 1]
        self.assertEqual(quicksort_recursive(arr5, 0, len(arr5), False), [
                         1, 20
                         ])
        arr6 = []
        self.assertEqual(quicksort_recursive(arr6, 0, len(arr6), False), None)
        arr7 = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(quicksort_recursive(arr7, 0, len(arr7), False), [
                         1, 2, 3, 4, 5, 6, 7
                         ])
