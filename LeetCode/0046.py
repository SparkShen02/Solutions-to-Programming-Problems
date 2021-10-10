class Solution:
    '''
    Backtrack. Start from the first number and advance one number at a time. At each level n, nums[n:] stores the numbers that have not been used (candidates). Store the number that is used at current level in nums[n] (i.e. nums[:n+1] represents current answer). 
    Introduction: in backtrack, the function explores all possible candidates and uses recursion (calls itself) to advance to the next level until it reaches an answer. Then, it comes back to a certain point and starts exploring and advancing again for the next answer. It works like a depth-first search. 
    Time complexity: O(n! * n), Space complexity: O(n! * n) (the resulting list). Explanation: there are n! resulting permutations. Each permutation needs to be copied to the resulting list, which requires n steps.  
    '''
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(n):
            if n == len(nums):
                ans.append(nums[:])
            for i in range(n, len(nums)):
                nums[i], nums[n] = nums[n], nums[i] # indicate that nums[i] is used at current level
                backtrack(n+1)
                nums[i], nums[n] = nums[n], nums[i] # restore

        ans = []
        backtrack(0)
        return ans