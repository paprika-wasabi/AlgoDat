"""
Bucketsort implementation using linked lists

Copyright 2020, University of Freiburg.

Philipp Schneider <philipp.schneider@cs.uni-freiburg.de>
"""

import random
import time
from Queue import Queue
from ListElement import ListElement


def bucket_sort(array, k, key=lambda x: x):
    '''
    Implements the bucket sort algorithm to sort
        data elements using a key function to
        assign sorting keys to data elements

    Args:
        array: array of data elements
        k: largest key
        key: a function mapping data elements to values
        in range(k+1) (idendity function as default)

    >>> array = [10-i for i in range(10)]
    >>> bucket_sort(array, 10)
    >>> str(array)
    '[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]'
    '''
    bucket = []
    # create k + 1 buckets and init Queue Object inside.
    for i in range(k + 1):
        bucket.append(Queue())
    for j in range(len(array)):
        x = key(array[j])
        bucket[x].enqueue(ListElement(array[j]))
    n = 0
    e = 0
    while n < k and e < len(array):
        # if bucket[n] is empty then move to next bucket.
        if bucket[n].is_empty():
            n += 1
        # if bucket[n] is not empty then distributes element in array[e].
        if bucket[n].is_empty() is False:
            array[e] = bucket[n].dequeue().get_key()
            e += 1


def bucket_sort_performance():
    '''
    Method that outputs key range and elapsed time for sorting.
    '''
    for k in range(10**4, (12 * (10**5)) + 1, 2 * 10**4):
        array = [random.randint(0, k) for i in range(10**4)]
        start_time = time.time()
        bucket_sort(array, k)
        run_time = (time.time() - start_time) * 1000
        print("%d\t%.1f" % (k, run_time))


if __name__ == "__main__":
    # array1 = [10 - i for i in range(10)]
    # array2 = [7, 2, 3, 1, 8, 9, 4, 5, 10, 6]
    # array3 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    # bucket_sort(array1, 10)
    # print(array1)
    # bucket_sort(array2, 10)
    # print(array2)
    # bucket_sort(array3, 10)
    # print(array3)
    bucket_sort_performance()
