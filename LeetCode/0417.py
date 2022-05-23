class Solution:
    '''
    Run depth-first search from every border cell. 
    Time complexity: O(mn), Space complexity: O(mn). 
    '''
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        numR, numC = len(heights), len(heights[0])
        s = []
        res = []

        # Reverse-explore from the pacific ocean
        s = [(r, 0) for r in range(numR)] + [(0, c) for c in range(1, numC)]
        pacificReachable = set()
        while len(s) != 0:
            r, c = s.pop()
            if (r, c) in pacificReachable:
                continue
            pacificReachable.add((r, c))
            h = heights[r][c]
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nr, nc = r+dr, c+dc
                if 0 <= nr < numR and 0 <= nc < numC:
                    if heights[nr][nc] >= h:
                        s.append((nr, nc))
        if len(pacificReachable) == 0:
            return []

        # Reverse-explore from the atlantic ocean
        s = [(r, numC-1) for r in range(numR)] + [(numR-1, c) for c in range(numC-1)]
        atlanticReachable = set()
        while len(s) != 0:
            r, c = s.pop()
            if (r, c) in atlanticReachable:
                continue
            atlanticReachable.add((r, c))
            if (r, c) in pacificReachable:
                res.append([r, c])
            h = heights[r][c]
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nr, nc = r+dr, c+dc
                if 0 <= nr < numR and 0 <= nc < numC:
                    if heights[nr][nc] >= h:
                        s.append((nr, nc))
        return res
