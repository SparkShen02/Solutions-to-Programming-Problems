class Solution:
    '''
    Treat the whole matrix as a sorted array, and apply binary search. 
    Time complexity: O(log(mn)), Space complexity: O(1). 
    '''
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        numR, numC = len(matrix), len(matrix[0])

        def convert(n):
            return n // numC, n % numC

        left, right = 0, numR * numC - 1
        while left <= right:
            mid = (left + right) // 2
            i, j = convert(mid)
            num = matrix[i][j]
            if target == num:
                return True
            elif target < num:
                right = mid - 1
            else:
                left = mid + 1

        return False