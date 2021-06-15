class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10: return n
        # 定区间，肯定小于10^10
        n -= 10
        i = 2
        
        while i < 10:
            if n - i*9*pow(10,i-1) < 0:
                break
            else: n -= i*9*pow(10,i-1)
            i += 1
        
        div, rem = n//(i), n%(i)
        
        temp = pow(10, i-1) + div
                 
        return str(temp)[rem]
        