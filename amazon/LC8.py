class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        nm, pm = -pow(2,31), pow(2, 31)-1
        
        temp = "0"
        sign = 0
        flag_ds = False # if the digit starts
        for i in range(len(s)):
            if flag_ds and not (s[i] >= '0' and s[i] <= '9'): break 
            if s[i]==" ": continue            
            elif s[i] == "-" and sign == 0: 
                sign = -1
                flag_ds = True
            elif s[i] == "+" and sign == 0: 
                sign = 1
                flag_ds = True
            elif s[i] >= '0' and s[i] <= '9': 
                if sign == 0: sign = 1
                temp += s[i]
                flag_ds = True
            else: break
        
        number = int(temp) * sign
        res = min(number, pm)
        res = max(res, nm)
        
        return res
            
            