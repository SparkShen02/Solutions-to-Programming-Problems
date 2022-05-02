class Solution:
    '''
    Store the number of occurrences of each letter in a dictionary (hash table). 
    Repeatedly choose the largest possible letter to construct the answer string. 
    Time complexity: O(n), Space complexity: O(1). 
    '''
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        letters = "zyxwvutsrqponmlkjihgfedcba "

        freq = {ch: 0 for ch in letters}
        for ch in s:
            freq[ch] += 1

        ans = ""
        for i in range(len(letters)):
            ch = letters[i]
            repeatTimes = 0
            while freq[ch] > 0:
                if repeatTimes < repeatLimit:
                    ans += ch
                    freq[ch] -= 1
                    repeatTimes += 1
                else:
                    for j in range(i+1, len(letters)):
                        if freq[letters[j]] != 0:
                            break
                        if j == len(letters)-1:
                            return ans
                    nextCh = letters[j]
                    ans += nextCh
                    freq[nextCh] -= 1
                    repeatTimes = 0
        return ans