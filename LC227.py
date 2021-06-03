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
        
        # solve it
        stack = []
        cur_operate = 0
        iF = 0
        while True:
            if iF >= len(splited):
                break
            elif not splited[iF][0] in cal:
                stack.append(splited[iF][0])
            elif splited[iF][0] == "-":
                iF += 1
                stack.append(0 - splited[iF][0])   
            elif splited[iF][0] == "*":
                lastNum = stack.pop()  
                iF += 1
                stack.append(splited[iF][0] * lastNum)                
            elif splited[iF][0] == "/":
                lastNum = stack.pop()  
                iF += 1
                if lastNum<0:
                    stack.append(-(abs(lastNum) // splited[iF][0]))
                else:
                    stack.append(lastNum // splited[iF][0])
                    
            iF += 1
        
        sumT = sum(stack)
            
        return sumT
                
        
        
    
    # string to number
    def s2n(self, st):
        res = 0
        st = st[::-1]
        for i in range(len(st)):
            num = ord(st[i]) - ord('0')
            res += num*pow(10, i)
        return res