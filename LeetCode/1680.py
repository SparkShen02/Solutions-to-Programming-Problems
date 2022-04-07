class Solution:
    '''
    f[i] = the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order
    f[i] = f[i-1] * 2^(length of the binary representation of i) + i
    Based on the modulo rules (a + b) % n = ((a % n) + (b % n)) % n and (a * b) % x = ((a % x) * (b % x)) % x:
        f[i] % x = ((f[i-1] * 2^len) % x + i % x) % x = (( (f[i-1] % x) * (2^len % x) ) % x + i % x) % x = ((f[i-1] % x) * (2^len % x) + i) % x
    Based on the constraints in the problem:
        f[i] % x = ((f[i-1] % x) * 2^len + i) % x
    Time complexity: O(n), Space complexity: O(1). 
    '''
    def concatenatedBinary(self, n: int) -> int:
        mod = 10**9 + 7
        ans = 1 # f[i] % mod
        length = 1 # length of the binary representation of the current number
        nextDigit = 2 # length increments 1 when the current number is 2, 4, 8, ...
        for i in range(2, n+1):
            if i == nextDigit:
                length += 1
                nextDigit *= 2
            ans = ((ans << length) + i) % mod
        return ans