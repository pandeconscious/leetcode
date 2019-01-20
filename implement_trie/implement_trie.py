class TrieNode(object):
    def __init__(self):
        self.children = [None for _ in xrange(ord('a'), ord('z')+1)]
        self.word_end = False
    
    def __getitem__(self, i):
        return self.children[i - ord('a')]
    
    def __setitem__(self, i, item):
        self.children[i - ord('a')] = item

class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        trie = self.root
        for ch in word:
            if trie[ord(ch)] == None:
                trie[ord(ch)] = TrieNode()
            trie = trie[ord(ch)]
        trie.word_end = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        trie = self.root
        for ch in word:
            if trie[ord(ch)] == None:
                return False
            trie = trie[ord(ch)]
        return trie.word_end
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        trie = self.root
        for ch in prefix:
            if trie[ord(ch)] == None:
                return False
            trie = trie[ord(ch)]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
