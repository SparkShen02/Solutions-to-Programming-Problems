class Solution:
    '''
    For each number, find its divisors/factors. 
    Time complexity: O(n * sqrt(m)), Space complexity: O(1). 
    '''
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            sumFactor = 1 + num
            numFactor = 2
            bound = int(sqrt(num)) + 1
            for factor in range(2, bound):
                if num % factor == 0:
                    numFactor += 1
                    sumFactor += factor
                    if factor != num // factor:
                        numFactor += 1
                        sumFactor += num // factor
                    if numFactor > 4:
                        break
            if numFactor == 4:
                ans += sumFactor
        return ans