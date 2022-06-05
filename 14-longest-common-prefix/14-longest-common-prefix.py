class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


def insert(root, word):
    curr = root
    for char in word:
        curr = curr.children.setdefault(char, TrieNode())
    curr.end_of_word = True
    
    
class Solution:
    def longestCommonPrefix(self, words: List[str]) -> str:
        head = TrieNode()

        for word in words:
            insert(head, word)

        lcp = ""
        curr = head

        # loop until we find the end of word and node has only 1 child
        while curr and not curr.end_of_word and len(curr.children) == 1:
            for key, val in curr.children.items():
                lcp += key
                curr = val

        return lcp