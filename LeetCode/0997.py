class Solution:
    '''
    Use two dictionaries to respectively record the # of people that a particular person trusts and the # of people that trust this person. 
    Time complexity: O(n), Space complexity: O(n).
    '''
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustedByWho = {i: 0 for i in range(1, n+1)}
        trustWho = {i: 0 for i in range(1, n+1)}
        for a, b in trust:
            trustWho[a] += 1
            trustedByWho[b] += 1
        
        for i in range(1, n+1):
            if trustWho[i] == 0 and trustedByWho[i] == n-1:
                return i
        return -1