class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # user_id -> [count, tweetId]
        self.followMap = defaultdict(set) # user_id -> hashset(followeeId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1
        if len(self.tweetMap[userId]) > 10:
            self.tweetMap[userId].pop(0)

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        res = []

        # include user itself into the followMap since the 10 most recent
        # tweets can also from the user itself

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            # edge case: check if the followee has tweets
            if followeeId in self.tweetMap:
                # retrieve the most recent tweet and append to the heap
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index-1])
        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                c, t = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [c, t, followeeId, index-1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
