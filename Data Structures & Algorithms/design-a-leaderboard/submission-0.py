from collections import Counter

class Leaderboard:

    def __init__(self):
        self.scores = Counter()
        
    # use Counter to add score to player: { id : score}
    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] += score
        
    # get top k players, sum up their scores, and return 
    def top(self, K: int) -> int:
        return sum(score[1] for score in self.scores.most_common(K))
        
    # reset player score to 0
    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
