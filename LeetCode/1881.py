class Solution:
    '''
    If n represents a positive number, traverse n from left to right, and then insert x to the left of the first number that is < x. 
    If n represents a negative number, traverse n from left to right, and then insert x to the left of the first number that is > x. 
    Time complexity: O(n), Space complexity: O(n) (the resulting answer). 
    '''
    def maxValue(self, n: str, x: int) -> str:
        if n[0] != '-':
            for i in range(len(n)):
                if int(n[i]) < x:
                    return n[:i] + str(x) + n[i:]
            return n + str(x)
        else:
            for i in range(1, len(n)):
                if int(n[i]) > x:
                    return n[:i] + str(x) + n[i:]
            return n + str(x)