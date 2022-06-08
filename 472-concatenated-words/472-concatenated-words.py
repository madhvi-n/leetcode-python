class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        dictionary = set(words)
        memo = {}

        def dfs(word):
            if word in memo:
                return memo[word]
            
            memo[word] = False
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in dictionary and suffix in dictionary:
                    memo[word] = True
                    break
                if prefix in dictionary and dfs(suffix):
                    memo[word] = True
                    break
                if suffix in dictionary and dfs(prefix):
                    memo[word] = True
                    break
            return memo[word]
        return [word for word in words if dfs(word)]