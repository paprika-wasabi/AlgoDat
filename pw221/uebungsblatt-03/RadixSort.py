"""
Bucketsort implementation using linked lists

Copyright 2020, University of Freiburg.

Philipp Schneider <philipp.schneider@cs.uni-freiburg.de>
"""

import random
import time
from BucketSort import bucket_sort
import math


def radix_sort(array, k):
    '''
    Implements the radix sort algorithm to sort
        data elements with keys in range(k+1)

    Args:
        array: array of data elements
        k: largest key
        key: a function mapping data elements to values
        in range(k+1) (idendity function as default)

    >>> array = [10-i for i in range(10)]
    >>> radix_sort(array, 10)
    >>> str(array)
    '[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]'
    '''
    m = int(math.log(k))
    for i in range(m):
        bucket_sort(array, k, key=lambda x: (x % (10**(i + 1))) // 10**i)


def radix_sort_performance():
    '''
    Method that outputs key range and elapsed time for sorting.
    '''
    for k in range(10**4, (12 * (10**5)) + 1, 2 * 10**4):
        array = [random.randint(0, k) for i in range(10**4)]
        start_time = time.time()
        radix_sort(array, k)
        run_time = (time.time() - start_time) * 1000
        print("%d\t%.1f" % (k, run_time))


if __name__ == "__main__":
    radix_sort_performance()
    # array = [100 - i for i in range(100)]
    # radix_sort(array, 100)
    # print(array)
    # array2 = [99, 100, 300, 2, 5, 7, 24, 20, 69, 75, 222, 111, 150, 250]
    # radix_sort(array2, 300)
    # print(array2)
