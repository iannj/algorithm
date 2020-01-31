#!/usr/bin/env python3
# -*— coding=utf-8 -*-

"""Bubble Sort Algorithm:
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.
This function is the implementation of Bubble Sort Algorithm in python. In this function, a variable swapped is defined. If no elements are swapped, which means that all elements are in order. a break command will stop the looping as soon as possible.
"""


def bubble_sort(collection):
    """
    The implementation of bubble sort algorithm in python
    :param collection: some mutable ordered collection with heterogeneous comparable items inside.The keywords are mutable/immutable,orderd,comparable and heterogeneous.
    :return: the same collection ordered by ascending

    Examples:
    """
    length = len(collection)

    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i): # The head or tail element must be order.
            if collection[j] > collection[j + 1]: # A Comparison operator '>' here makes ascending. Changing the operator, change the order.
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
                swapped = True
        if not swapped:
            break
    return collection


if __name__ == "__main__":
    a = [1, 5, 3, 8]
    print(bubble_sort(a))
