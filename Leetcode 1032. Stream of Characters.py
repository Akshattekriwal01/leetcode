"""
1032. Stream of Characters

Implement the StreamChecker class as follows:

StreamChecker(words): Constructor, init the data structure with the given words.
query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order from oldest to newest, including this letter just queried) spell one of the words in the given list.
 

Example:

StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
streamChecker.query('a');          // return false
streamChecker.query('b');          // return false
streamChecker.query('c');          // return false
streamChecker.query('d');          // return true, because 'cd' is in the wordlist
streamChecker.query('e');          // return false
streamChecker.query('f');          // return true, because 'f' is in the wordlist
streamChecker.query('g');          // return false
streamChecker.query('h');          // return false
streamChecker.query('i');          // return false
streamChecker.query('j');          // return false
streamChecker.query('k');          // return false
streamChecker.query('l');          // return true, because 'kl' is in the wordlist
 

Note:

1 <= words.length <= 2000
1 <= words[i].length <= 2000
Words will only consist of lowercase English letters.
Queries will only consist of lowercase English letters.
The number of queries is at most 40000.
"""

from typing import List
import collections


class Solution:
    def __init__(self, words: List[str]):
        self.chars = collections.deque()
        self.trie = Trie()
        self.k = 0
        for word in words:
            self.trie.add(word)
            self.k = max(self.k, len(word))

    def query(self, letter: str) -> bool:
        self.chars.append(letter)
        if len(self.chars) > self.k:
            self.chars.popleft()
        return self.trie.query(self.chars)


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for ch in word[::-1]:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isWord = True

    def query(self, chars):
        node = self.root
        for i in range(len(chars) - 1, -1, -1):
            ch = chars[i]
            node = node.children.get(ch, None)
            if not node:
                return False
            if node.isWord:
                return True
        return False