class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        result = []
        result.insert(0, deck.pop(0))
        for i, element in enumerate(deck):
            result.insert(0, result.pop())
            result.insert(0, element) 
        return result