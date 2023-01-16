class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        score = dict()
        
        for winner, loser in matches:
            score[winner] = score.get(winner, 0)
            score[loser] = score.get(loser, 0) + 1
        
        winner, loser = [], []
        for player, count in score.items():
            if count == 0:
                winner.append(player)
            if count == 1:
                loser.append(player)
        
        return [sorted(winner), sorted(loser)]