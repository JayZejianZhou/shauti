class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        # 数字转26进制
        final = float('inf')
        res = []
        while columnNumber:
            res.append((columnNumber-1) % 26)
            columnNumber = (columnNumber-1) / 26
            
        res = res[::-1]
        real_res = ""
        # convert to char
        for i in res:
            real_res += chr(i+ord("A"))
            
        return real_res
            