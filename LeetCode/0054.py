class Solution:
    '''
    Recursion. 
    spiralOrder(rowTop, rowBot, colLeft, colRight) = [exterior elements of the matrix] + spiralOrder(rowTop+1, rowBot-1, colLeft+1, colRight-1)
    Time complexity: O(n), Space complexity: O(n) (the resulting list). 
    '''
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        self.ans = []

        def recur(rowTop, rowBot, colLeft, colRight):
            if rowTop > rowBot or colLeft > colRight:
                return
            if rowTop == rowBot:
                self.ans += matrix[rowTop][colLeft:colRight+1]
                return
            if colLeft == colRight:
                self.ans += [matrix[row][colLeft] for row in range(rowTop, rowBot+1)]
                return

            # Add the exterior elements of the matrix to self.ans
            for col in range(colLeft, colRight+1):
                self.ans.append(matrix[rowTop][col])
            for row in range(rowTop+1, rowBot+1):
                self.ans.append(matrix[row][colRight])
            for col in range(colRight-1, colLeft-1, -1):
                self.ans.append(matrix[rowBot][col])
            for row in range(rowBot-1, rowTop, -1):
                self.ans.append(matrix[row][colLeft])

            recur(rowTop+1, rowBot-1, colLeft+1, colRight-1)
        
        recur(0, len(matrix)-1, 0, len(matrix[0])-1)
        return self.ans