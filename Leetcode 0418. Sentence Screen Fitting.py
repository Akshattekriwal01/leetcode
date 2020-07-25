"""
418. Sentence Screen Fitting

Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given sentence can be fitted on the screen.

Note:

A word cannot be split into two lines.
The order of words in the sentence must remain unchanged.
Two consecutive words in a line must be separated by a single space.
Total words in the sentence won't exceed 100.
Length of each word is greater than 0 and won't exceed 10.
1 ≤ rows, cols ≤ 20,000.
Example 1:

Input:
rows = 2, cols = 8, sentence = ["hello", "world"]

Output: 
1

Explanation:
hello---
world---

The character '-' signifies an empty space on the screen.
Example 2:

Input:
rows = 3, cols = 6, sentence = ["a", "bcd", "e"]

Output: 
2

Explanation:
a-bcd- 
e-a---
bcd-e-

The character '-' signifies an empty space on the screen.
Example 3:

Input:
rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]

Output: 
1

Explanation:
I-had
apple
pie-I
had--

The character '-' signifies an empty space on the screen.
"""

from typing import List

class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        """
        Intuition: use simulation to count how many characters (including 
        necessary spaces) the given screen can print. The result will be the
        total characters divided by size of the sentence (including spaces).
        The constrain of the typing is that a new line always start at the 
        beginning of a word.

        To count the number of characters, join the sentence with space to form
        a proper string S. Now, use a cnt variable to record number of 
        characters been printed and iterate through the rows. At each row, it
        can print at most cols # of characters, so increment cnt by cols; next
        check which character in the S the pointer is currently, i=cnt%len(S);
        there are three possibilities inlustrated as below:
            AB-CDE-FG
                  |   i = i + 1
                  at space, move one step to the beginning of next word

            AB-CDE-FG
                 |    i = i + 2
                 at end of a word, move two steps to the beginning of next word
            AB-CDE-FG
                |     i retro back until the beginning of a word
                in the middle of a word
        """
        S = " ".join(sentence) + " "
        n = len(S)
        cnt = 0 # number of characters it can print
        for i in range(rows):
            cnt += cols - 1
            i = cnt % n
            if S[i] == " ":
                cnt += 1
            elif S[i+1] == " ":
                cnt += 2
            else:
                while i > 0 and S[i-1] != " ":
                    cnt -= 1
                    i -= 1
        return cnt / len(S)