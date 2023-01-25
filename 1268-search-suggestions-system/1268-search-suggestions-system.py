class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []
        

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = TrieNode()
        for product in sorted(products):
            self._insert(product, root)
        return self._search(searchWord, root)
    
    def _insert(self, product: str, root: TrieNode) -> None:
        curr = root
        for char in product:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            
            curr.suggestions.append(product)
            curr.suggestions.sort()
            
            if len(curr.suggestions) > 3:
                curr.suggestions.pop()
    
    def _search(self, searchWord: str, root: TrieNode) -> List[List[str]]:              
        ans = []
        for char in searchWord:
            if root:
                root = root.children.get(char)
            ans.append(root.suggestions if root else [])            
        return ans
