class Solution:
    '''                                                                                                                                                                                                                                
    Always turn the smallest integer to its negation.
    To reduce the time complexity:
        (1) Traverse nums and record the occurrences of every integer in a dictionary;
        (2) Start from -100, turn each negative integer to its negation;
        (3) Now there're only non-negative integers. Repeatedly turn the smallest integer to its negation.
    Time complexity: O(n + 201) = O(n), Space complexity: O(201) = O(1).                                                                                                                                                                                  
    ''' 
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        freq = {num: 0 for num in range(-100, 101)}
        maxSum = 0
        for num in nums:
            freq[num] += 1
            maxSum += num

        for num in range(-100, 0):
            if freq[num] >= 1:
                n = min(freq[num], k)
                freq[-num] += n
                maxSum -= 2 * num * n
                k -= n
                if k == 0:
                    break

        if k % 2 == 0:
            return maxSum
        minInt = 0
        for num in range(0, 101):
            if freq[num] >= 1:
                minInt = num
                return maxSum - 2 * minInt