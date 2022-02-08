class Solution:
    '''
    Dynamic programming. 
    dp[k][amt] = the # of combinations that make up amt using the first k coins
    dp[k][amt] = dp[k-1][amt] + dp[k-1][amt-curCoin]] + dp[k-1][amt-2*curCoin]] + ...
    Note that dp[k][amt-curCoin] = dp[k-1][amt-curCoin] + dp[k-1][amt-2*curCoin] ...
    So dp[k][amt] = dp[k-1][amt] + dp[k][amt-curCoin]
    Time complexity: O(len(coins)*amount), Space complexity: O(amount). 
    '''
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for amt in range(amount+1)]
        dp[0] = 1
        for curCoin in coins:
            for amt in range(curCoin, amount+1): # amt-curCoin >= 0
                dp[amt] = dp[amt] + dp[amt-curCoin]
        return dp[amount]