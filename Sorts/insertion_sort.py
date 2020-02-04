#!/usr/env/bin python3
# -*- coding=utf-8 -*-

"""Insertion Sort Algorithm
Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.Here is how it works.
  - Index *i is the current element. All the elements before current are sorted.
  - Using index *j to traversal all the elements before, finding out the element greater than the current one, inserting it before.
  - Using index *i to traversal all the element.
"""


def insertion_sort(collection: list):
    length = len(collection)

    for i in range(length):
        if i > 0:
            for j in range(i):
                if collection[j] > collection[i]:
                    collection.insert(j, collection[i])
                    collection.pop(i + 1)


if __name__ == '__main__':
    a = [1, 3, 6, 2, 4, 2, 6, 8, 5, 7, 5]
    insertion_sort(a)
    print(a)
