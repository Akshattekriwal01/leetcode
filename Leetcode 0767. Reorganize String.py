"""
767. Reorganize String

Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].
"""
import heapq
import collections

class Solution:
    def reorganizeString(self, S: str) -> str:
        """
        time: O(NlogA), A = number of unique chars
        space: O(N)
        """
        count = collections.Counter(S)
        if max(count.values()) > (len(S) + 1) // 2:
            return ""
        heap = [(-cnt, char) for char, cnt in count.items()]
        heapq.heapify(heap)
        ans = []
        while heap:
            first_cnt, first = heapq.heappop(heap)
            if not ans or ans[-1] != first:
                ans.append(first)
                if first_cnt < -1:
                    heapq.heappush(heap, (first_cnt + 1, first))
            else:
                second_cnt, second = heapq.heappop(heap)
                ans.append(second)
                heapq.heappush((first_cnt, first))
                if second_cnt < -1:
                    heapq.heappush(heap, (second_cnt + 1, second))
        return "".join(ans)