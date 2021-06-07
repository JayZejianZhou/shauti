# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.data = []
        for it in nestedList:
            self.helper(it)
        self.cur = -1    # the index of the current integer
        
    
    # go through the nest structures
    def helper(self, dat):
        if dat.isInteger(): 
            self.data.append(dat.getInteger())
            return 0
        else:
            listT = dat.getList()
            for it in listT:
                self.helper(it)
    
    def next(self):
        """
        :rtype: int
        """
        self.cur += 1
        return self.data[self.cur]

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.cur >= len(self.data)-1:
            return False
        else:
            return True
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())