#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""Quick Sort Algorithm
Quick Sort Algorithm is a typical recursive sorting algorithm. There are 3 kinds of quick sort algorithm.
1. quick sort 1-way algorithm
Here is how the algorithm works.
 - Index *l is the left edge of the collection.
 - Index *r is the right edge of the collection.
 - Pivot v is the first element which is indexed with *l
 - There are 2 partitions inside. The left partition contents all the elements lesser than v. The right partition contents all the elements greater than v.
 - Index *j is the left edge of right partition, setting l + 1 as default.
 - Index *i is a self-increasing index which points to the current element, starting from l+1 and stopping at r.
 - As *i increases, you'd compare the current element with v and put it in the left partition while it is lesser.
 - At the end of this round, you'd swap v and *j - 1, which is the right edge of left partition. Then you get [l ... j - 2] << lesser << [v] >> greater >> [j ... r]
 - Recurse the left partition and the right partition.

2. quick sort 2-way algorithm
Here is how the algorithm works.
 - Pivot v is the last element of collection.
 - Collection lesser is the extension partition contents all the elements lesser than v.
 - Collection greater is the extension partition contents all the elements greater than v.
 - Rejoin them then you get [lesser] [v] [greater].
 - To each partition, you may recurse it.

3. quick sort 3-way algorithm
Here is how the algorithm works.
 - Index *l is the left edge of the collection.
 - Index *r is the right edge of the collection.
 - Pivot v is the first element which is indexed with *l
 - There are 3 partitions inside. The left partition contents all the elements lesser than v. The right partition contents all the elements greater than v. The middle partition contents all the elements equal to v.
 - Index *lt is the left edge of middle partition, setting l as default.
 - Index *gt is the right edge of middle partition, setting r as default.
 - Index *i is a self-increasing index which points to the current element, starting from l  and stopping at gt.
 - As *i increases, you'd compare the current element with v. Now, you have 3 status.
    - lesser. Put the current in the left partition, increase lt and keep going.
    - equal. It should be here. Do nothing and keep going.
    - greater. Put the current in the right partition, subtract gt. Notice here, as you swap the current and the gt, current should be a new one. You may recheck it.
    - At the end of this round, you may get [l ... lt - 1] << lesser << [lt ... gt] >> greater >> [gt+1 ... r]
 - Recurse the left partition and the right partition.

"""


def partition(collection, l, r):
    """
    The partition function works for quick sort 1-way algorithm.
    :param collection: some mutable ordered collection with heterogeneous comparable items inside.
    :param l: the start index of collection.
    :param r: the end index of collection.
    :return: the index *j - 1 of partition
    """
    # v is the pivot this round
    v = collection[l]

    # *i is the self-increasing index pointing to current element, starting from l + 1
    # *j is the left edge of right partition, starting from l + 1
    # *j - 1 is the position of v at the end of this round

    j = l + 1
    for i in range(l + 1, r + 1):
        if collection[i] <= v:
            collection[j], collection[i] = collection[i], collection[j]
            j += 1
    collection[l], collection[j - 1] = collection[j - 1], collection[l]

    return j - 1


def quick_sort_1_way(collection, l, r):
    """
    The implementation of quick sort 1-way algorithm in python. This function works with function partition together.
    :param collection: the mutable ordered collection with heterogeneous comparable items inside.
    :param l: the left edge of collection
    :param r: the right edge of collection
    :return: None
    """
    if l < r:
        m = partition(collection, l, r)
        quick_sort_1_way(collection, l, m - 1)
        quick_sort_1_way(collection, m + 1, r)


def quick_sort_1_way_in_1(collection, l, r):
    """
    The implementation of quick sort 1-way algorithm in one function in python
    :param collection: the mutable ordered collection with heterogeneous comparable items inside.
    :param l: the left edge of collection.
    :param r: the right edge of collection.
    :return: None
    """
    if l < r:
        # v is the pivot of this round
        v = collection[l]

        # *i is a self-increasing index pointing to current element, starting from l + 1
        # *j is the left edge of right partition, starting from l + 1
        # *j - 1 is the position of v at the end of this round
        i = j = l + 1
        while i <= r:
            if collection[i] < v:
                collection[i], collection[j] = collection[j], collection[i]
                j += 1
            i += 1
        collection[l], collection[j - 1] = collection[j - 1], collection[l]
        quick_sort_1_way_in_1(collection, l, j - 1)
        quick_sort_1_way_in_1(collection, j, r)
    else:
        return


def quick_sort_3_way(collection, l, r):
    """
    The implementation of quick sort 3-way algorithm in python
    :param collection: the mutable ordered collection with heterogeneous comparable items inside.
    :param l: the left edge of collection.
    :param r: the right edge of collection.
    :return: None
    """
    if l < r:
        # *lt is the left edge of middle partition, starting from l
        # *gt is the right edge of middle partition, starting from r
        # *i is a self-increasing index pointing to current element, starting from l
        lt = i = l
        gt = r
        # v is the pivot this round
        v = collection[l]
        while i <= gt:
            if collection[i] < v:
                collection[lt], collection[i] = collection[i], collection[lt]
                lt += 1
                i += 1
            elif collection[i] > v:
                collection[gt], collection[i] = collection[i], collection[gt]
                gt -= 1
            else:
                i += 1
        quick_sort_3_way(collection, l, lt - 1)
        quick_sort_3_way(collection, gt + 1, r)
    else:
        return


def quick_sort_2_way(collection):
    """
    The implementation of quick sort 2-way algorithm in python.
    :param collection: some mutable ordered collection with heterogeneous comparable items inside.
    :return: the same collection ordered by ascending.
    """
    length = len(collection)
    if length <= 1:
        return collection
    else:
        pivot = collection.pop()
        lesser, greater = [], []
        for element in collection:
            if element <= pivot:
                lesser.append(element)
            else:
                greater.append(element)
        return quick_sort_2_way(lesser) + [pivot] + quick_sort_2_way(
            greater)  # recursive here. the lesser ahead runs ascending order.


if __name__ == '__main__':
    a = [1, 3, 6, 2, 4, 7, 5]
    category = 2

    if category == 1:
        quick_sort_1_way(a, 0, 6)
        print(a)
    elif category == 2:
        print(quick_sort_2_way(a))
    elif category == 3:
        quick_sort_3_way(a, 0, 6)
        print(a)
    elif category == 4:
        quick_sort_1_way_in_1(a, 0, 6)
        print(a)
