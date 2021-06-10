class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        aL, bL = [], []
        for i in a:
            aL.append(int(i))
        for j in b:
            bL.append(int(j))
        aL = aL[::-1]
        bL = bL[::-1]
   
        res = []
        
        acu = 0 # 进位
        for i in range(min(len(aL), len(bL))):
            if aL[i]+bL[i]+acu == 2:
                acu = 1
                res.append("0")
            elif aL[i]+bL[i]+acu == 3:
                acu = 1
                res.append("1")
            else:
                res.append(str(aL[i]+bL[i]+acu))
                acu = 0
        
        i += 1
        rest = bL if i == len(aL) else aL
        
        for j in range(i, len(rest)):
            if rest[j] + acu == 2:
                acu = 1
                res.append("0")
            elif rest[j]+acu == 3:
                acu = 1
                res.append("1")
            else:
                res.append(str(rest[j] + acu))
                acu = 0
                
        if acu == 1:
            res.append("1")
            
        return "".join(res[::-1])
            