class Solution:
    '''
    Convert nums[num-1] to negative if num appears in the array. 
    Time complexity: O(n), Space complexity: O(n) (the resulting array). 
    '''
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            num = abs(num)
            nums[num-1] = -abs(nums[num-1])

        ans = []
        for num in range(1, len(nums)+1):
            if nums[num-1] > 0:
                ans.append(num)
        return ans