class UndergroundSystem:

    def __init__(self):
        self.ids = {}
        self.pairs = {}
        self.frequency = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.ids[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        name, t2 = self.ids.pop(id)
        self.pairs[(name, stationName)] = t - t2 + self.pairs.get((name, stationName), 0)
        self.frequency[(name, stationName)] = 1 + self.frequency.get((name, stationName), 0)
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.pairs[startStation, endStation]/self.frequency[startStation, endStation]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)