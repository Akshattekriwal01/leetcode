"""
1131. Maximum of Absolute Value Expression

Given two arrays of integers with equal lengths, return the maximum value of:

|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|

where the maximum is taken over all 0 <= i, j < arr1.length.

 

Example

Input: arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
Output: 13
Example 2:

Input: arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]
Output: 20
 

Constraints:

2 <= arr1.length == arr2.length <= 40000
-10^6 <= arr1[i], arr2[i] <= 10^6
"""

class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        """
        assume i > j, |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j| is the max of:
            (arr1[i] - arr1[j]) + (arr2[i] - arr2[j]) + (i - j) => (arr1[i] + arr2[i] + i) - (arr1[j] + arr2[j] + j) => a(i) - a(j)
            (arr1[i] - arr1[j]) - (arr2[i] - arr2[j]) + (i - j) => (arr1[i] - arr2[i] + i) - (arr1[j] - arr2[j] + j) => b(i) - b(j)
            -(arr1[i] - arr1[j]) + (arr2[i] - arr2[j]) + (i - j) => (-arr1[i] + arr2[i] + i) - (-arr1[j] + arr2[j] + j) => c(i) - c(j)
            -(arr1[i] - arr1[j]) - (arr2[i] - arr2[j]) + (i - j) => (-arr1[i] - arr2[i] + i) - (-arr1[j] - arr2[j] + j) => d(i) - d(j)

        so the problem reduces to finding max different of abs(f(i) - f(j)) for all [a, b, c, d]
        """
        a = lambda i: arr1[i] + arr2[i] + i
        b = lambda i: arr1[i] - arr2[i] + i
        c = lambda i: -arr1[i] + arr2[i] + i
        d = lambda i: -arr1[i] - arr2[i] + i

        ans = 0
        for f in [a, b, c, d]:
            minf = maxf = f(0)
            for i in range(1, len(arr1)):
                curr = f(i)
                minf = min(minf, curr)
                maxf = max(maxf, curr)
                ans = max(ans, maxf - minf)
        return ans