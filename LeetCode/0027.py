class Solution:
    '''
    Swap each val to the back of array. 
    Time complexity: O(n), Space complexity: O(1). 
    '''
    def removeElement(self, nums: List[int], val: int) -> int:
        pos = len(nums) - 1 # the position before the swapped vals
        i = 0
        while i <= pos:
            if nums[i] == val:
                nums[i], nums[pos] = nums[pos], nums[i]
                pos -= 1
            else:
                i += 1
        return i