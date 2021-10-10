class Solution:
    '''
    Start at the top-right corner: move left if target < curNum (because the whole column can be omitted), and move down if target > curNum (because the whole row can be omitted). Repeat until reach the bound.
    Time complexity: O(m+n), Space complexity: O(1). Explanation: Think about the search path, its length can be at most m+n. 
    '''
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        numR, numC = len(matrix), len(matrix[0])
        curR, curC = 0, numC - 1
        while curR < numR and curC >= 0:
            curNum = matrix[curR][curC]
            if target == curNum:
                return True
            elif target < curNum:
                curC -= 1; # move left
            else:
                curR += 1; # move down
        return False