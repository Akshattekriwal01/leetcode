"""
753. Cracking the Safe

There is a box protected by a password. The password is a sequence of n digits where each digit can be one of the first k digits 0, 1, ..., k-1.

While entering a password, the last n digits entered will automatically be matched against the correct password.

For example, assuming the correct password is "345", if you type "012345", the box will open because the correct password matches the suffix of the entered password.

Return any password of minimum length that is guaranteed to open the box at some point of entering it.

 

Example 1:

Input: n = 1, k = 2
Output: "01"
Note: "10" will be accepted too.
Example 2:

Input: n = 2, k = 2
Output: "00110"
Note: "01100", "10011", "11001" will be accepted too.
 

Note:

n will be in the range [1, 4].
k will be in the range [1, 10].
k^n will be at most 4096.
"""

class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        """
        Eulerian path and Eulerian circuit in graph

        Definition:
            Eulerian path is a path that visit each edge exactly once.
            Eulerian circuit is Eulerian path that start and end at the same 
            node.

        Conditions:
            First of all, all nodes with non zero degrees need to belong to the
            same connected component.
            
            Eulerian path exists in undirected graph if and only if either all 
            nodes have even degree or exactly two nodes have odd degree.

            Eulerian circuit exists in undirected graph if and only if all 
            nodes have even degree.

            Eulerian path exists in directed graph if and only if at most one
            node has indegree - outdegree == 1 and at most one node has 
            outdegree - indegree == 1 and all other nodes has equal indegree 
            and outdegree.

            Eulerian circuit exists in directed graph if and only if all nodes
            has equal indegree and outdegree.
        """
        ans = []
        seen = set()
        def dfs(node):
            for i in range(k):
                nei = node + str(i)
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei[1:])
                    ans.append(str(i))
        dfs("0" * (n - 1))
        return "".join(ans) + "0" * (n - 1)

    def crackSafe(self, n: int, k: int) -> str:
        """ mathematics """
        M = k ** (n - 1)
        P = [k * q + i for i in range(k) for q in range(M)]
        ans = []
        for i in range(k ** n):
            j = i
            while P[j] >= 0:
                ans.append(str(j / M))
                P[j], j = -1, P[j]
        return "".join(ans) + "0" * (n - 1)