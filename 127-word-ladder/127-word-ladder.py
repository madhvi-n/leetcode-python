class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0
        
        length = len(beginWord)
        words = defaultdict(list)
        
        for word in wordList:
            for i in range(length):
                words[word[:i] + "*" + word[i+1:]].append(word)
        
        queue = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)
        
        while queue:
            current_word, level = queue.popleft()
            
            for i in range(length):
                possible_word = current_word[:i] + "*" + current_word[i+1:]
                
                for word in words[possible_word]:
                    if word == endWord:
                        return level + 1
                    
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level + 1))
        return 0
        