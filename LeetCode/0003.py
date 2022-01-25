class Solution:
    '''
    Use two pointers, one points to the start of current substring, and the other points just past the end of current substring. 
    Use a set (hash table) to store the characters that are in the current substring. Add a character to the set when the "end" pointer moves forward and remove a character from the set when the "start" pointer moves forward. 
    Time complexity: O(n), Space complexity: O(n).
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0 or n == 1:
            return n

        start, end = 0, 1
        occ = set(s[0])
        ans = 0
        while end < n:            
            while end < n and s[end] not in occ:
                occ.add(s[end])
                end += 1
            ans = max(ans, end-start)
            if end == n:
                return ans
            while True:
                occ.remove(s[start])
                start += 1
                if s[start-1] == s[end]:
                    break
