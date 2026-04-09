class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        root = self.root

        for char in word:
            if char not in root.children:
                root.children[char] = Node()
            root = root.children[char]
        
        root.isWord = True

    def search(self, word: str) -> bool:
        
        def dfs(root, index):

            for i in range(index, len(word)):
                char = word[i]
                if char != ".":
                    if char not in root.children:
                        return False
                    root = root.children[char]
                else:
                    for child in root.children.values():
                        if dfs(child, i + 1):
                            return True
                    return False
            
            return root.isWord

        return dfs(self.root, 0)
