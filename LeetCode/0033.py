class Solution:
    '''
    Binary search. 
    If nums[i] < nums[len(nums)-1], then min is at the left of i; if nums[i] > nums[len(nums)-1], then min is at the right of i. 
    Time complexity: O(log(n)), Space complexity: O(1). 
    '''
    def findMinIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        left, right = 0, len(nums)-1
        last = nums[right]
        while left <= right:
            mid = left + (right-left) // 2
            if mid == 0:
                if nums[mid] < last:
                    return 0
                elif nums[mid] > last:
                    left = mid + 1
            else:
                if nums[mid-1] > nums[mid]:
                    return mid
                elif nums[mid] < last:
                    right = mid - 1
                elif nums[mid] > last:
                    left = mid + 1

    '''
    Use binary search to find the index of the minimum element of the rotated sorted array. 
    Suppose the min is at k, apply binary search on the imagined sorted array from nums[k] to nums[len(nums)+k-1].
    Time complexity: O(log(n)), Space complexity: O(1). 
    '''
    def search(self, nums: List[int], target: int) -> bool:
        k = self.findMinIndex(nums)
        left, right = k, len(nums) + k - 1
        while left <= right:
            mid = left + (right-left) // 2
            arrMid = mid % len(nums)
            if nums[arrMid] == target:
                return arrMid
            elif nums[arrMid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1