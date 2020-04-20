"""
Given a list of reviews, a list of keywords and an integer k. Find the most popular k keywords in order of most to least frequently mentioned.

The comparison of strings is case-insensitive. If keywords are mentioned an equal number of times in reviews, sort alphabetically.

Example 1:

Input:
k = 2
keywords = ["anacell", "cetracular", "betacellular"]
reviews = [
  "Anacell provides the best services in the city",
  "betacellular has awesome services",
  "Best services provided by anacell, everyone should use anacell",
]

Output:
["anacell", "betacellular"]

Explanation:
"anacell" is occuring in 2 different reviews and "betacellular" is only occuring in 1 review.
Example 2:

Input:
k = 2
keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
reviews = [
  "I love anacell Best services; Best services provided by anacell",
  "betacellular has great services",
  "deltacellular provides much better services than betacellular",
  "cetracular is worse than anacell",
  "Betacellular is better than deltacellular.",
]

Output:
["betacellular", "anacell"]

Explanation:
"betacellular" is occuring in 3 different reviews. "anacell" and "deltacellular" are occuring in 2 reviews, but "anacell" is lexicographically smaller.
"""
from typing import List
import heapq
import collections
import unittest

class Solution:
    def topKFrequentKeywords(self, k: int, keywords: List[str], 
        reviews: List[str]) -> List[str]:
        counts = {word: 0 for word in keywords}
        for review in reviews:
            l = r = 0
            seen = set()
            # keyword may be at the end of text
            while r <= len(review):
                if r == len(review) or not review[r].isalpha():
                    word = review[l:r].lower()
                    if word in counts and word not in seen:
                        counts[word] += 1
                        seen.add(word)
                    l = r + 1
                r += 1
        heap = []
        for word, count in counts.items():
            heapq.heappush(heap, MyObj(word, count))
            if len(heap) > k:
                heapq.heappop(heap)
        topk = []
        while heap:
            topk.append(heapq.heappop(heap).word)
        return topk[::-1]


class MyObj:
    """
    A custom object class that implements the required comparison order for 
    keywords.
    """
    def __init__(self, word: str, count: int) -> None:
        self.word = word
        self.count = count

    def __lt__(self, obj):
        if self.count < obj.count:
            return True
        elif self.count == obj.count:
            return self.word > obj.word
        else:
            return False


class TestSolution(unittest.TestCase):
    def test1(self):
        k = 2
        keywords = ["anacell", "cetracular", "betacellular"]
        reviews = [
          "Anacell provides the best services in the city",
          "betacellular has awesome services",
          "Best services provided by anacell, everyone should use anacell",
        ]
        output = ["anacell", "betacellular"]
        self.assertEqual(Solution().topKFrequentKeywords(k, keywords, reviews),
          output, "Should be [\"anacell\", \"betacellular\"]")

    def test2(self):
        k = 2
        keywords = ["anacell", "betacellular", "cetracular", "deltacellular",
          "eurocell"]
        reviews = [
          "I love anacell Best services; Best services provided by anacell",
          "betacellular has great services",
          "deltacellular provides much better services than betacellular",
          "cetracular is worse than anacell",
          "Betacellular is better than deltacellular.",
        ]
        output = ["betacellular", "anacell"]
        self.assertEqual(Solution().topKFrequentKeywords(k, keywords, reviews),
          output, "Should be [\"betacellular\", \"anacell\"]")


if __name__ == "__main__":
    unittest.main()