class Solution:
    '''
    The # of digits of an integer num = round down of log10(num) + 1.
    Time complexity: O(n), Space complexity: O(1). 
    '''
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            if int(math.log10(num) + 1) % 2 == 0:
                ans += 1
        return ans