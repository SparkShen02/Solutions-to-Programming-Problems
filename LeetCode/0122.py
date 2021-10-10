class Solution:
    '''
    On day i, buy if prices[i] < prices[i+1]; sell if prices[i] >= prices[i+1]. 
    Time complexity: O(n), Space complexity: O(1). 
    '''
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        bought, buyPrice = False, None
        for i in range(len(prices)):
            if i == len(prices) - 1:
                if bought:
                    profit += prices[i] - buyPrice
                return profit

            if not bought:
                if prices[i] < prices[i+1]:
                    buyPrice = prices[i]
                    bought = True
            else:
                if prices[i] >= prices[i+1]:
                    profit += prices[i] - buyPrice
                    bought = False
