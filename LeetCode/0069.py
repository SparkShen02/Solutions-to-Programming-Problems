class Solution:
    '''
    Use binary search to find the first integer n (0 < n <= x) such that n**2 > x. 
    Time complexity: O(log(n)), Space complexity: O(1). 
    '''
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            if mid**2 > x and (mid-1)**2 <= x:
                return mid - 1
            elif mid**2 > x:
                right = mid - 1
            else:
                left = mid + 1