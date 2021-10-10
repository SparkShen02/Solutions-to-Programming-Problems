class Solution:
    '''
    Given an sorted array nums, find all unique [nums[i], nums[j]] that adds up to target. 
    Use two pointers, one moves forward from the beginning and the other moves backward from the end, to point to the two numbers being added. 
    Time complexity: O(n), Space complexity: O(1). 
    '''
    def twoSum(self, nums, target):
        start = 0
        end = len(nums) - 1
        ans = []
        while start < end:
            if nums[start] + nums[end] == target:
                ans.append([nums[start], nums[end]])
                
                while start + 1 < len(nums) and nums[start] == nums[start+1]: # skip duplicates
                    start += 1
                while end - 1 > -1 and nums[end] == nums[end-1]: # skip duplicates
                    end -= 1
                
                start += 1
                end -= 1
            elif nums[start] + nums[end] < target:
                start += 1
            elif nums[start] + nums[end] > target:
                end -= 1
        return ans

    '''
    Sort nums. 
    Then, for each number (with index i) in nums, find the corresponding twoSum with nums[i+1:].
    Time complexity: O(n^2), Space complexity: O(log(n)). 
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # O(nlog(n))
        ans = []
        i = 0
        while i < len(nums): # O(n^2)
            for subAns in self.twoSum(nums[i+1:], -nums[i]):
                ans.append([nums[i]] + subAns)
            while i + 1 < len(nums) and nums[i] == nums[i+1]: # skip duplicates
                i += 1
            i += 1
        return ans