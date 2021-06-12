class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        tmin = -pow(2, 31)
        tmax = pow(2, 31) -1
        
        res = 0
        sign = 1

        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0): sign = -1
        dividend, divisor = abs(dividend), abs(divisor)
        rem = dividend
        while rem >= divisor:
            n = 0
            while divisor << n <= rem: n += 1        
            res += pow(2, n-1)        
            rem = rem - (divisor<<(n-1))
            
            
        
        res = max(min(res*sign, tmax), tmin)
        
        return res
        
        
        