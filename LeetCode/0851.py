class Solution:
    '''
    First, build a tree from richer, such that each node is richer than its parent. 
    Second, calculate the answer of each node from the answers of its children. 
    Time complexity: O(# of nodes + # of edges), Space complexity: O(# of nodes + # of edges). 
    '''
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        node2Children = {node: [] for node in range(n)}
        for a, b in richer:
            node2Children[b].append(a)

        def calAnswer(node, answer):
            if answer[node] != None:
                return answer
            curAns = node
            for child in node2Children[node]:
                answer = calAnswer(child, answer)
                if quiet[answer[child]] < quiet[curAns]:
                    curAns = answer[child]
            answer[node] = curAns
            return answer
        answer = [None] * n
        for node in range(n):
            answer = calAnswer(node, answer)
        return answer
