class Solution:
    '''
    At a char, # of deletions required = # of B in front + # of A after. 
    Count # of A after before the start. Then, traverse each character. 
    Time complexity: O(n), Space complexity: O(1). 
    '''
    def minimumDeletions(self, s: str) -> int:
        a_after = s.count('a')
        b_front = 0
        ans = a_after
        for ch in s:
            if ch == 'a':
                a_after -= 1
            ans = min(ans, a_after + b_front)
            if ch == 'b':
                b_front += 1
        return ans