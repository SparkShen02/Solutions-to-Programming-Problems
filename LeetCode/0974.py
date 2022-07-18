class Solution:
    '''
    Build an array preSum, such that preSum[i] = nums[0] + nums[1] + ... + nums[i]. 
    Then, build another array preSumMod, such that preSumMod[i] = preSum[i] % k. 
    Suppose the subarray nums[l], ..., nums[r] has a sum divisible by k, then (preSum[r]-preSum[l-1]) % k = 0. 
    We have:
              (preSum[r] - preSum[l-1]) % k = 0
        (preSumMod[r] - preSumMod[l-1]) % k = 0
                               preSumMod[r] = preSumMod[l-1] (0 <= preSumMod[i] <= k-1, and so -(k-1) <= preSumMod[r] - preSumMod[l-1]) <= k-1)
    So, the # of subarrays, ending at index r, that have a sum divisible by k = the # of l, 0 <= l <= r, such that preSumMod[l-1] = preSumMod[r]. 
    The latter can be computed in O(1) time if we maintain a frequency dictionary for preSum. 
    Time complexity: O(n), Space complexity: O(n). 
    '''
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        preSumModFreq = {}
        preSumModFreq[0] = 1 # preSum[-1] = 0

        curSum = 0
        ans = 0
        for r in range(n):
            curSum += nums[r]
            curMod = curSum % k
            ans += preSumModFreq.get(curMod, 0)
            if curMod not in preSumModFreq:
                preSumModFreq[curMod] = 1
            else:    
                preSumModFreq[curMod] += 1
        return ans