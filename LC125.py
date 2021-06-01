class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s)-1
        while l<r:
            if not ((s[l] >= 'a' and s[l] <= 'z') or (s[l] >= 'A' and s[l] <= 'Z') or (s[l] >= '0' and s[l]<='9')):
                l += 1
                continue
            if not ((s[r] >= 'a' and s[r] <= 'z') or (s[r] >= 'A' and s[r] <= 'Z') or (s[r] >= '0' and s[r]<='9')):
                r -= 1
                continue
            if not (s[l] == s[r] or (abs(ord(s[l]) - ord(s[r])) == abs(ord('A')-ord('a')) and ((s[l] >= 'a' and s[l] <= 'z') or (s[l] >= 'A' and s[l] <= 'Z')))):
                return False
            l += 1
            r -= 1
        return True