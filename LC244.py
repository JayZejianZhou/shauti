class WordDistance(object):

    def __init__(self, wordsDict):
        """
        :type wordsDict: List[str]
        """
        # 统计出现位置
        self.data = collections.defaultdict(list)
        for count, val in enumerate(wordsDict):
            self.data[val].append(count)
        

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # 取出位置
        ls1, ls2 = self.data[word1], self.data[word2]
        
        cur_min = float("inf")
        for it in ls1:
            last = float("inf")    # 统计一下上一次的差是多少，因为排过序了，所以如果增加的话那就不行，说明这一个it的最小已经找到了
            for jt in ls2:
                if abs(it-jt) > last: break
                else: 
                    last = abs(it-jt)
                    cur_min = min(last, cur_min)
        
        return cur_min


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)