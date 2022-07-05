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

        # >>> array = [20,1]
        # >>> quicksort(array, True)
        # >>> array
        # [1, 20]
        # >>> array = [20,1]
        # >>> quicksort(array, False)
        # >>> array
        # [1, 20]
    """
    # if the given array is has no reason to be ordered
    if len(array) == 1:
        return array
    if array == []:
        return None
    # will call quicksort_recursive
    left = 0
    right = len(array)
    return quicksort_recursive(array, left, right - 1, randomized)


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
    # For a simple array that requires no rearrangement
    # if len(array) <= 1:
    #     return
    # else:
    #     if left < right:
    #         index = quicksort_divide(array, left, right, randomized)
    #         # Recursive Calls for each division
    #         quicksort_recursive(array, left, index - 1, randomized)
    #         quicksort_recursive(array, index + 1, right, randomized)
    # return array
    if left >= right:
        return
    index = quicksort_divide(array, left, right, randomized)
    quicksort_recursive(array, left, index - 1, randomized)
    quicksort_recursive(array, index + 1, right, randomized)
    return array


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
    if array == []:
        return 0
    # check if array more than 1
    if len(array) == 1:
        return 0
    # Chosing how pivot are pick
    if randomized is True:
        k = randint(left, right)
        pivot = array[k]
        (array[left], array[k]) = (array[k], array[left])
    else:
        pivot = array[left]
    # Rearrangement of the parts
    i = left + 1
    j = right
    while(i < j):
        while(array[j] > pivot):
            j -= 1
        while(array[i] < pivot):
            i += 1
            if(i == right):
                break
        if(i < j):
            (array[i], array[j]) = (array[j], array[i])
    (array[left], array[j]) = (array[j], array[left])
    return j


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
    # arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 100, 4]
    # print(quicksort(arr, randomized=True))
    quick_sort_performance(False, True)
    # arr1 = [80, 1, 5, 3, 30, 2, 18, 15, 11, 100]
    # print(quicksort(arr1, randomized=False))
    # arr2 = [21, 1, 300, 7, 20, 2, 19, 15, 31, 110]
    # print(quicksort(arr2, randomized=False))
    # arr3 = [41, 20, 32, 58, 69, 70, 75, 23, 84, 1, 2, 3]
    # print(quicksort(arr3, randomized=False))
