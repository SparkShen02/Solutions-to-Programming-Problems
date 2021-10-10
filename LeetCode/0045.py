class Solution:
    '''
    Repeatedly calculate the max index that can be reached after the ith jump. 
    Time complexity: O(n), Space complexity: O(1).    
    '''
    def jump(self, nums: List[int]) -> int:            
        curIndex = 0
        i = 0
        maxReachableIndex = 0
        while maxReachableIndex < len(nums)-1:
            i += 1
            temp = maxReachableIndex
            
            # Calculate the maxReachableIndex after the ith jump
            for index in range(curIndex, temp+1):
                maxReachableIndex = max(maxReachableIndex, index+nums[index])
            
            curIndex = temp + 1
        return i