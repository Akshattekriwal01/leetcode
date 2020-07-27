"""
844. Backspace String Compare

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
"""

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        """
        approach 1:
            Use two stacks to store characters, if see a backspace pop stack
            time O(N), space O(N)
        approach 2: use two points starting at the end of the two strings, 
            Move pointers towards the beginning, if see a backspace move one 
            more step.
            time O(N), space O(1)
        """
        def move(s, i):
            """ move the pointer towards beginning by checking backspaces """
            bal = 0 # number of unused backspace
            while i >= 0 and (bal > 0 or s[i] == "#"):
                if s[i] == "#":
                    bal += 1
                else:
                    bal -= 1
                i -= 1
            return i

        i = len(S) - 1
        j = len(T) - 1
        while i >= 0 and j >= 0:
            i = move(S, i)
            j = move(T, j)
            if i < 0 and j < 0:
                return True
            if i < 0 or j < 0 or S[i] != T[j]:
                return False
            i -= 1
            j -= 1
        return move(S, i) < 0 and move(T, j) < 0