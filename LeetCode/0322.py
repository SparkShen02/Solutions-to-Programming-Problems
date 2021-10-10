class Solution:
    '''
    f[s] = min # of coins that make up s
    f[s] = min(1 + f[s-c] for c in coins)
    Time complexity: O(S*C), Space complexity: O(S).
    '''
    def coinChange(self, coins: List[int], amount: int) -> int:
        f = [math.inf for s in range(amount+1)] # inf indicates that the amount cannot be made up
        f[0] = 0
        for s in range(1, amount+1):
            for c in coins:
                if s-c>= 0:
                    f[s] = min(f[s], 1 + f[s-c])
        return f[amount] if f[amount] != math.inf else -1