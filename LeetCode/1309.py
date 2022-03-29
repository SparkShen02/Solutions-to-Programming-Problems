class Solution:
    '''
    To convert '1', ..., '26' to the corresponding letters: chr(int(ch) + 96). 
    Time complexity: O(n), Space complexity: O(n). 
    '''
    def freqAlphabets(self, s: str) -> str:
        ans = [] # to lower the time & space complexity of concatenating strings
        i = 0
        while i < len(s):
            if i < len(s)-2 and s[i+2] == '#':
                ans.append(chr(int(s[i:i+2]) + 96))
                i += 3
            else:
                ans.append(chr(int(s[i]) + 96))
                i += 1
        return ''.join(ans)