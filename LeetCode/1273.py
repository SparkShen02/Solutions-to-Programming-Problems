class Solution:
    '''
    Recursion. The sum of node values of the tree rooted at node i = value[i] + the sum of node values of each of i's subtree. 
    Then, use depth first search to skip every subtree whose sum of node values is zero and count the answer. 
    Time complexity: O(n), Space complexity: O(n). 
    '''
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        children = {i: [] for i in range(nodes)}
        for i in range(nodes):
            if (parent[i] != -1):
                children[parent[i]].append(i)

        # Recursion
        def calculateSum(node):
            for child in children[node]:
                calculateSum(child)
                value[node] += value[child] # value[i] = the sum of node values of the tree rooted at node i
        calculateSum(0)

        # Use DFS to count the answer
        ans = 0
        s = [0]
        while len(s) != 0:
            node = s.pop()
            if value[node] == 0:
                continue
            ans += 1
            for child in children[node]:
                s.append(child)
        return ans