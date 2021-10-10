class Solution:
    '''
    To fulfill the constant space requirement, utilize nums to record if a number exists. 
    To record that a number i exists, turn the number at index (i - 1) to negative. 
    largestPossibleAns = len(nums) + 1. First, iterate nums and turn all non-positive numbers to largestPossibleAns (so that they will be ignored). Then, iterate nums and record every number that is less than largestPossibleAns. Last, iterate nums to get the answer. 
    Time complexity: O(n), Space complexity: O(1). 
    '''
    def firstMissingPositive(self, nums: List[int]) -> int:
        largestPossibleAns = len(nums) + 1
        for i in range(0, len(nums)):
            if nums[i] <= 0:
                nums[i] = largestPossibleAns

        for i in range(0, len(nums)):
            curNum = nums[i]
            if curNum < 0:
                curNum = -curNum
            if 0 < curNum < largestPossibleAns:
                if nums[curNum-1] > 0: # haven't encountered
                    nums[curNum-1] = -1 * nums[curNum-1]

        for i in range(0, len(nums)):
            if nums[i] >= 0:
                return i+1
        return largestPossibleAns