# -*- coding=utf-8 -*-
"""
Fisher-Yates Shuttle Algorithm
----------------------------------
  Fisher–Yates shuffle 算法由 Ronald Fisher 和 Frank Yates 于 1938 年提出，在 1964 年由 Richard Durstenfeld 改编为适用于电脑编程的版本。
  这个算法很牛逼却很好理解，通俗的解释就是：将最后 1 个数和前面任意 n-1 个数中的一个数进行交换，然后倒数第 2 个数和前面任意 n-2 个数中的一个数进行交换。
  :author: liujie.nj@gmail.com
  :change log:
    v0.1 This is the first version with python.
"""
import random
from random import randint

D = [x for x in range(100)]

target = []

while len(D) > 1:
    temp = D.pop(-1)
    i = random.randint(0, len(D) - 1)
    target.insert(0, D[i])
    D[i] = temp
    print(target)
target.insert(D[0], 0)
print(target)
