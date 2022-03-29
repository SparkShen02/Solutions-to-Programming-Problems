class Solution:
    '''
    The time complexities for both string.split() and string.join() are O(n). 
    '''
    def truncateSentence(self, s: str, k: int) -> str:
        return ' '.join(s.split(' ')[:k])