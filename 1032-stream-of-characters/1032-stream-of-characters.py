class TrieNode:
    def __init__(self):
        self.children = dict()
        self.word_end = False

class StreamChecker:
    
    def __init__(self, words):
        """
        :type words: List[str]
        """      
        self.waitlist = []
        self.root = TrieNode()
        
        for word in words:
            current_node = self.root
            for letter in word:
                if letter not in current_node.children:
                    current_node.children[letter] = TrieNode()
                current_node = current_node.children[letter]
            current_node.word_end = True

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        waitlist = []
        
        if letter in self.root.children:
            waitlist.append(self.root.children[letter])
            
        for item in self.waitlist:
            if letter in item.children:
                waitlist.append(item.children[letter])
                
        self.waitlist = waitlist
        return any(item.word_end for item in self.waitlist)