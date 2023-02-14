class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        root = self.root
        for char in word:
            if char not in root.children:
                root.children[char] = TrieNode()
            root = root.children[char]
        root.word_end = True
    
    def prefix_exists(self, word):
        root = self.root
        for char in word:
            if root.word_end:
                return True
            if char not in root.children:
                return False
            root = root.children[char]
        return root.word_end
        
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        answer = []
        folder.sort()
        
        trie = Trie()
        
        for subfolder in folder:
            chars = subfolder.split('/')
            if not trie.prefix_exists(chars):
                trie.insert(chars)
                answer.append(subfolder)
        return answer