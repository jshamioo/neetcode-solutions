class Twitter:

    def __init__(self):
        self.globalNumTweets = 0
        self.followers = defaultdict(set)
        self.following = defaultdict(set)
        self.userTweets = defaultdict(deque)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.globalNumTweets += 1
        if userId not in self.userTweets:
            self.userTweets[userId] = deque(maxlen=10)
        
        self.userTweets[userId].appendleft((self.globalNumTweets, tweetId))


    def getNewsFeed(self, userId: int) -> List[int]:
        minHeapTweets = []
        heapq.heapify(minHeapTweets)

        for user in list(self.following[userId]) + [userId]:
            for globalTweetNum, userTweetId in self.userTweets[user]:
                if len(minHeapTweets) == 10:
                    currLowestTweetNum, currLowestUserTweetId = minHeapTweets[0]
                    if currLowestTweetNum < globalTweetNum:
                        heapq.heappop(minHeapTweets)
                        heapq.heappush(minHeapTweets, (globalTweetNum, userTweetId))
                    continue
                
                heapq.heappush(minHeapTweets, (globalTweetNum, userTweetId))
                
        result = [tweetId for _, tweetId in sorted(minHeapTweets, reverse=True)]
        return result


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return  # prevent self-follow
        self.followers[followeeId].add(followerId)
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followeeId].discard(followerId)
        self.following[followerId].discard(followeeId)
        
        
