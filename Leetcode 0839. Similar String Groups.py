"""
839. Similar String Groups

Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y. Also two strings X and Y are similar if they are equal.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list A of strings.  Every string in A is an anagram of every other string in A.  How many groups are there?

 

Example 1:

Input: A = ["tars","rats","arts","star"]
Output: 2
 

Constraints:

1 <= A.length <= 2000
1 <= A[i].length <= 1000
A.length * A[i].length <= 20000
All words in A consist of lowercase letters only.
All words in A have the same length and are anagrams of each other.
The judging time limit has been increased for this question.
"""

class Solution:
    def numSimilarGroups(self, A: List[str]) -> int:
        def similar(word1, word2):
            diff = 0
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    diff += 1
                if diff > 2:
                    return False
            return True
        A = list(set(A))
        indices = {word: idx for idx, word in enumerate(A)}
        N, L = len(A), len(A[0])
        uf = UnionFind(len(A))
        if N < (L * (L - 1) // 2):
            for i in range(len(A)):
                for j in range(i + 1, len(A)):
                    if similar(A[i], A[j]):
                        uf.union(i, j)
        else:
            for i, word in enumerate(A):
                arr = list(word)
                for j in range(L):
                    for k in range(j + 1, L):
                        arr[j], arr[k] = arr[k], arr[j]
                        uf.union(i, indices.get("".join(arr), -1))
                        arr[j], arr[k] = arr[k], arr[j]
        return uf.cc


class UnionFind:
    def __init__(self, n):
        self.id = [i for i in range(n)]
        self.size = [1 for i in range(n)]
        self.cc = n

    def find(self, i):
        root = i
        while root != self.id[root]:
            root = self.id[root]
        while i != root:
            j = self.id[i]
            self.id[i] = root
            i = j
        return root

    def union(self, i, j):
        if i < 0 or j < 0:
            return
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i == root_j:
            return
        if self.size[root_i] < self.size[root_j]:
            self.id[root_i] = root_j
            self.size[root_j] += self.size[root_i]
        else:
            self.id[root_j] = root_i
            self.size[root_i] += self.size[root_j]
        self.cc -= 1