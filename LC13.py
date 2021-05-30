class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # record the table
        tab1 = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        tab2 = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        
        res = 0
        i = 0
        while i < len(s):
            if i+1 < len(s) and s[i]+s[i+1] in tab2:
                res += tab2[s[i]+s[i+1]] 
                i += 2
            else:
                res += tab1[s[i]]
                i += 1

        return res
        