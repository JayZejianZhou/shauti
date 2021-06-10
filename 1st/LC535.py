class Codec:

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        # 定义字典，4个换一个, 中间用隔开
        self.short = ""
        self.dic = dict()
        for i in range(0, len(longUrl), 4):
            self.dic[str(i)] = longUrl[i:i+4]
            self.short += str(i) + '.'
        return self.short

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        res = ""
        shortUrl= shortUrl.split('.')
        shortUrl.remove("")
        for it in shortUrl:
            res += str(self.dic[it])
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))