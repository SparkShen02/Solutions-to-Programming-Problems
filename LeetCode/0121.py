class Solution:
    '''
    f[i] = the max profit that can be achieved selling on day i
    f[i] = price[i] - min(price[:i]) if price[i] > min(price[:i])
    Time complexity: O(n), Space complexity: O(1). 
    '''
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_f_i = 0
        for i in range(len(prices)):
            if prices[i] <= min_price:
                min_price = prices[i]
            else:
                f_i = prices[i] - min_price
                if f_i > max_f_i:
                    max_f_i = f_i
        return max_f_i