class Solution:
    '''
    Think of each operation as a rectangle with its upper-left corner located at (0, 0). 
    The overlapping rectangle of two such rectangles, one with width a & length b and the other with width A & length B = min(a, A) * min(b, B). 
    Similarly, the overlapping rectangle of all the rectangles = min width of all the rectangles * min length of all the rectangles. 
    Time complexity: O(n), Space complexity: O(1). 
    '''
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if len(ops) == 0:
            return m * n

        minA, minB = ops[0][0], ops[0][1]
        for a, b in ops:
            minA = min(minA, a)
            minB = min(minB, b)
        return minA * minB