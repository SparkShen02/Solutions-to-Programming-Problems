class Solution:
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """
    def __init__(self):
        self.cache={}
    def isInterleave(self, s1, s2, s3):
        if (s1,s2,s3) in self.cache:
            return self.cache[(s1,s2,s3)]
        
        if len(s1)+len(s2)!=len(s3):
            return False
        
        if len(s1)==0 or len(s2)==0:
            if s1==s3 or s2==s3:
                return True
            return False

        if s3[0]==s1[0] and s3[0]==s2[0]: 
            result = self.isInterleave(s1, s2[1:], s3[1:]) or self.isInterleave(s1[1:], s2, s3[1:])
            self.cache[(s1,s2,s3)]=result
            return result
            
        if s3[0]==s1[0]:
            result = self.isInterleave(s1[1:], s2, s3[1:])
            self.cache[(s1,s2,s3)]=result
            return result
            
        if s3[0]==s2[0]:
            result = self.isInterleave(s1, s2[1:], s3[1:])
            self.cache[(s1,s2,s3)]=result
            return result
    
        return False