class Solution:
    '''
    Sort intervals by the start number. Then traverse every pair of adjacent intervals and possibly merge them.
    Time complexity: O(nlog(n)), Space complexity: O(n).  
    '''
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() # with a time complexity of O(nlog(n)) and a space complexity of O(log(n)). 
        
        merged = [intervals[0]]
        for cur in intervals[1:]:
            # Compare current interval with the previous one
            prev = merged[-1]
            if cur[0] <= prev[1]:
                prev[1] = max(prev[1], cur[1])
            else:
                merged.append(cur)
        return merged