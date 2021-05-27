# https://blog.csdn.net/fuxuemingzhu/article/details/90448531

class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)== 1:
            return s
        
        stack = []
        for i in s:
            if stack and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)