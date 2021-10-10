class Solution:
    '''
    Convert a domino [a, b] to an integer a*10+b such that a <= b. 
    Two dominos are equivalent if they are converted to the same integer. 
    Record each domino in an array of length 100 (from index 0 to 99). For example, a value of 3 at arr[68] means that 3 dominoes that are converted to 68 have been reached.
    Time complexity: O(n), Space complexity: O(1). 
    '''
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        ans = 0
        count = [0 for i in range(100)]
        for x, y in dominoes:
            if x <= y:
                num = x * 10 + y
            else:
                num = y * 10 + x
            ans += count[num]
            count[num] += 1
        return ans
        