class TweetCounts(object):

    def __init__(self):
        self.tweet = collections.defaultdict(list)

    def recordTweet(self, tweetName, time):
        """
        :type tweetName: str
        :type time: int
        :rtype: None
        """
        self.tweet[tweetName].append(time)        

    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
        """
        :type freq: str
        :type tweetName: str
        :type startTime: int
        :type endTime: int
        :rtype: List[int]
        """
        times = self.tweet[tweetName]
        times.sort()

        if freq == "minute":
            multiplier = 60
        elif freq == "hour":
            multiplier = 3600
        elif freq == "day":
            multiplier = 86400 
        
        num_mult = (endTime - startTime)/multiplier
        rest = [startTime + num_mult*multiplier, endTime]
        
        res = []
        for i in range(num_mult):
            temp = self.finf_duration(times, startTime + i*multiplier, startTime + (i+1)*multiplier -1) # 注意我写的函数是双闭集
            res.append(temp)
        # 最后收拢剩下的
        temp = self.finf_duration(times, rest[0], rest[1])
        res.append(temp)
        
        return res
            
        
    # 找到固定时间内的点，双闭集
    def finf_duration(self, times, start, end):
        res = 0
        for i in range(start, end+1):
            if i in times:
                res+=1
        return res


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)