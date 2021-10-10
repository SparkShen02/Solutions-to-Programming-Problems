class Solution:
    '''
    There are about log10(x) digits in x.
    Time complexity: O(log(n)), Space complexity: O(log(n)).
    '''
    def reverse(self, x: int) -> int:
        ans = int(str(x)[::-1]) if x >= 0 else -int(str(-x)[::-1])
        return 0 if ans < -1 * (2**31) or ans > (2**31) - 1 else ans
