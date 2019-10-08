class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        
    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[None] = None

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def find(word, node):
            if not word:
                return None in node
            char, word = word[0], word[1:]
            if char != '.':
                return char in node and find(word, node[char])
            return any(find(word, kid) for kid in node.values() if kid)
        return find(word, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)