import heapq
from collections import defaultdict

class Twitter:
    def __init__(self):
        self.followees = defaultdict(dict)
        self.tweets = defaultdict(list)
        self.timestamp = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId].append((-self.timestamp, -tweetId))
            heapq.heapify(self.tweets[userId])
        else:
            heapq.heappush(self.tweets[userId], (-self.timestamp,-tweetId))
        self.timestamp += 1
        self.followees[userId][userId] = True

        return
        
    def getNewsFeed(self, userId: int) -> List[int]:
        latestUsersTweets = []
        for i in range(10):
            mostRecentTweet = (None, None, None) # (UserId, timestamp, TweetId)
            for followedUser in self.followees[userId].keys():
                if len(self.tweets[followedUser]) > 0 and (mostRecentTweet == (None, None, None) or self.tweets[followedUser][0][0] < mostRecentTweet[1]):
                    mostRecentTweet = (followedUser, self.tweets[followedUser][0][0], self.tweets[followedUser][0][1])
            if mostRecentTweet != (None, None, None):
                latestUsersTweets.append(mostRecentTweet)
                heapq.heappop(self.tweets[mostRecentTweet[0]])

        for i in range(len(latestUsersTweets)):
            heapq.heappush(self.tweets[latestUsersTweets[i][0]], (latestUsersTweets[i][1], latestUsersTweets[i][2]))

        latestTweets = [abs(tweetId) for (userId, timestamp, tweetId) in latestUsersTweets]
        return latestTweets        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId][followeeId] = True
        return
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followees[followerId]:
            del self.followees[followerId][followeeId]
        return

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)