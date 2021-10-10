class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(cur, curSum, start):
            if curSum > self.target:
                return
            if curSum == self.target:
                ans.append(cur)
                return
            for i in range(start, len(candidates)):
                num = candidates[i]
                backtrack(cur+[num], curSum+num, i)

        self.target = target
        ans = []
        backtrack([], 0, 0)
        return ans