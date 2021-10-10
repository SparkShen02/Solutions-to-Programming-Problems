class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """
    # dp[i][j] means LCS of A[0:i] and B[0:j]
    # dp[i][j] = dp[i-1][j-1]+1 if A[i] == B[j]
    # else: dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    def longestCommonSubsequence(self, A, B):
        if not A or not B:
            return 0
        
        dp = [[0 for j in range(len(B)+1)] for i in range(len(A)+1)]
        
        for i in range(1, len(A)+1):
            for j in range(1, len(B)+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1 
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                
        return dp[-1][-1]
