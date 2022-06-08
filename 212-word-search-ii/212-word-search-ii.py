class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_end = False

    def insert(self, word):
        curr = self
        for char in word:
            curr = curr.children.setdefault(char, TrieNode())
        curr.word_end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.insert(word)

        rows, cols = len(board), len(board[0])
        self.num_words = len(words)
        result = []

        def dfs(row, col, node, path, result):
            if self.num_words == 0:
                return

            if node.word_end:
                result.append(path)
                node.word_end = False
                self.num_words -= 1

            if (row < 0 or col < 0 or
                row == rows or col == cols):
                return

            temp = board[row][col]

            if temp not in node.children:
                return

            board[row][col] = '#'

            for x,y in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                dfs(row + x, col + y, node.children[temp], path + temp, result)

            board[row][col] = temp

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "", result)

        return result