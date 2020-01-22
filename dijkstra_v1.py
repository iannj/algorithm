#!/usr/env/bin python3
# -*- codung=utf-8 -*-

# graph g
A, B, C, D, E, F = list('ABCDEF')

# 使用邻接表G表示到其相邻节点的权值
G = {A: {B: 1, C: 12},
     B: {A: 1, C: 9, D: 3},
     C: {A: 12, B: 9, D: 4, F: 5},
     D: {B: 3, C: 4, E: 15, F: 13},
     E: {D: 15, F: 4},
     F: {D: 13, E: 4, C: 5}
     }

# 首节点A
# 转接节点t
t = A
# 当前寻址路径p
p = []

# 已遍历节点集合S
S = []

# 未便利节点集合U
U = list(G.keys())

S.append(t)
U.remove(t)

print(S)
print(U)
while U != []:
    p.append(t)
    c = G.get(t)
    print(c)
    pass