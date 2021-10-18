class Solution:
    '''
    For the letter 'a', if there are 3 'a's in t and 2 'a's in s, then 1 of the 'a's in t needs to be replaced. 
    Apply the same logic to every letter. 
    Time complexity: O(n), Space complexity: O(1). 
    '''
    def minSteps(self, s: str, t: str) -> int:
        countS = {ch: 0 for ch in "abcdefghijklmnopqrstuvwxyz"}
        countT = {ch: 0 for ch in "abcdefghijklmnopqrstuvwxyz"}
        for ch in s:
            countS[ch] += 1
        for ch in t:
            countT[ch] += 1
        
        ans = 0
        for ch in "abcdefghijklmnopqrstuvwxyz":
            if countT[ch] > countS[ch]:
                ans += countT[ch] - countS[ch]
        return ans