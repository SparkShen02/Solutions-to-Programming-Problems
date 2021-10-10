class Solution:
    '''
    f[i][j] = minimum path sum from (0, 0) to (i, j)
    f[i][j] = min(f[i-1][j], f[i][j-1]) + grid[i][j]
    Time complexity: O(n), Space complexity: O(n). 
    '''
    def minPathSum(self, grid: List[List[int]]) -> int:
        nRow, nCol = len(grid), len(grid[0])

        f = [[-1]*nCol for _ in range(nRow)]
        f[0][0] = grid[0][0]

        for i in range(nRow):
            for j in range(nCol):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    f[i][j] = f[i][j-1]
                elif j == 0:
                    f[i][j] = f[i-1][j]
                else:
                    f[i][j] = min(f[i-1][j], f[i][j-1])
                f[i][j] += grid[i][j]

        return f[nRow-1][nCol-1]