class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.que = []
        self.size = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.que.append(val)
        if len(self.que) > self.size: 
            self.que.pop(0)
            return sum(self.que)/float(self.size)
        elif len(self.que) == self.size: return sum(self.que)/float(self.size)
        else: return sum(self.que)/float(len(self.que))
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)