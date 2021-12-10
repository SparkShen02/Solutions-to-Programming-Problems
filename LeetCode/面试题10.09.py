class Solution:
    '''
    For an element in the matrix, the elements to its left are <= than it and the elements below it are >= than it. 
    Start from the top-right element, and then gradually approach the target element. After each move, an entire row or column can be excluded from our search. 
    Time complexity: O(m+n), Space complexity: o(1). 
    '''
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        def inbound(r, c):
            return r < len(matrix) and c >= 0

        row, col = 0, len(matrix[0])-1
        while inbound(row, col):
            if target < matrix[row][col]:
                col -= 1
            elif target > matrix[row][col]:
                row += 1
            else:
                return True
        return False