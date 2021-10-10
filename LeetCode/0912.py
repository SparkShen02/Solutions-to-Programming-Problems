class Solution:
    '''
    Heapsort. Why? Quicksort has a space complexity of O(log(n)) (from recursion calls) and mergesort has a space complexity of O(n) (from the auxiliary array used in merging). 
    Time complexity: O(n + n * log(n)) = O(nlogn), Space complexity: O(1). 
    '''
    def sortArray(self, nums: List[int]) -> List[int]:
        self.heapify(nums)
        heapLen = len(nums)
        while heapLen > 0:
            # Extract the biggest value from the max heap and put it in the right spot
            maxVal = self.extractMax(nums, heapLen)
            nums[heapLen-1] = maxVal
            heapLen -= 1
        return nums

    '''
    Extract the max element from a max heap. 
    Time complexity: O(log(n)), Space complexity: O(1). 
    '''
    def extractMax(self, nums, heapLen):
        maxVal = nums[0]
        nums[0] = nums[heapLen-1] # copy the right-most, bottom-most node to the root
        self.swapDown(nums, 0, heapLen-1)
        return maxVal

    '''
    Convert an array (list) into a max heap. 
    Time complexity: O(n), Space complexity: O(1). 
    '''
    def heapify(self, nums):
        start = len(nums) // 2 - 1
        for i in range(start, -1, -1):
            self.swapDown(nums, i, len(nums)) 

    # Repeatedly swap the element with the larger of its two children
    def swapDown(self, nums, i, heapLen):
        while True:
            left, right = 2 * i + 1, 2 * i + 2
            larger = None
            if left < heapLen and right < heapLen:
                if nums[left] > nums[i] or nums[right] > nums[i]:
                    larger = left if nums[left] > nums[right] else right
            elif left < heapLen and nums[left] > nums[i]:
                larger = left
            elif right < heapLen and nums[right] > nums[i]:
                larger = right
            
            if larger == None:
                break
            nums[i], nums[larger] = nums[larger], nums[i] # swap
            i = larger