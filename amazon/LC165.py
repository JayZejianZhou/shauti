class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1ls, v2ls = version1.split("."), version2.split(".")
        
        tempelate = ["0"]*max(len(v1ls), len(v2ls))
        v1t, v2t = tempelate, tempelate[:]
        
        for i in range(len(v1ls)): v1t[i] = v1ls[i]
        for i in range(len(v2ls)): v2t[i] = v2ls[i]
        
        for i in range(len(v1t)):
            if int(v1t[i]) > int(v2t[i]): return 1
            elif int(v1t[i]) < int(v2t[i]): return -1
        
        return 0
        
        