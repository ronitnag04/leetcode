class Trie:

    def __init__(self):
        self.tree = []
        

    def insert(self, word: str) -> None:
        self.tree.append(word)
        self.tree.sort()

    def search(self, word: str) -> bool:
        return word in self.tree

    def startsWith(self, prefix: str) -> bool:
        l = len(prefix)
        pres = [s[:l] for s in self.tree]
        return prefix in pres


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)