"""
552. Student Attendance Record II

Given a positive integer n, return the number of all possible attendance records with length n, which will be regarded as rewardable. The answer may be very large, return it after mod 109 + 7.

A student attendance record is a string that only contains the following three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A record is regarded as rewardable if it doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

Example 1:
Input: n = 2
Output: 8 
Explanation:
There are 8 records with length 2 will be regarded as rewardable:
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" won't be regarded as rewardable owing to more than one absent times. 
Note: The value of n won't exceed 100,000.

"""

class Solution:
    def checkRecord(self, n: int) -> int:
        # state: (last_letter, num_A, num_L)
        # last_letter: last letter in the sequence, can be any of "A", "L", "P"
        # num_A: total count of A in the sequence, should less than 2
        # num_L: number of L the sequence ended with, should be less than 3
        if n == 0:
            return 0
        MOD = 10 ** 9 + 7
        prev = {("A", 1, 0): 1, ("P", 0, 0): 1, ("L", 0, 1): 1}
        for _ in range(2, n + 1):
            curr = collections.defaultdict(int)
            for (char, num_A, num_L), cnt in prev.items():
                cnt %= MOD
                if num_A == 0:
                    curr[("A", 1, 0)] = (curr[("A", 1, 0)] + cnt) % MOD
                if num_L <= 1:
                    curr[("L", num_A, num_L + 1)] = (curr[("L", num_A, num_L + 1)] + cnt) % MOD
                curr[("P", num_A, 0)] = (curr[("P", num_A, 0)] + cnt) % MOD
            prev = curr
        return sum(prev.values()) % MOD


    def checkRecord(self, n: int) -> int:
        """ possible states
                0: .......A
                1: ...A...P
                2: ...A...L
                3: ...A...LL
                4: .......P
                5: .......L
                6: .......LL
        define the number of rewardable seq at current step for each state f[i]
        where i is the idx of state; initially f = [0, 0, 0, 0, 1, 0, 0].

        moving current step to the next, f[i] is updated as following,
            f[0] = f[4] + f[5] + f[6]
            f[1] = f[0] + f[1] + f[2] + f[3]
            f[2] = f[0] + f[1] 
            f[3] = f[2]
            f[4] = f[4] + f[5] + f[6]
            f[5] = f[4]
            f[6] = f[5]
        these updates could be translated into a matrix dot product:
            f = M * f
        where M is:
            [[0, 0, 0, 0, 1, 1, 1],
             [1, 1, 1, 1, 0, 0, 0],
             [1, 1, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 1, 1],
             [0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 1, 0]]

        so for the nth step, f_n = M^n * f_0
        """
        MOD = 10 ** 9 + 7
        def power(A, n):
            # binary representation of n
            # 39 =  1   0   1   0   1   1, then A^39 is the product of
            #      A^32    A^4     A^2 A^1
            base = A
            ans = [[0] * len(A) for _ in range(len(A))]
            for i in range(len(A)):
                ans[i][i] = 1
            while n > 0:
                if n % 2 == 1:
                    ans = multiply(ans, base)
                base = multiply(base, base)
            return ans

        def multiply(A, B):
            m, n, l = len(A), len(A[0]), len(B[0])
            C = [[0] * l for _ in range(m)]
            for i in range(m):
                for j in range(l):
                    C[i][j] = sum(A[i][k] * B[k][j] for k in range(n)) % MOD
            return C

        f = [[0], [0], [0], [0], [1], [0], [0]]
        M = [
            [0, 0, 0, 0, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0]]
        f = multiply(power(M, n), f)
        return sum(f[i] for i in range(7)) % MOD