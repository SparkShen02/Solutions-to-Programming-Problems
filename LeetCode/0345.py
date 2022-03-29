class Solution:
    '''
    Use a stack to store the vowels. 
    Time complexity: O(n), Space complexity: O(n). 
    '''
    def reverseVowels(self, s: str) -> str:
        vowels = []
        for ch in s:
            if ch in "aeiouAEIOU":
                vowels.append(ch)
        
        ans = [] # to lower the time & space complexity of concatenating strings
        for ch in s:
            if ch in "aeiouAEIOU":
                ans.append(vowels.pop())
            else:
                ans.append(ch)
        return ''.join(ans)