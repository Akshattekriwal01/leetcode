"""
425. Word Squares

Given a set of words (without duplicates), find all word squares you can build from them.

A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.

b a l l
a r e a
l e a d
l a d y
Note:
There are at least 1 and at most 1000 words.
All words will have the exact same length.
Word length is at least 1 and at most 5.
Each word contains only lowercase English alphabet a-z.
Example 1:

Input:
["area","lead","wall","lady","ball"]

Output:
[
  [ "wall",
    "area",
    "lead",
    "lady"
  ],
  [ "ball",
    "area",
    "lead",
    "lady"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
Example 2:

Input:
["abat","baba","atan","atal"]

Output:
[
  [ "baba",
    "abat",
    "baba",
    "atan"
  ],
  [ "baba",
    "abat",
    "baba",
    "atal"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
"""

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        """
        time O(N*L^(N*L))
        space O(L)
        """
        n = len(words[0])

        def iter_prefix(prefix):
            l = len(prefix)
            for word in words:
                if word[:l] == prefix:
                    yield word
        
        def backtrack(path, sqr):
            if len(path) == n:
                sqr.append(path[:])
                return
            i = len(path)
            prefix = "".join([w[i] for w in path])
            for word in iter_prefix(prefix):
                backtrack(path + [word], sqr)
        
        sqr = []
        for word in words:
            backtrack([word], sqr)
        return sqr

    def wordSquares(self, words: List[str]) -> List[List[str]]:
        """
        time O(N*26^L)
        space O(N*L)
        """
        L = len(words[0])
        prefix = collections.defaultdict(list)
        for word in words:
            for l in range(1, L):
                prefix[word[:l]].append(word)

        def backtrack(path, sqr):
            if len(path) == L:
                sqr.append(path[:])
                return
            i = len(path)
            p = "".join([w[i] for w in path])
            for word in prefix[p]:
                backtrack(path + [word], sqr)
        sqr = []
        for word in words:
            backtrack([word], sqr)
        return sqr

    def wordSquares(self, words: List[str]) -> List[List[str]]:
        """
        time O(NL26^L)
        space O(NL)
        """
        L = len(words[0])
        trie = Trie()
        for word in words:
            trie.add(word)
        
        def backtrack(path, sqr):
            if len(path) == L:
                sqr.append(path[:])
                return
            i = len(path)
            p = "".join([w[i] for w in path])
            for word in trie.query(p):
                backtrack(path + [word], sqr)
        
        sqr = []
        for word in words:
            backtrack([word], sqr)
        return sqr

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
class Trie:
    def __init__(self):
        self.root =  TrieNode()

    def add(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isWord = True

    def query(self, prefix):
        import collections
        node = self.root
        for c in prefix:
            if c not in node.children:
                return []
            node = node.children[c]
        words = []
        deq = collections.deque([(node, [])])
        while deq:
            for _ in range(len(deq)):
                node, path = deq.popleft()
                if node.isWord:
                    words.append(prefix + "".join(path))
                for c in node.children:
                    deq.append((node.children[c], path + [c]))
        return words

