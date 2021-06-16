class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        s1, s2, s3 = list(s1), list(s2), list(s3)
        
        
        while s1 and s2:
            if s1[0] == s2[0] and s1[0] == s3[0]: 
                return self.isInterleave(s1[1:], s2, s3[1:]) or self.isInterleave(s1, s2[1:], s3[1:])
            
            elif s1[0] == s3[0]:
                s1.pop(0)
                s3.pop(0)
            elif s2[0] == s3[0]:
                s2.pop(0)
                s3.pop(0)
            else:
                return False
        
        if not s1 and not s2 and not s3: return True
        elif not s1: return s2 == s3
        elif not s2: return s1 == s3

