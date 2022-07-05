"""
Implementation of QuickSort algorithm with different methods of
choosing the pivot method.

Copyright 2016, University of Freiburg.
Olelsii Saukh <saukho@cs.uni-freiburg.de>
"""

import sys
import time
from random import randint


# Quicksort might cause a recursion depth >5000 -> increase limit
sys.setrecursionlimit(6000)


def quicksort(array, randomized=True):
    """
    Sort array in ascending order. Wrapper for the sorting method.

    Args:
        int[] array:    integer array
        bool randomized:    method how to pick pivot. True if randomized.

        >>> array = [20,1]
        >>> quicksort(array, True)
        >>> array
        [1, 20]
        >>> array = [20,1]
        >>> quicksort(array, False)
        >>> array
        [1, 20]
    """


def quicksort_recursive(array, left, right, randomized):
    """
    Method that recursively divides array on parts and calls the
    rearrangement procedure on each part.

    Args:
        int[] array:    integer array that has to be sorted
        int left:    left index from which the rearrangement starts.
        int right:    right index till which the rearrangement goes.
        bool randomized:    method how to pick pivot. True if randomized.
    """


def quicksort_divide(array, left, right, randomized):
    """
    Method that executes the divide step of the algorithm. Method chooses
    pivot element and  performs arranges the elements inside the array in such
    a way, that elements that are smaller than pivot are placed to the left of
    it, and elements that are larger that pivot are placed the the right of
    pivot (arbitrary for elements equal to pivot).

    Args:
        int[] array:    integer array that has to be rearranged.
        int left:    left index from which the rearrangement starts.
        int right:    right index till which the rearrangement goes.
        bool randomized:    method how to pick pivot. True if randomized.
    Returns:
        int:    index where the pivot after the split is located.
    """


def quick_sort_performance(rand_values=True, rand_pivot=True):
    """
    Method that outputs array size and elapsed time for sorting.

    Args:
        rand_values:    True if array should contain random values
        rand_pivot:    switch pivot strategy for evaluation
    """

    for n in range(100, 5001, 100):
        if rand_values:
            array = [randint(0, 5000) for i in range(n)]
        else:
            array = [k for k in range(n, 0, -1)]

        start_time = time.time()
        quicksort(array, rand_pivot)
        run_time = (time.time() - start_time) * 1000
        print("{}\t{:.1f}".format(n, run_time))


if __name__ == "__main__":
    quick_sort_performance(False, False)
