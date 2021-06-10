class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        if len(s) < k:
            return s
        
        while True:
            i, res = self.isKEALL(s, k)   
            if res:
                break
            else:
                s = s[:i] + s[i+k:]

        return s
        
        
    # is k equal in all s
    def isKEALL(self, s, k):
        for i in range(len(s)-k+1):
            if self.isKE(i, s, k):
                return i, False
        return -1, True
        
        
    # is k equal?
    def isKE(self, ind, s, k):
        char = s[ind]
        for i in range(k):
            if not char == s[ind+i]:
                return False
        
        return True