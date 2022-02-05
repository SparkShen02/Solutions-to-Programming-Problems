class Solution:
    '''
    The number at row i, col j = the number at row i-1, col j-1 + the number at row i-1, col j. 
    Time complexity: O(n^2), Space complexity: O(n^2) where n = numRows. 
    '''
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[-1]*(i+1) for i in range(numRows)]
        for i in range(numRows):
            n = i + 1
            for j in range(n):
                if j == 0 or j == n-1:
                    ans[i][j] = 1
                else:
                    ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
        return ans
