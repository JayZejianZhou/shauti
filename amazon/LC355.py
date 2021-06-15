class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users = {}  # user: who you follow        
        self.tweets = {} # user: twits
        self.time = 0    # record time

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        if not self.users.get(userId):
            self.users[userId] = [userId]
        
        if not self.tweets.get(userId): 
            self.tweets[userId] = []
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        feeds = []
        if not self.users.get(userId): return None
        for it in self.users[userId]:
            if not self.tweets.get(it): continue
            feeds += self.tweets[it]
        feeds.sort(key=lambda l:l[0], reverse=True)
        return [it[1] for it in feeds[0:10]]
            
        

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if not self.users.get(followerId): self.users[followerId] = [followerId]
        if not followeeId in self.users[followerId]: self.users[followerId].append(followeeId)
        

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if self.users.get(followerId) and followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)