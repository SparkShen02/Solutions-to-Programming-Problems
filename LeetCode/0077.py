class Solution:
    '''
    Backtrack. At each level, possible candidates are [lastNum+1, n]. 
    Time complexity: O((# of ans) * k), Space complexity: O((# of ans) * k). 
    '''
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        curAns = [0] * k

        def backtrack(i):
            if i == k:
                ans.append(curAns[:])
                return

            if i == 0:
                lastNum = 0
            else:
                lastNum = curAns[i-1]
            for candidate in range(lastNum+1, n+1):
                curAns[i] = candidate
                backtrack(i+1)
        
        backtrack(0)
        return ans