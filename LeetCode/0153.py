class Solution:
    '''
    Binary search. 
    If nums[i] < nums[len(nums)-1], then min is at the left of i; if nums[i] > nums[len(nums)-1], then min is at the right of i. 
    Time complexity: O(log(n)), Space complexity: O(1). 
    '''
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left, right = 0, len(nums)-1
        last = nums[right]
        while left <= right:
            mid = left + (right-left) // 2
            if mid == 0:
                if nums[mid] < last:
                    return nums[0]
                elif nums[mid] > last:
                    left = mid + 1
            else:
                if nums[mid-1] > nums[mid]:
                    return nums[mid]
                elif nums[mid] < last:
                    right = mid - 1
                elif nums[mid] > last:
                    left = mid + 1
