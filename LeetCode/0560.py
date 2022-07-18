class Solution:
    '''
    Build an array preSum, such that preSum[i] = nums[0] + nums[1] + ... + nums[i]. 
    Suppose the subarray nums[l], ..., nums[r] has a sum of k, then preSum[r] - preSum[l-1] = k, or preSum[l-1] = preSum[r] - k.
    So, the # of subarrays, ending at index r, whose sum equals to k = the # of l, 0 <= l <= r, such that preSum[l-1] = preSum[r] - k.
    The latter can be computed in O(1) time if we maintain a frequency dictionary for preSum. 
    Time complexity: O(n), Space complexity: O(n). 
    '''
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        preSumFreq = {}
        preSumFreq[0] = 1 # preSum[-1] = 0

        curSum = 0
        ans = 0
        for r in range(n):
            curSum += nums[r]
            ans += preSumFreq.get(curSum-k, 0)
            if curSum not in preSumFreq:
                preSumFreq[curSum] = 1
            else:    
                preSumFreq[curSum] += 1
        return ans