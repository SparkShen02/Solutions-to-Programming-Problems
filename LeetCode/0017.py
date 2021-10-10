class Solution:
    '''
    Backtrack.
    Time complexity: O(3^n * n), Space complexity: O(3^n * n). 
    '''
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        n = len(digits)
        if n == 0:
            return ans
            
        letters = [0, 0, "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        def backtrack(i, cur):
            if i == n:
                ans.append(cur)
                return
            for letter in letters[int(digits[i])]:
                backtrack(i+1, cur+letter)

        backtrack(0, "")
        return ans