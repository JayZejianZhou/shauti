class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        num = []
        while not x // 10 == 0:
            num.append(x%10)
            x = x//10
            
        num.append(x)
        if num == num[::-1]:
            return True
        else:
            return False
        