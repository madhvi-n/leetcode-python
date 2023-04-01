from datetime import datetime

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        return max(0, self.getDate(min(leaveAlice, leaveBob)) - self.getDate(max(arriveAlice, arriveBob)) + 1)
    
    def getDate(self, date):
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        month, day = tuple(map(int, date.split('-')))
        return sum(months[:month - 1]) + day
