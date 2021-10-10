class Solution:
    '''
    Let i points just after the processed sub-array. When reached a non-zero number, swap it with nums[i]. 
    Time complexity: O(n), Space complexity: O(1). 
    '''
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for n in range(len(nums)):
            if nums[n] != 0:
                nums[n], nums[i] = nums[i], nums[n]
                i += 1