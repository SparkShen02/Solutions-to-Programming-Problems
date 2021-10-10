class Solution:
    def DFS(self, grid, i, j):
        s = [(i, j)]
        while len(s) != 0:
            curI, curJ = s.pop()
            for disI, disJ in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nextI, nextJ = curI + disI, curJ + disJ
                if 0 <= nextI < self.numR and 0 <= nextJ < self.numC and grid[nextI][nextJ] == "1":
                    grid[nextI][nextJ] = "*" # mark it as visited
                    s.append((nextI, nextJ))

    '''
    Run a depth-first search for every "1". Treat it as an island, and mark every land that it connects to as visited. 
    Time complexity: O(n), Space complexity: O(n). 
    '''
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        self.numR, self.numC = len(grid), len(grid[0])
        for i in range(self.numR):
            for j in range(self.numC):
                if grid[i][j] == "1":
                    ans += 1
                    self.DFS(grid, i, j)
        return ans

