import math 
from heapq import *
# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    """
    @param graph: a list of Undirected graph node
    @param A: nodeA
    @param B: nodeB
    @return:  the length of the shortest path
    """
    def shortestPath(self, graph, start_vertex, end_vertex):
        dists = { node: math.inf for node in graph }
        dists[start_vertex] = 0
        lookUp = {}
        unvisited = []
        nodes = {}
    
        for node in graph:
            entry = [dists[node], node.label]
            lookUp[node] = entry
            nodes[node.label] = node
            heappush(unvisited, entry)
    
        while unvisited:
            # 找到没有visit过而且dist最小的
            heapify(unvisited)
            curDist, cur = heappop(unvisited)
            cur = nodes[cur]
            
            if cur == end_vertex:
                return dists[cur]
            
            for neighbor in cur.neighbors:
                # relax
                # 更新cur连接的点
                dist = dists[cur] + 1
                if dist < dists[neighbor]:
                    dists[neighbor] = dist
                    lookUp[neighbor][0] = dist
    
        return dists
