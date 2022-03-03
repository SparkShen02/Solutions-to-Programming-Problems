class Solution:
    '''
    Let a0, a1, ..., an represent the digits in num. So, num = an * 10^n + ... + a1 * 10^1 + a0 * 10^0. 
    Given:
        For any i >= 0, 10^i % 9 = 1
        (A + B) % C = (A % C) + (B % C)
        (A * B) % C = (A % C * B % C) % C
    Then:
        num % 9 = (an * 10^n) % 9 + ... + (a1 * 10^1) % 9 + (a0 * 10^0) % 9
                = (an % 9) % 9 + ... + (a1 % 9) % 9 + (a0 % 9) % 9
                = an % 9 + ... + a1 % 9 + a0 % 9
                = (an + ... + a1 + a0) % 9
    Let num --(add all digits together)--> num1 --(add all digits together)--> ... --(add all digits together)--> numi, such that numi < 10. 
    num % 9 = num1 % 9 = ... = numi % 9
    Because 0 < numi < 10, numi = numi % 9 if numi % 9 != 0 else 9. 

    Time complexity: O(1), Space complexity: O(1). 
    '''
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        mod = num % 9
        return mod if mod != 0 else 9