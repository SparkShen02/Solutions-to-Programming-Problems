class Solution:
    '''
    Repeatedly choose the biggest value (symbol) for num. 
    Time complexity: O(1), Space complexity: O(1). 
    '''
    def intToRoman(self, num: int) -> str:
        vals = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        syms = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]

        ans = ""
        for i in range(13):
            val = vals[i]
            if num >= val:
                rep = num // val
                ans += syms[i] * rep
                num -= val * rep
                if num == 0:
                    break
        return ans