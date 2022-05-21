from random import randrange

class Solution:
    '''
    One element appears n times, and all other elements appear just once. 
    Repeatedly, randomly choose two numbers and compare them. 
    The probability that the two numbers are equal = (n/2n) * ((n-1)/(2n-1)) ≈ 1/4. So, we're expected to find the answer in about 4 trials. 
    Time complexity: big-O of random.randrange(), Space complexity: O(1). 
    '''
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)
        while True:
            x, y = randrange(n), randrange(n) # randomly get a number in the range [0, n-1]
            if x != y and nums[x] == nums[y]:
                return nums[x]