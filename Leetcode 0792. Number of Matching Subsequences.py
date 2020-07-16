"""
792. Number of Matching Subsequences

Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.

Example :
Input: 
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".
Note:

All words in words and S will only consists of lowercase letters.
The length of S will be in the range of [1, 50000].
The length of words will be in the range of [1, 5000].
The length of words[i] will be in the range of [1, 50].
"""

class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        """
            1. store the indexes of all chars in ascending order
            2. given a query word "...xy...", the index that y appears in S
               should be larger than the index appears in S
            3. scan the word char by char, and for the current char x record the
               smallest index it appears in S called i_x, for the next char y, 
               find the smallest index i_y larger than i_x. If i_y does not exist
               then this word is not subsequence of S
        """
        char_indexes = collections.defaultdict(list)
        for idx, char in enumerate(S):
            char_indexes[char].append(idx)
        ans = 0
        N = len(S)
        for word in words:
            flag = 1
            idx_prev = -1
            for char in word:
                i = bisect.bisect_right(char_indexes[char], idx_prev)               
                if i == len(char_indexes[char]):
                    flag = 0
                    break
                idx_prev = char_indexes[char][i]
            ans += flag
        return ans
                    
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        """
        using pointers for each word and a pointer for the string S
        
        """

        heads = [[] for _ in range(26)]
        for i, word in enumerate(words):
            heads[ord(word[0]) - ord("a")].append((i, 1))

        ans = 0
        for c in S:
            old_bucket = heads[ord(c) - ord("a")][:]
            heads[ord(c) - ord("a")] = []
            for i, j in old_bucket:
                if j == len(words[i]):
                    ans += 1
                else:
                    heads[ord(words[i][j]) - ord("a")].append((i, j + 1))
        return ans