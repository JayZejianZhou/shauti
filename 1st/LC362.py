class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hit_num = []

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        self.hit_num.append(timestamp)
        

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        hit_nums = 0
        for i in range(len(self.hit_num)-1, -1, -1):
            if self.hit_num[i] > timestamp-300 and self.hit_num[i] <= timestamp:
                hit_nums += 1
                
            if self.hit_num[i] < timestamp-300:
                break
        return hit_nums
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)