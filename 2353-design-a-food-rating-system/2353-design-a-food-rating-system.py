class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.mapping = {}
        self.ratings = defaultdict(list)
        for food, cuisine, rating in zip(foods, cuisines, ratings): 
            self.mapping[food] = (cuisine, rating)
            heapq.heappush(self.ratings[cuisine],(-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, rating = self.mapping[food]
        self.mapping[food] = cuisine, newRating
        heapq.heappush(self.ratings[cuisine],(-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        while self.ratings[cuisine] and -self.ratings[cuisine][0][0] != self.mapping[self.ratings[cuisine][0][1]][1]:
            heapq.heappop(self.ratings[cuisine])
        return self.ratings[cuisine][0][1]

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)