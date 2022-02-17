class Solution:
    '''
    Start before the last element, traverse the array backwards, and find the last '0' (because it specifies the end of a character). 
    Start after that element, traverse to the end of the array and stop before the last element. Count the number of '1' on the way.  
    If this number is even, then the last character must be one-bit; otherwise, the last character must be two-bit. 
    To further optimize, we can combine the two traversals into one backward traversal. 
    Time complexity: O(n), Space complexity: O(1). 
    '''
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        count = 0
        i = len(bits) - 2
        while i >= 0:
            if bits[i] == 0:
                break
            else:
                count += 1
            i -= 1
        return count % 2 == 0