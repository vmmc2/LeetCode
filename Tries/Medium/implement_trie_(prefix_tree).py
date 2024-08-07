class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.endOfWord = True
        
        return

    def search(self, word: str) -> bool:
        answer = True

        curr = self.root
        for ch in word:
            if ch not in curr.children:
                answer = False
                return answer
            curr = curr.children[ch]

        if not curr.endOfWord:
            answer = False
            return answer
        
        return answer

    def startsWith(self, prefix: str) -> bool:
        answer = True

        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                answer = False
                return answer
            curr = curr.children[ch]

        return answer

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)