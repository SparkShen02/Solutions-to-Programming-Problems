class Solution:
    '''
    Use a dictionary (hash table) to store whether a number exists in nums.
    Then, for each num in nums, if it starts a sequence (num-1 not in the dictionary), find the length of the sequence. 
    Time complexity: O(n), Space complexity: O(n). 
    '''
    def longestConsecutive(self, nums: List[int]) -> int:
        inNums = {}
        for num in nums:
            inNums[num] = True
        
        maxLen = 0
        for num in nums:
            if num-1 not in inNums: # O(1)
                curLen = 0
                while num in inNums:
                    curLen += 1
                    num += 1
                maxLen = max(maxLen, curLen)
        return maxLen