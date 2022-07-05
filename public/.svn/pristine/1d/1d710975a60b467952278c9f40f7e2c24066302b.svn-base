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


def quicksort(array, if_randomized=True):
    """
    Sort array in ascending order. Wrapper for the sorting method.

    Args:
        int[] array:    integer array
        bool if_randomized:    method how to pick pivot. True if randomized.

        >>> array = [0, 7, -2, 11, 5, 120, 0, 11, 6, 7, 11, -2, -2]
        >>> quicksort(array, True)
        >>> array
        [-2, -2, -2, 0, 0, 5, 6, 7, 7, 11, 11, 11, 120]
        >>> array = [0, 7, -2, 11, 5, 120, 0, 11, 6, 7, 11, -2, -2]
        >>> quicksort(array, False)
        >>> array
        [-2, -2, -2, 0, 0, 5, 6, 7, 7, 11, 11, 11, 120]

        >>> array = [20,1]
        >>> quicksort(array, True)
        >>> array
        [1, 20]
        >>> array = [20,1]
        >>> quicksort(array, False)
        >>> array
        [1, 20]

        >>> array = []
        >>> quicksort(array, True)
        >>> array
        []
        >>> quicksort(array, True)
        >>> array
        []
    """

    if len(array) <= 1:
        return
    quicksort_recursive(array, 0, len(array) - 1, if_randomized)


def quicksort_recursive(array, left, right, if_randomized):
    """
    Method that recursively divides array on parts and calls the
    rearrangement procedure on each part.

    Args:
        int[] array:    non-empty integer array that has to be sorted
        int left:    left index from which the rearrangement starts.
        int right:    right index till which the rearrangement goes.
        bool if_randomized:    method how to pick pivot. True if randomized.

        >>> array = [0, 7, -2, 11, 5, 120, 0, 11, 6, 7, 11, -2, -2]
        >>> quicksort_recursive(array, 4, 12, True)
        >>> array
        [0, 7, -2, 11, -2, -2, 0, 5, 6, 7, 11, 11, 120]
        >>> quicksort_recursive(array, 4, 12, False)
        >>> array
        [0, 7, -2, 11, -2, -2, 0, 5, 6, 7, 11, 11, 120]
    """

    if left < right:
        split_index = quicksort_divide(array, left, right, if_randomized)
        quicksort_recursive(array, left, split_index - 1, if_randomized)
        quicksort_recursive(array, split_index + 1, right, if_randomized)


def quicksort_divide(array, left, right, if_randomized):
    """
    Method that executes the divide step of the algorithm. Method chooses
    pivot element and performs rearrangement of the elements inside of
    the array in such a way, that elements that are smaller than pivot are
    placed to the left of it, and elements that are larger that pivot are
    placed the the right of pivot (arbitrary for elements equal to pivot).

    Args:
        int[] array:    integer array that has to be rearranged.
        int left:    left index from which the rearrangement starts.
        int right:    right index till which the rearrangement goes.
        bool if_randomized:    method how to pick pivot. True if randomized.
    Returns:
        int:    index where the pivot after the split is.

        >>> array = [0, 7, -2, 11, 5, 120, 0, 11, 6, 7, 11, -2, -2]
        >>> quicksort_divide(array, 0, 12, False)
        3
        >>> array
        [-2, -2, -2, 0, 5, 120, 0, 11, 6, 7, 11, 11, 7]
    """

    pivot = get_pivot(array, left, right, if_randomized)
    le = left
    ri = right
    while le < ri:
        while le <= ri and array[le] <= pivot:
            le += 1
        while le <= ri and array[ri] >= pivot:
            ri -= 1
        if le < ri:
            swap(array, le, ri)
    # swap pivot into the middle
    swap(array, left, ri)
    return ri


def swap(array, first, second):
    """
    Swap two elements of an array.

    Args:
        int[] array:   integer array where elements have to be swapped.
        int first:   left index from which the rearrangement starts.
        int second:   right index till which the rearrangement goes.
    """

    array[first], array[second] = array[second], array[first]


def get_pivot(array, left, right, if_randomized):
    """
    Method that returns value of pivot - one of elements of the array
    between indices left and right.

    Args:
        int[] array:    array for which we need to get pivot
        int left:    left border of array interval
        int right:    right border of array interval.
        bool if_randomized:    method how to pick pivot. True if randomized.
    Returns:
        int:    value of pivot element.
    """

    if if_randomized is False:
        return array[left]

    index = randint(left, right)
    swap(array, left, index)
    return array[left]


def quick_sort_performance(rand_values=True, rand_pivot=True):
    for n in range(100, 5001, 100):
        if rand_values:
            array = [randint(0, 5000) for i in range(n)]
        else:
            array = [k for k in range(n, 0, -1)]

        start_time = time.time()
        quicksort(array, rand_pivot)
        run_time = (time.time() - start_time) * 1000
        print("%d\t%.1f" % (n, run_time))


if __name__ == "__main__":
    quick_sort_performance(True, True)
