class Solution:
    startOfLongest = 0
    endOfLongest = 0

    '''
    Traverse s and find substrings of the form "a" and "aa". For each such substring, move leftward and rightward simultaneously to find the longest palindrome centered at the substring. 
    Time complexity: O(n^2), Space complexity: O(1). 
    '''
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s)):

            def expandPalindrome(start, end):
                while -1 < start and end < len(s) and s[start] == s[end]:
                    start -= 1
                    end += 1
                if (end-1) - (start+1) > self.endOfLongest - self.startOfLongest:
                    self.startOfLongest, self.endOfLongest = start+1, end-1

            # Check substring of the form "a"
            start, end = i-1, i+1
            expandPalindrome(start, end)
    
            # Check substring of the form "aa"
            if i + 1 < len(s) and s[i] == s[i+1]:
                start, end = i-1, i+2
                expandPalindrome(start, end)
            
        return s[self.startOfLongest : self.endOfLongest+1]