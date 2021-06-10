class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        indL = 0
        indR = len(s)-1
        
        is_palindrome = lambda  x: x==x[::-1]
        strPart = lambda s, x: s[:x] + s[x + 1:]

        # corner case
        if indL == indR:
            return True
        
        while indL < indR:
            if s[indL] == s[indR]:
                pass
            elif is_palindrome(strPart(s, indL)):
                return True
            elif is_palindrome(strPart(s, indR)):
                return True
            else:
                return False
            indL += 1
            indR -= 1
            
        return True
            
        
        