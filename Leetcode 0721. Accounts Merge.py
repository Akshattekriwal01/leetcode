"""
721. Accounts Merge

Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:
Input: 
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation: 
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Note:

The length of accounts will be in the range [1, 1000].
The length of accounts[i] will be in the range [1, 10].
The length of accounts[i][j] will be in the range [1, 30].
"""

class Solution:
    def accountsMerge1(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        graph + dfs: account -> email
        time: O(Sum((N_i)log(N_i)))
        space: O(Sum(N_i))
        """
        email_account_map = collections.defaultdict(list)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                email_account_map[email].append(i)

        def dfs(i, emails, visited):
            if visited[i]:
                return
            visited[i] = True
            for email in accounts[i][1:]:
                emails.add(email)
                for j in email_account_map[email]:
                    dfs(j, emails, visited)

        visited = [False] * len(accounts)
        ans = []
        for i, account in enumerate(accounts):
            if visited[i]:
                continue
            name = account[0]
            emails = set()
            dfs(i, emails, visited)
            ans.append([name] + sorted(list(emails)))
        return ans


    def accountsMerge1(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        union-find
        """
        n = len(accounts)
        uf = UnionFind(n)
        email_account_map = {}
        for i in range(n):
            for email in accounts[i][1:]:
                if email in email_account_map:
                    uf.union(i, email_account_map[email])
                else:
                    email_account_map[email] = i
        merged = {}
        for i in range(n):
            root = uf.find(i)
            if root not in merged:
                merged[root] = [accounts[i][0], set()]
            for email in accounts[i][1:]:
                merged[root][1].add(email)
        return [[name] + sorted(list(emails)) for name, emails in merged.values()]


class UnionFind:
    def __init__(self, n):
        self.id = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

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