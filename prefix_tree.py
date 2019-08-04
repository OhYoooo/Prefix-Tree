from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.nodes = defaultdict(TrieNode)
        self.count = 0
        self.isWord = False

class Trie:
    def __init__(self):
        """
        Initialize data structure.
        """
        self.root = TrieNode()
    
    def insert(self, word: str):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if word == '':
            return
        curr = self.root
        for char in word:
            curr.count += 1
            curr = curr.nodes[char]
        curr.count += 1
        curr.isWord = True

    def query(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        :type target: str
        :rtype: bool
        """
        if word == '':
            return False
        curr = self.root
        for char in word:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        return curr.isWord

    def startWith(self, prefix: str) -> int:
        """
        Returns the number of words in the trie that start with the given prefix.   
        :type prefix: str
        :rtype: int
        """
        if prefix == '':
            return 0
        curr = self.root
        for char in prefix:
            if char not in curr.nodes:
                return 0
            curr = curr.nodes[char]
        return curr.count

    def lazyDelete(self, target: str) -> bool:
        """
        Returns true if target exist and successfully delete from the trie.
        :type target: str
        :rtype: bool
        """
        if target == '':
            return False
        curr = self.root
        for char in target:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        if curr.isWord:
            curr.isWord = False
            return True
        else:
             return False

    def listAllMatches(self, prefix: str):
        """
        Returns all words started with prefix
        :param prefix:
        :return: List[str]
        """
        result = []
        if prefix == '':
            return result
        def recursiveQuery(node: TrieNode, path: str):
            if len(node.nodes) == 0:
                result.append(path)
            else:
                for key in node.nodes.keys():
                    recursiveQuery(node.nodes[key], path + key)
        
        curr = self.root
        for char in prefix:
            if char not in curr.nodes:
                return result
            curr = curr.nodes[char]
        recursiveQuery(curr, prefix + '')
        return result
