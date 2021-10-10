from heapq import *
class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """
    def medianII(self, nums):
        left_heap = [] # max heap
        right_heap = [] # min heap
        res = []
        left = True
    
        for num in nums:
            if left:
                minRight = heappop(right_heap) if right_heap else 1000
                if num > minRight:
                    med = -heappushpop(left_heap, -minRight)
                    heappush(left_heap, -med)
                    heappush(right_heap, num)
                    res.append(med)
                else:
                    heappush(right_heap, minRight)
                    med = -heappushpop(left_heap, -num)
                    heappush(left_heap, -med)
                    res.append(med)
                left = False
            else:
                maxLeft = -heappop(left_heap)
                if num < maxLeft:
                    heappush(right_heap, maxLeft)
                    med = -heappushpop(left_heap, -num)
                    heappush(left_heap, -med)
                    res.append(med)
                else:
                    med = -heappushpop(left_heap, -maxLeft)
                    heappush(right_heap, num)
                    heappush(left_heap, -med)
                    res.append(med)
                left = True
    
        return res
