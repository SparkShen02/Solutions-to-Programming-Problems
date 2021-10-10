class Solution:
    '''
    Use a dictionary to store the number of times a character appears.
    Time complexity: O(n), Space complexity: O(1). 
    '''
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = { ch: 0 for ch in "abcdefghijklmnopqrstuvwxyz" }
        for ch in s:
            count[ch] += 1
        for ch in t:
            count[ch] -= 1
            if count[ch] < 0:
                return False
                
        for val in count.values():
            if val != 0:
                return False
        return True