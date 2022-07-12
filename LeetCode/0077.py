class Solution:
    '''
    Backtrack. At each level, possible candidates are [lastNum+1, n]. 
    Time complexity: O((# of ans) * k), Space complexity: O((# of ans) * k). 
    '''
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        curAns = [0] * k

        def backtrack(ansLen, lastNum):
            if ansLen == k:
                ans.append(curAns[:])
                return

            for candidate in range(lastNum+1, n+1):
                curAns[ansLen] = candidate
                backtrack(ansLen+1, candidate)
        
        backtrack(0, 0)
        return ans