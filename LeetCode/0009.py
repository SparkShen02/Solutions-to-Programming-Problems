class Solution:
    '''
    Split the integer into a left half and a reversed right half. Then, compare the two parts. 
    For example, x = 1221, let left = 12 and reserveRight = 12; x = 12321, let left = 123 and right = 12. 
    Time complexity: O(log(n)) (length of the integer), Space complexity: O(1). 
    '''
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False
        if x == 0:
            return True

        lenX = int(math.log(x, 10)) + 1
        left, right = x, 0
        for _ in range(lenX//2):
            # Add the rightmost digit to right and erase it from left
            right = right * 10 + left % 10
            left = left // 10
        
        if lenX % 2 == 0:
            return left == right
        else:
            return (left//10) == right