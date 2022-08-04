class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_end = False
    
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            curr = curr.children.setdefault(char, TrieNode())
        curr.word_end = True
        
    def search(self, word: str) -> bool:
        
        def dfs(node, i):
            if i == len(word): return node.word_end

            if word[i] == ".":
                for child in node.children:
                    if dfs(node.children[child], i+1): 
                        return True
                    
            if word[i] in node.children:
                return dfs(node.children[word[i]], i+1)
            
            return False
        return dfs(self.root, 0)
