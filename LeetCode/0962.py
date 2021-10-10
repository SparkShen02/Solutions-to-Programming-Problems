class Solution:
    '''
    Monotonous Stack. Traverse nums in order, find a strictly decreasing sequence starting at nums[0] (e.g., if nums = [6, 8, 2, 0, 1, 5], find 6 -> 2 -> 0]). Push the index of each num in this sequence to a stack s. The start of the longest ramp must come from one of the indexes in the stack.
    Traverse nums in the reverse order using i, if nums[i] >= nums[s.top()], then this is the longest ramp that starts at s.top().
    Time complexity: O(n), Space complexity: O(n). 
    '''
    def maxWidthRamp(self, nums: List[int]) -> int:
        prevNum = nums[0]
        s = [0]
        for i in range(1, len(nums)):
            if nums[i] < prevNum:
                s.append(i)
                prevNum = nums[i]
        
        ans = 0
        i = len(nums) - 1
        while len(s) != 0:
            if i == s[-1]:
                s.pop()
            elif nums[i] >= nums[s[-1]]:
                ans = max(ans, i-s[-1])
                s.pop()
            else:
                i -= 1
        return ans