class Solution:
    '''
    Want to put each (i, j) at (j, nRow-1-i). 
    Apply a diagonal flip, which puts each (i, j) at (j, i). Then, apply a horizontal flip, which puts each (j, i) at (j, nRow-1-i). 
    Time complexity: O(n) where n denotes the total number of elements in the matrix, Space complexity: O(1). 
    '''
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        nRow, nCol = len(matrix), len(matrix[0])

        # Diagonal flip
        for i in range(nRow):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Horizontal flip
        for i in range(nRow):
            for j in range(nCol//2):
                matrix[i][j], matrix[i][nCol-1-j] = matrix[i][nCol-1-j], matrix[i][j]
        
        return matrix