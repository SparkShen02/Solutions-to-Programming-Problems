class Solution:
    '''
    Method 1:
        Run breadth-first search, with all the 0s at level 0. 
        Time complexity: O(mn), Space complexity: O(mn). 

    Method 2:
        Dynamic programming. 
        dp[r][c]: for cell (r, c), distance of the nearest 0; 
        dp1[r][c]: for cell (r, c), distance of the nearest 0 that's at the upper-left of it; 
        dp2[r][c]: for cell (r, c), distance of the nearest 0 that's at the lower-right of it.
        dp3[r][c] ...
        dp4[r][c] ...
        dp1[r][c] = min(dp1[r-1][c], dp1[r][c-1]) + 1
        dp2[r][c] = min(dp1[r+1][c], dp1[r][c+1]) + 1
        dp3[r][c] ...
        dp4[r][c] ...
        dp[r][c] = min(dp1[r][c], dp2[r][c], dp3[r][c], dp4[r][c])
        If, instead of using 4 different dp lists for 4 directions, we maintain just 1 dp list, we only need to calculate dp1 values and then calculate dp2 values based on the dp1 values. This simplified version also covers all 0s in the 4 directions. 
        Time complexity: O(mn), Space complexity: O(1) (not counting the returned m*n list). 
    '''
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        numR, numC = len(mat), len(mat[0])
        dp = [[math.inf for c in range(numC)] for r in range(numR)]

        # Calculate dp1
        for r in range(numR):
            for c in range(numC):
                if mat[r][c] == 0:
                    dp[r][c] = 0
                    continue
                if 0 <= r-1 < numR:
                    dp[r][c] = dp[r-1][c]+1
                if 0 <= c-1 < numC:
                    dp[r][c] = min(dp[r][c], dp[r][c-1]+1)

        # Calculate dp2
        for r in range(numR-1, -1, -1):
            for c in range(numC-1, -1, -1):
                if dp[r][c] == 0:
                    continue
                if 0 <= r+1 < numR:
                    dp[r][c] = min(dp[r][c], dp[r+1][c]+1)
                if 0 <= c+1 < numC:
                    dp[r][c] = min(dp[r][c], dp[r][c+1]+1)
        
        return dp
