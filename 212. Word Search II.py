class TrieNode:
    def __init__(self):
        self.is_word = None
        self.children = {}
class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.root
        for letter in word:
            current = current.children.setdefault(letter, TrieNode())
        current.is_word = word
class Solution:
    def search(self, i, j, root, board, m, n, r):
        char = board[i][j]
        if not (char and char in root.children):
            return

        board[i][j], root = None, root.children[char]

        if root.is_word:
            r.append(root.is_word)
            root.is_word = None

        for x, y in ((0, -1), (-1, 0), (0, 1), (1, 0)):
            ii, jj = i + x, j + y
            if 0 <= ii < m and 0 <= jj < n:
                self.search(ii, jj, root, board, m, n, r)
        board[i][j] = char
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board:
            return []

        tree = Trie()
        [tree.insert(word) for word in words]

        m, n, r = len(board), len(board[0]), []

        for i, row in enumerate(board):
            for j, char in enumerate(row):
                self.search(i, j, tree.root, board, m, n, r)
        return r