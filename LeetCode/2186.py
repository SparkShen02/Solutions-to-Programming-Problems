class Solution:
    '''
    For each letter, calculate the difference in the number of occurrences of the letter in the two strings. 
    Time complexity: O(n), Space complexity: O(n). 
    '''
    def minSteps(self, s: str, t: str) -> int:
        d = {ch: 0 for ch in "abcdefghijklmnopqrstuvwxyz"}
        for ch in s:
            d[ch] += 1
        for ch in t:
            d[ch] -= 1
        
        ans = 0
        for val in d.values():
            ans += abs(val)
        return ans