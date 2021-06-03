class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s = s.replace(' ', '')
        
        cal = ["+", "-", "*", "/"]
        
        # split the equation
        stack = []
        splited = []
        for it in s:
            if it in cal:
                splited.append(stack[:])
                splited.append([it])
                stack = []
            else:
                stack.append(it)
        
        splited.append(stack[:])
        
        # strings to num
        for i in range(len(splited)):
            if not splited[i][0] in cal:
                splited[i] = [self.s2n(splited[i])]
        
        
        # calculate "*" and "/"
        while True:
            isE = self.is_el1(splited)
            if isE == -1:
                break
            else:
                numL = splited[isE-1][0]
                numR = splited[isE+1][0]
                
                if splited[isE][0] == "*":
                    splited = splited[:isE-1]+[[numL*numR]]+splited[isE+2:] # truncate the list
                else:
                    splited = splited[:isE-1]+[[numL//numR]]+splited[isE+2:] # truncate the list
        
        # calculate "+" and "-"
        while True:
            isE = self.is_el2(splited)
            if isE == -1:
                break
            else:
                numL = splited[isE-1][0]
                numR = splited[isE+1][0]
                
                if splited[isE][0] == "+":
                    splited = splited[:isE-1]+[[numL+numR]]+splited[isE+2:] # truncate the list
                else:
                    splited = splited[:isE-1]+[[numL-numR]]+splited[isE+2:] # truncate the list
           
        return splited[0][0]
        
    # string to number
    def s2n(self, st):
        res = 0
        st = st[::-1]
        for i in range(len(st)):
            num = ord(st[i]) - ord('0')
            res += num*pow(10, i)
        return res
    
    # is "*", "/" elimated?
    def is_el1(self, sp):
        cal = ["*", "/"]
        for i in range(len(sp)):
            if sp[i][0] in cal:
                return i
        return -1
    
    # is "+", "-" elimated?
    def is_el2(self, sp):
        cal = ["+", "-"]
        for i in range(len(sp)):
            if sp[i][0] in cal:
                return i
        return -1
    