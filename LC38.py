class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = []
        last = "1"
        
        if n==1: return "1"
        
        for i in range(2, n+1):
            # 转换
            ind = 0
            this = ""
            while ind<len(last):
                dup = self.find_same(last, ind)
                this = this+str(dup)+str(last[ind])
                ind += dup
            last = this
        
        return this
    
    # 找相同后多少个
    def find_same(self, s, ind):
        res = 0
        if ind+res==len(s)-1:   #最后一个
            return 1
        while ind<len(s)-1 and s[ind] == s[ind+1]:
            res += 1
            ind += 1
        return res+1