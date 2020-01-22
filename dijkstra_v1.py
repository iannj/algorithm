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

route_tables = {}
full_route_tables = []
# 首节点origin_node
origin_node = A

# 启动环节变量
# 转接节点transit_node
transit_node = origin_node

# 当前寻址路径pre_path
pre_path = [A]
# 当前寻址路径权值
pre_weight = 0

# 已遍历节点集合S
S = [transit_node]

# 未便利节点集合U
U = list(G.keys())
U.remove(transit_node)

# 开始处理
# 此版本假设G为全连通图
# 下个版本优化非全连通图
final_node = False

while not final_node:
    final_node = True
    # 获取当前节点邻接关系
    transit_neighbours = G.get(transit_node)
    if transit_neighbours is not None:
        # 本轮有效邻居中权值最短的节点round_short
        round_short = []
        for k, v in transit_neighbours.items():
            # 后继节点不应当在前置路由表中，避免路由成环
            if k not in pre_path:
                # 路由表：源节点，目的节点，路由，路由权值
                route_item_key = origin_node + '-' + k
                route_item_wight = pre_weight + v
                route_item = {route_item_key: [origin_node, k, '-'.join(pre_path) + '-' + k, route_item_wight]}
                full_route_tables.append(route_item)
                # print(route_item)
                # 本轮最短节点,没有最短节点时置最短节点，有则置最小节点
                if len(round_short) == 0:
                    round_short = [k, v]
                elif round_short[1] > v:
                    round_short = [k, v]
                # 路由表条目,没有路由表条目则置路由表条目，有则比较后置权值较小的条目
                route_tables_item = route_tables.get(route_item_key)
                if route_tables_item is None:
                    route_tables[route_item_key] = route_item.get(route_item_key)
                elif route_tables_item[3] > route_item.get(route_item_key)[3]:
                    route_tables[route_item_key] = route_item.get(route_item_key)
                final_node = False

        # 当本轮有处理节点时更新后继节点
        if not final_node:
            transit_node = round_short[0]
            S.append(transit_node)
            U.remove(transit_node)
            pre_path.append(transit_node)
            pre_weight += round_short[1]

for k, v in route_tables.items():
    print(k, v)

print('----------')

for k in full_route_tables:
    print(k)
