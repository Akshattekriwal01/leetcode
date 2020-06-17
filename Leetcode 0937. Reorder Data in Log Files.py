"""
937. Reorder Data in Log Files

You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.

 

Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
 

Constraints:

0 <= logs.length <= 100
3 <= logs[i].length <= 100
logs[i] is guaranteed to have an identifier, and a word after the identifier.
"""

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        indices = range(len(logs)).sort(key=lambda i: MyLog(i, logs[i]))
        return [logs[i] for i in indices]

class MyLog(object):
    def __init__(self, idx: int, text: str):
        self.idx = idx
        self.text = text
        
    def __lt__(self, other):
        i = self.text.index(" ") + 1 # index of first letter after identifier
        j = other.text.index(" ") + 1 # index of first letter after identifier
        if self.text[i].isdigit() and other.text[j].isdigit():
            return self.idx < other.idx
        elif self.text[i].isdigit():
            return False
        elif other.text[j].isdigit():
            return True
        else:
            if self.text[i:] < other.text[j:]:
                return True
            elif self.text[i:] == other.text[j:]:
                return self.text[:i] < other.text[:j]
            else:
                return False