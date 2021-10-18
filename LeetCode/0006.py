class Solution:
    '''
    Use a list to store the string at each row. 
    Traverse s, the row number of each character follows the pattern: 1, 2, ..., numRows, numRows-1, ..., 1, 2, ..., numRows, numRows-1, ...
    Time complexity: O(n), Space complexity: O(n). 
    '''
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        stringAtRow = [""] * (numRows+1)
        curRow = 1
        increasing = False
        for ch in s:
            stringAtRow[curRow] += ch
            if curRow == numRows or curRow == 1:
                increasing = not increasing
            curRow = curRow + 1 if increasing else curRow - 1
        
        ans = ""
        for i in range(1, numRows+1):
            ans += stringAtRow[i]
        return ans