class Solution:
    '''
    Binary search. Insert at the index i such that nums[i-1] < target <= nums[i]. 
    Time complexity: O(log(n)), Space complexity: O(1).
    '''
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            prevNum, nextNum = nums[mid-1] if mid != 0 else -float('inf'), nums[mid]
            if prevNum < target <= nextNum:
                return mid
            elif target <= prevNum:
                r = mid - 1
            elif nextNum < target:
                l = mid + 1
        return len(nums)