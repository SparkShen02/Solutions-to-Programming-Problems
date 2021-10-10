class Solution:
    '''
    Let dist[i][j] denotes the minimum path sum from top to the number at row i, column j. 
    dist[i][j] = triangle[i][j] + min(dist[i-1][j-1], dist[i-1][j]). 
    Since dist[j] is calculated using dist[j-1] and dist[j] from the previous row, we can reduce the space complexity to O(n) if we traverse j in the reverse order. 
    Let n be the number of rows in the triangle. Time complexity: O(n^2), Space complexity: O(n). 
    '''
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dist = [-1 for _ in range(len(triangle))]
        for i in range(0, len(triangle)):
            rowLen = i + 1
            for j in range(rowLen-1, -1, -1): 
                if i == 0:
                    dist[j] = triangle[i][j]
                elif j == 0:
                    dist[j] = triangle[i][j] + dist[j]
                elif j == rowLen - 1:
                    dist[j] = triangle[i][j] + dist[j-1]
                else:
                    dist[j] = triangle[i][j] + min(dist[j-1], dist[j])
        return min(dist)