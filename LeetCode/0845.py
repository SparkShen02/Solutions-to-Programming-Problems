class Solution:
    '''
    dp_as[i] = the length of the longest strictly ascending subarray that ends at i
    dp_des[i] = the length of the longest strictly descending subarray that starts at i
    dp_as[i] + dp_des[i] - 1 = the length of the longest mountain subarray whose peak is at i
    Time complexity: O(n), Space complexity: O(n). 
    '''
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        dp_as, dp_des = [-1 for i in range(n)], [-1 for i in range(n)]

        dp_as[0] = 1
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                dp_as[i] = dp_as[i-1] + 1
            else:
                dp_as[i] = 1
        
        dp_des[n-1] = 1
        for i in range(n-2, -1, -1):
            if arr[i] > arr[i+1]:
                dp_des[i] = dp_des[i+1] + 1
            else:
                dp_des[i] = 1
        
        ans = 0
        for i in range(1, n-1):
            if dp_as[i] == 1 or dp_des[i] == 1: # does not meet the condition of being a mountain array
                continue
            ans = max(ans, dp_as[i] + dp_des[i] - 1)
        
        return ans
