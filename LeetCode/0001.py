class Solution:
    '''
    Iterate through nums and construct a dictionary that stores a number as the key and the index to that number as the value. This can be used to check if a certain number exists in nums and if so, what its index is. 
    Time complexity: O(n), Space complexity: O(n). 
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToInd = {}
        for i in range(0, len(nums)):
            numToInd[nums[i]] = i
        
        for i in range(0, len(nums)):
            targetNum = target - nums[i]
            if numToInd.get(targetNum) != None and i != numToInd[targetNum]:
                return [i, numToInd[targetNum]]