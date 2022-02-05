class Solution:
    '''
    In order to merge the arrays in-place, repeatedly compare the numbers at the end of the two arrays and place the larger one to the end (extra space) of nums1. 
    Time complexity: O(n), Space complexity: O(1). 
    '''
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m - 1, n - 1
        beforeMerged = m + n - 1 # points before the merged array
        while p1 >= 0 and p2 >= 0:
            num1, num2 = nums1[p1], nums2[p2]
            if num1 > num2:
                nums1[beforeMerged] = num1
                p1 -= 1
            else:
                nums1[beforeMerged] = num2
                p2 -= 1
            beforeMerged -= 1
        for i in range(p2, -1, -1): # merge the remaining numbers in nums2
            nums1[beforeMerged] = nums2[p2]
            p2 -= 1
            beforeMerged -= 1
        return nums1
