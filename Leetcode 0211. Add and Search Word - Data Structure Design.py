"""
211. Add and Search Word - Data structure design

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.

"""

class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        nodes = [root]
        for char in word:
            if char == ".":
                # flatten an nested python object should start with outter loop
                nodes = [child for node in nodes 
                    for child in node.children.values()]
            else:
                nodes = [node.children[char] for node in nodes 
                    if char in node.children]
            if len(nodes) == 0:
                return False
        return any(node.isWord for node in nodes)


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False