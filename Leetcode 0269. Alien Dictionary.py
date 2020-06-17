"""
269. Alien Dictionary

There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
] 

Output: "" 

Explanation: The order is invalid, so return "".
Note:

You may assume all letters are in lowercase.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
"""

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        topological sort
        time: O(C + E + V), E <= min(V^2, N - 1) <= O(26^2), O(V) <= O(26)
        space: O(E + V) ~ O(26^2)
        """
        import collections
        graph = collections.defaultdict(set)
        indegree = collections.defaultdict(int)
        letters = set()
        for word in words:
            for char in word:
                letters.add(char)
        for i in range(len(words) - 1):
            j = 0
            while j < min(len(words[i]), len(words[i + 1])):
                if words[i][j] != words[i + 1][j]:
                    graph[words[i][j]].add(words[i + 1][j])
                    # avoid repeatly counting indegree
                    if words[i + 1][j] not in graph[words[i][j]]:
                        indgree[words[i + 1][j]] += 1
                    break
                j += 1
            if j == len(words[i]) and len(words[i]) > len(words[i + 1]):
                return ""
        queue = collections.deque([c for c in letters if indegree[c] == 0])
        res = []
        while queue:
            u = queue.popleft()
            res.append(u)
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        return "".join(res) if len(res) == len(letters) else ""
