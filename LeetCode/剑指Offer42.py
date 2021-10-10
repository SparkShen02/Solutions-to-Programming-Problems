class Solution:
    '''
    f[i] = 最后一个数是nums[i]的子数组的和的最大值
    f[i] = max(nums[i], nums[i] + f[i-1])
    Time complexity: O(n), Space complexity: O(1). 
    '''
    def maxSubArray(self, nums: List[int]) -> int:
        f_i = nums[0]
        max_f_i = f_i
        for i in range(1, len(nums)):
            f_i = max(nums[i], nums[i] + f_i)
            if f_i > max_f_i:
                max_f_i = f_i
        return max_f_i