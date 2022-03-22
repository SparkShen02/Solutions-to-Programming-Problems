class Solution:
    '''
    Long division:
        Calculate the integer part first and record the remainder
        Then, repeatedly if remainder != 0:
            If the remainder has appeared before: there exists a repeating part
            Use a hash table to record the remainder with the current index in the answer string
            Remainder *= 10
            Use the remainder to calculate the next digit of the fractional part
    Time complexity: O(10^4), Space complexity: O(10^4). 
    '''
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)

        negative = True if (numerator >> 31) ^ (denominator >> 31) else False
        numerator = abs(numerator)
        denominator = abs(denominator)

        quotient = numerator // denominator
        ans = str(quotient) + "."
        remainder = numerator - denominator * quotient

        remainderInd = {}
        curInd = len(ans)
        while remainder != 0:
            if remainder in remainderInd:
                ans = ans[:remainderInd[remainder]] + "(" + ans[remainderInd[remainder]:] + ")"
                break
            remainderInd[remainder] = curInd
            curInd += 1
            remainder *= 10

            quotient = remainder // denominator
            ans += str(quotient)
            remainder = remainder - denominator * quotient
            
        return "-" + ans if negative else ans