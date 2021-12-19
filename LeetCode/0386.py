class Solution:
    '''
    Imagine a prefix tree (trie) that represents all the numbers. 
    Run a depth-first search on this trie and stop exploring a branch when the number reached exceeds n. 
    Time complexity: O(n), Space complexity: O(n). 
    '''
    def lexicalOrder(self, n: int) -> List[int]:
        if n <= 9:
            return [i for i in range(1, n+1)]

        ans = []
        toVisit = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        while len(toVisit) != 0:
            num = toVisit.pop()
            ans.append(num)
            for nextNode in range(9, -1, -1):
                nextNum = num * 10 + nextNode
                if nextNum > n:
                    continue
                else:
                    toVisit.append(nextNum)
        return ans