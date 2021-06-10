class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)== 1:
            return s
        
        flag_all = False
        while not flag_all:
            cur_len = len(s)
            for i in range(len(s)-1):
                if s[i] == s[i+1]:
                    s = s[:i] + s[i+2:]
                    break
            if i >= cur_len-2:
                flag_all = True
                
        return s
            