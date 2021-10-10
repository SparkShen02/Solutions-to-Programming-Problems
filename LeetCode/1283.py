class Solution:
    '''
    Binary search. 
    As the divisor gets smaller, the sum gets bigger.
    Time complexity: O(n * log(10^6)), Space complexity: O(1). 
    '''
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if self.calSum(nums, mid) <= threshold:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

    # Time Complexity: O(n), Space complexity: O(1). 
    def calSum(self, nums, divisor):
        ans = 0
        for num in nums:
            ans += math.ceil(num/divisor)
        return ans