class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cash = collections.defaultdict(int)
        self.cap = capacity
        self.order = [] # 记录各个key进来的oder，越后面越新
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # 要把用过的最新的放order最后面
        if key in self.order:
            self.order.remove(key)
            self.order =  self.order + [key]
        
        return self.cash[key]-1
        pass
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        
      
        
        
        if len(self.order) >= self.cap and not key in self.order:
            self.cash[self.order[0]] = 0
            self.order = self.order[1:]
            
        # 要把用过的最新的放order最后面
        if key in self.order:
            self.order.remove(key)
            self.order =  self.order + [key]  
        else:
            self.order.append(key)
            
        self.cash[key] = value+1
        
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)