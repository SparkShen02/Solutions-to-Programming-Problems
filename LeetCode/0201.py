class Solution:
    '''
    Algorithm 1:
    0 -> 0000
    1 -> 0001
    2 -> 0010
    3 -> 0011
    4 -> 0100
    5 -> 0101
    6 -> 0110
    7 -> 0111
    8 -> 1000
    For the i-th bit (starting from right) in the binary representation of a decimal number num, let mult be the smallest multiple of 2^i that is > num, then the bit is 1 iff num is in the range [mult - 2^(i-1), mult). 
    For the i-th bits of all numbers in the range [left, right], let mult be the smallest multiple of 2^i that is > right, then the bits are all 1 iff [left, right] is contained in [mult - 2^(i-1), mult). 
    Time complexity: O(1), Space complexity: O(1). 

    Algorithm 2: 
    Consider the binary representations of left and right, and suppose their first i bits (starting from left) are identical. Since 0 <= left <= right, the (i+1)-th bits of all the numbers in the range [left, right] must consist of 0s and then 1s. Thus, there must exist x and x+1 in that range, such that the bits after the i-th bit for x are 0111... and those for x+1 are 1000...
    Therefore, the bitwise AND of all numbers in the range [left, right] consists of the preceding i bits of left and right that are identical followed by all 0s. 
    Time complexity: O(1), Space complexity: O(1). 
    '''
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # Algorithm 1
        # ans = 0
        # for i in range(1, 33):
        #     temp = 2**i
        #     mult = (right - right % temp) + temp
        #     if mult - 2**(i-1) <= left and right < mult:
        #         # Current bit is 1 in ans
        #         ans = ans | 1 << (i-1)
        # return ans

        # Algorithm 2
        shift = 0
        while left != right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift