class Solution:
    '''
    Every integer is in the range [1, len(nums)-1]. 
    Mark nums[n] as negative if n appears.
    Time complexity: O(n), Space complexity: O(1). 
    '''
    def findDuplicate(self, nums: List[int]) -> int:
        for n in nums:
            n = abs(n)
            if nums[n] < 0: # n already appeared
                return n
            nums[n] = -nums[n]