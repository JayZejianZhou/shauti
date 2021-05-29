class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        res = 1.0
        if n == 0:
            return 1            
        if n < 0:
            x = 1.0 / x
            n = -n
            
        if n % 2 :
            return x * self.myPow(x, n-1)
                  
        return self.myPow(x * x, n//2)
        
        