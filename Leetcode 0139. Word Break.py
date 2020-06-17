"""
139. Word Break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""

class Solution:
    def wordBreak1(self, s: str, wordDict: List[str]) -> bool:
        """
        time: O(NM), N = len(s), M = len(wordDict)
        space: O(N)
        """
        dp = [True] + [False] * len(s)
        for i in range(1, len(s) + 1):
            for word in wordDict:
                if dp[i - len(word)] and s[i - len(word):i] == word:
                    dp[i] = True
                    break
        return dp[-1]

    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        """
        time: O(N^2)
        space: O(N + L), L = # of characters in all words
        """
        wordSet = set(wordDict)
        dp = [True] + [False] * len(s)
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        return dp[-1]

    def wordBreak3(self, s: str, wordDict: List[str]) -> bool:
        """
        trie + bfs
        time: O(N*L)
        space: O(N + L), L = total characters in all words
        """
        trie = Trie()
        for word in wordDict:
            trie.add(word)

        lenSet = set([len(word) for word in wordDict])
        queue = collections.deque([0])
        visited = set([0])
        while queue:
            i = queue.popleft()
            if i == len(s):
                return True
            for l in lenSet:
                if i + l not in queue and trie.query(s[i:i + l]):
                    queue.append(i + l)
                    visited.add(i + l)
        return False


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isWord = True

    def query(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.isWord