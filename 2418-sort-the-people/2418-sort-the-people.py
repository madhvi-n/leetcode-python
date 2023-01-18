class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        array = sorted(list(zip(names, heights)), key = lambda x: x[1], reverse=True)
        return [name for name, height in array]