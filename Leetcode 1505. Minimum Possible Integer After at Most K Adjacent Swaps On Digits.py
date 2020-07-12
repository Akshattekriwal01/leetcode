"""
1505. Minimum Possible Integer After at Most K Adjacent Swaps On Digits

Given a string num representing the digits of a very large integer and an integer k.

You are allowed to swap any two adjacent digits of the integer at most k times.

Return the minimum integer you can obtain also as a string.

 

Example 1:


Input: num = "4321", k = 4
Output: "1342"
Explanation: The steps to obtain the minimum integer from 4321 with 4 adjacent swaps are shown.
Example 2:

Input: num = "100", k = 1
Output: "010"
Explanation: It's ok for the output to have leading zeros, but the input is guaranteed not to have any leading zeros.
Example 3:

Input: num = "36789", k = 1000
Output: "36789"
Explanation: We can keep the number without any swaps.
Example 4:

Input: num = "22", k = 22
Output: "22"
Example 5:

Input: num = "9438957234785635408", k = 23
Output: "0345989723478563548"
 

Constraints:

1 <= num.length <= 30000
num contains digits only and doesn't have leading zeros.
1 <= k <= 10^9
"""

class Solution:
    def minInteger(self, num: str, k: int) -> str:
        n = len(num)
        if k >= n * (n + 1) // 2:
            return "".join(sorted(num))
        pos = [collections.deque() for _ in range(10)]
        for i, d in enumerate(num):
            pos[ord(d) - ord("0")].append(i)
        visited = [False] * n
        #bit = BIT(n)
        ans = []
        while k > 0:
            found = False
            for d in range(10):
                if len(pos[d]) > 0:
                    i = pos[d][0]
                    cost = i - sum(visited[:i])#bit.query(i)
                    if cost <= k:
                        found = True
                        visited[i] = True
                        #bit.add(i)
                        pos[d].popleft()
                        ans.append(num[i])
                        k -= cost
                        break
            if not found:
                break
        for i in range(n):
            if not visited[i]:
                ans.append(num[i])
        return "".join(ans)

class BIT:
    def __init__(self, n):
        self.sum = [0] * (n + 1)

    def add(self, i):
        i += 1
        while i < len(self.sum):
            self.sum[i] += 1
            i += i & -i

    def query(self, i):
        i += 1
        total = 0
        while i > 0:
            total += self.sum[i]
            i -= i & -i
        return total