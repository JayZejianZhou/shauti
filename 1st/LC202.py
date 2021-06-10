class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = dict() # detect if there's a cycle
        while True:
            # get sum
            sumN = 0
            while not n==0:
                sumN += (n%10)**2
                n = n//10
            
            
            if sumN == 1: return True
            if (sumN in visited): 
                return False
            visited[sumN] = 1
            n = sumN