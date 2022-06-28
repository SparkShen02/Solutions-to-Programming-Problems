from math import gcd

class Solution:
    '''
    Brute force. List every possible fraction and find the greatest common divisor –– the largest number that divides both the numerator and the denominator. 
    Time complexity: O(n^2log(n)) (the big-O of finding GCD using Euclid's Algorithm is log(n)), Space complexity: O(1) (not considering the answer list). 
    '''
    def simplifiedFractions(self, n: int) -> List[str]:
        ans = []
        for deno in range(1, n+1):
            for nume in range(1, deno):
                if gcd(deno, nume) == 1:
                    ans.append(str(nume) + '/' + str(deno))
        return ans
