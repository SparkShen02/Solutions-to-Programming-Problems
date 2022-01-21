class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        a, b = 0, 1
        for _ in range(2, n+1):
            temp = a + b
            a = b
            b = temp
        return b