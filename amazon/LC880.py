class Solution(object):
    def decodeAtIndex(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        size = 0
        for it in s:
            if it.isalpha(): size+=1
            if it.isdigit(): size*=int(it)
        
        for c in reversed(s):
            k %= size
            if k==0 and c.isalpha(): return c
            if c.isdigit():
                size/=int(c)
            else:
                size-=1