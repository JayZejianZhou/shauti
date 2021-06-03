class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        temp = self.stack[-1]
        self.stack.pop()
        return temp

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]        
        

    def peekMax(self):
        """
        :rtype: int
        """
        maxT = float('-inf')
        maxI = 0
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i] > maxT:
                maxT = self.stack[i]
                maxI = i
        # self.stack = self.stack[:i] + self.stack[i+1:]    
        return maxT
        

    def popMax(self):
        """
        :rtype: int
        """
        maxT = float('-inf')
        maxI = 0
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i] > maxT:
                maxT = self.stack[i]
                maxI = i
        self.stack = self.stack[:maxI] + self.stack[maxI+1:]    
        return maxT
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()