class Solution:
    '''
    Backtrack. Each time advances one character. Store the # of open and closed parentheses in current string to determine the next character's possible candidates. 
    Time complexity: ..., Space complexity: O(n) (from recursion calls). 
    '''
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(cur, numO, numC):
            if numO + numC == n * 2:
                ans.append(cur)
                return
            
            if numO > numC:
                if numO == n:
                    # candidates = [')']
                    backtrack(cur+')', numO, numC+1)
                else:
                    # candidates = ['(', ')']
                    backtrack(cur+'(', numO+1, numC)
                    backtrack(cur+')', numO, numC+1)
            elif numO == numC:
                # candiates = ['(']
                backtrack(cur+'(', numO+1, numC)

        backtrack("", 0, 0)
        return ans
