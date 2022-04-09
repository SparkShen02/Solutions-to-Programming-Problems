from collections import defaultdict

class Solution:
    '''
    Repeatedly remove from the tree the leaf nodes (this operation won't affect the answer) until only 1 or 2 node(s) remain, and the remaining node(s) would be the root(s) of all MHT(s). 
    Use a dictionary to record the nodes that each node connects to (in a set/hash table):
        Use this dictionary to find the first round of leaf nodes. 
        Use this dictionary and the current round of leaf nodes to find the next found of leaf nodes. 
    Time complexity: O(n), Space complexity: O(n). 
    '''
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        neighbors = defaultdict(set)
        for a, b in edges:
            neighbors[a].add(b)
            neighbors[b].add(a)
        
        leafNodes = [node for node in range(0, n) if len(neighbors[node]) == 1]
        while len(neighbors) > 2:
            nextLeafNodes = []
            for leaf in leafNodes:
                leafNeighbor = neighbors.pop(leaf).pop()
                neighbors[leafNeighbor].remove(leaf)
                if len(neighbors[leafNeighbor]) == 1:
                    nextLeafNodes.append(leafNeighbor)
            leafNodes = nextLeafNodes
        return list(neighbors.keys())