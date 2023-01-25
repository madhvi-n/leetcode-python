class TrieNode:
    def __init__(self):
        self.children = dict.fromkeys(list(string.ascii_lowercase), None)
        self.word_end = None

def insert(root, word):
    curr = root
    for char in word:
        if curr.children[char] is None:
            curr.children[char] = TrieNode()
        curr = curr.children[char]
    curr.word_end = word
    
class Solution:
    def longestWord(self, words: List[str]) -> str:
        head = TrieNode()
        result = []
        for word in words:
            insert(head, word)

        def dfs(root):
            for key, child in root.children.items():
                if child and child.word_end:
                    if len(child.word_end) > len(result):
                        result.append(child.word_end)
                    dfs(child)

        dfs(head)
        return result[-1] if result else ""