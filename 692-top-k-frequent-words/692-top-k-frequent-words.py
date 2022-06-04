class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        hashmap = dict()
        
        for word in words:
            hashmap[word] = 1 + hashmap.get(word, 0)
        
        res = [key for key, val in sorted(hashmap.items(), key=lambda x: (-x[1]))]
        
        return res[:k]
        
