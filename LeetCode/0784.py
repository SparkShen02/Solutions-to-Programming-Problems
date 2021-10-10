class Solution:
    '''
    Backtrack. Each time advances one character. 
    Time complexity: O(2^n * n), Space complexity: O(2^n * n).
    '''
    def letterCasePermutation(self, S: str) -> List[str]:
        ans = []

        def backtrack(cur):
            if len(cur) == len(S):
                ans.append(cur)
                return
            
            nextCh = S[len(cur)]
            if nextCh.isdigit():
                backtrack(cur+nextCh)
            else:
                backtrack(cur+nextCh.upper())
                backtrack(cur+nextCh.lower())

        backtrack("")
        return ans