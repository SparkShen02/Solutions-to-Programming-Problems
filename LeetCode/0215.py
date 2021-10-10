class Solution:
    '''
    Quickselect (similar to quicksort). 
    After a partition step, the position of the pivot element is its final position in the sorted array. We can compare this position with k to (1) get the answer; or (2) discard half of the array and continue to sort the other half. 
    Time complexity: O(n), Space complexity: O(log(n)) (from recursion calls). 
    '''
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(nums, 0, len(nums)-1, len(nums)-k)

    def quickSelect(self, nums, start, end, target):
        pivot = self.partition(nums, start, end)
        if target == pivot:
            return nums[pivot]
        elif target < pivot:
            return self.quickSelect(nums, start, pivot-1, target)
        else:
            return self.quickSelect(nums, pivot+1, end, target)

    # Time complexity: O(n), Space complexity: O(1). 
    def partition(self, nums, start, end):
        pivot = nums[end] # pick the last element as the pivot
        i = start # points just after the last element that is <= pivot
        for j in range(start, end):
            if nums[j] <= pivot:
                nums[i], nums[j] = nums[j], nums[i] # swap
                i += 1
        nums[i], nums[end] = nums[end], nums[i] # swap the pivot to the right position
        return i