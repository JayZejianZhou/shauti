class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.sz = 1000
        self.data = [[] for i in range(self.sz)]
        

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        # is the key in current hashmap?
        flag_fnd = False
        for i in self.data[self.hash(key)]:
            if i[0] == key:        
                i[1] = value
                flag_fnd = True
        
        if not flag_fnd:
            self.data[self.hash(key)].append([key, value])
        
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        for i in self.data[self.hash(key)]:
            if i[0] == key:
                return i[1]
        return -1
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        for i in self.data[self.hash(key)]:
            if i[0] == key:
                i[1] = -1
        
    def hash(self, num):
        return num % self.sz   # hash function


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)