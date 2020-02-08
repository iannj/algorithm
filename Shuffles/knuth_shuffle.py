# -*- coding=utf-8 -*-

"""
Knuth Shuffles Algorithm
---------------------------
公平的洗牌算法。公平是指，对于生成的排列，每一个元素都能独立等概率地出现在每一个位置。或者反过来，每一个位置都能独立等概率地放置每个元素。
"""

import random

D = [x for x in range(5)]
l = len(D) - 1

for i in range(l):
    x = random.randint(i, l)
    print(f"i= {i},l= {l},x= {x}")
    temp = D[i]
    D[i] = D[x]
    D[x] = temp
    print(D)
