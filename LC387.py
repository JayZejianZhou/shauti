class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        data = collections.defaultdict(int)
        
        for it in s:
            data[it] += 1
        
        for i in range(len(s)):
            if data[s[i]] == 1:
                return i
        
        return -1