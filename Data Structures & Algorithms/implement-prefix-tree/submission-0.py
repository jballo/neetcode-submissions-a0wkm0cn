class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False


class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        root = self.root
        for char in word:
            if char not in root.children:
                root.children[char] = Node()
            root = root.children[char]
        
        root.isWord = True

    def search(self, word: str) -> bool:
        root = self.root
        for char in word:
            if char not in root.children:
                return False
            root = root.children[char]
        
        return True if root.isWord else False

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for char in prefix:
            if char in root.children:
                root = root.children[char]
            else:
                return False

        return True