class Solution:
    '''
    Traverse temperatures in reverse order. Use a dict "closet" to record the position of the latest encounter with each temperature. At each position i, cloest[t] records the smallest position j, such that j > i and temperatures[j] = t. 
    Time complexity: O(n * 71), Space complexity: O(n + 71). 
    '''
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [math.inf] * len(temperatures)
        closet = {t: math.inf for t in range(30, 101)}

        for i in range(len(temperatures)-1, -1, -1):
            minPos = math.inf
            for t in range(temperatures[i]+1, 101):
                minPos = min(minPos, closet[t])
            ans[i] = minPos - i if minPos < math.inf else 0
            closet[temperatures[i]] = i

        return ans