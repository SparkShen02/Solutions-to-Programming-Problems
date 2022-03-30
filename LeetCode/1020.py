class Solution:
    '''
    Run depth-first search from every boundary land cell. Any land cell reached along the way is not an enclave. 
    Time complexity: O(mn), Space complexity: O(mn).
    '''
    def numEnclaves(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        def dfs(r, c):
            if grid[r][c] == 0 or (r, c) in visited:
                return
            visited.add((r, c))
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r+dr, c+dc
                if (0 <= nr < numR and 0 <= nc < numC):
                    dfs(nr, nc)
        
        numR, numC = len(grid), len(grid[0])
        
        # Count land cells that are not enclaves
        visited = set()
        for r in range(numR):
            dfs(r, 0)
            dfs(r, numC-1)
        for c in range(numC):
            dfs(0, c)
            dfs(numR-1, c)

        # Count land cells
        cnt = 0
        for r in range(numR):
            for c in range(numC):
                if grid[r][c] == 1:
                    cnt += 1
        
        return cnt - len(visited)