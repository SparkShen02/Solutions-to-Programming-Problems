'''
Integer: '+' / '-' (optional) + at least one digit
Decimal number: '+' / '-' (optional) + (1) at least one digit + '.' + any number of digit                                                    or (2) '.' + at least one digit
Valid number: (1) an integer or an decimal number                                                                   or (2) an integer or an decimal number + 'E' / 'e' + an integer
Time complexity: O(n), Space complexity: O(n).
'''
class Solution:
    def isInteger(self, s):
        if s == "": 
            return False

        for i in range(0, len(s)):
            ch = s[i]
            if ch == '+' or ch == '-':
                if i != 0 or len(s) == 1: # '+' / '-' is not at the start or s only has '+' / '-'
                    return False
            elif ch not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                return False
        return True

    def isDecimal(self, s):
        if s.count('.') != 1:
            return False
        beforeDot, afterDot = s.split('.')
        
        hasNumBeforeDot = False
        for i in range(0, len(beforeDot)):
            ch = beforeDot[i]
            if ch == '+' or ch == '-':
                if i != 0:
                    return False
            elif ch not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                return False
            else:
                hasNumBeforeDot = True

        if not hasNumBeforeDot and len(afterDot) == 0:
            return False
        for ch in afterDot:
            if ch not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                return False
        return True

    def isNumber(self, s: str) -> bool:
        hasE = False
        whichE = ''
        for i in range(0, len(s)):
            if s[i] == 'E' or s[i] == 'e':
                if hasE: # multiple 'E's or 'e's
                    return False
                hasE = True
                whichE = s[i]

        if not hasE:
            return self.isInteger(s) or self.isDecimal(s)
        else:
            beforeE, afterE = s.split(whichE)
            return (self.isInteger(beforeE) or self.isDecimal(beforeE)) and self.isInteger(afterE)