class Solution:
    '''
    Dynamic programming. 
    dp[i][j] = LCS between text1[0:i] and text2[0:j]
    dp[i][j] = 1 + dp[i-1][j-1] if text1[i-1] == text2[j-1]; else max(dp[i][j-1], dp[i-1][j])
    Time complexity: O(n^2), Space complexity: O(n^2). 
    '''
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for i in range(len(text2)+1)] for j in range(len(text1)+1)]
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[-1][-1]