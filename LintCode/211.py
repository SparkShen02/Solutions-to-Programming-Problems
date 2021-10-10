class Solution:
    """
    @param A: a string
    @param B: a string
    @return: a boolean
    """
    def Permutation(self, A, B):
        if len(A) != len(B):
            return False
            
        for ch in A:
            if A.count(ch) != B.count(ch):
                return False
        return True
