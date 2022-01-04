class Solution:
    '''
    dp[n] = the minimum possible height of the bookshelf after placing the first n books. 
    When placing the nth book, there are the following possibilities:
        (1) The nth book is placed alone on the lowest shelf;
        (2) The nth and (n-1)th books are placed on the lowest shelf; 
        (3) The nth, (n-1)th, and (n-2)th books are placed on the lowest shelf; 
        ... until no more book can be placed together on the lowest shelf. 
    So, dp[n] = min(dp[n-1] + ..., dp[n-2] + ..., dp[n-3] + ..., ...)
    Time complexity: O(n^2), Space complexity: O(n). 
    '''
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        dp = [math.inf] * (len(books)+1)
        dp[0] = 0
        dp[1] = books[0][1]
        for n in range(2, len(books)+1):
            height = 0
            freeWidth = shelfWidth
            for j in range(1, n+1): # j denotes the number of books that are placed on the lowest shelf
                height = max(height, books[n-j][1])
                freeWidth -= books[n-j][0]
                if freeWidth < 0:
                    break
                dp[n] = min(dp[n], dp[n-j] + height)
        return dp[-1]