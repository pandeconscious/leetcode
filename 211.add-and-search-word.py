class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isword = False
    
    def search(self, word):
        if not word:
            return self.isword
        if word[0] is not '.':
            ind = get_index(word[0])
            if not self.children[ind]:
                return False
            return self.children[ind].search(word[1:])
        else:
            for childnode in self.children:
                if childnode and childnode.search(word[1:]):
                        return True
            return False
        

class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        currnode = self.trie
        for ch in word:
            ind = get_index(ch)
            if not currnode.children[ind]:
                currnode.children[ind] = TrieNode()
            currnode = currnode.children[ind]
        currnode.isword = True
                

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.trie.search(word)
                    
def get_index(ch):
        return ord(ch) - ord('a')

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
