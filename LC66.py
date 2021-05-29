class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        summ = 0
        digit = digits[::-1]
        res = []
        incr = 0    # 进位
        digit[0] = digit[0] + 1
        for i in digit:
            r = i
            if incr == 1:
                r = r + 1
                incr = 0
            
            if r == 10:
                incr = 1
                res.append(0)
            else:
                res.append(r)
        if incr == 1:
            res.append(1)
        
        return res[::-1]
            