class Solution:
    '''
    Use two pointers, one points to the start of current substring, and the other points just past the end of current substring. 
    Use a set (hash table) to store the characters that are in the current substring. Remove a character from the set when the "start" pointer moves forward, and add a character to the set when the "end" pointer moves forward. 
    Time complexity: O(n), Space complexity: O(n).
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0 or n == 1:
            return n

        start, end = 0, 1
        occ = set(s[0])
        ans = 0
        while start < n and end < n:
            # Skip duplicates
            while start+1 < n and s[start] == s[start+1]:
                start += 1
                end += 1
            
            while end < n and s[end] not in occ:
                occ.add(s[end])
                end += 1

            ans = max(ans, end-start)
            occ.remove(s[start])
            start += 1
        return ans