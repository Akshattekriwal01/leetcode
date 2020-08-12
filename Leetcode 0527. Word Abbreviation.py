"""
527. Word Abbreviation

Given an array of n distinct non-empty strings, you need to generate minimal possible abbreviations for every word following rules below.

Begin with the first character and then the number of characters abbreviated, which followed by the last character.
If there are any conflict, that is more than one words share the same abbreviation, a longer prefix is used instead of only the first character until making the map from word to abbreviation become unique. In other words, a final abbreviation cannot map to more than one original words.
If the abbreviation doesn't make the word shorter, then keep it as original.
Example:
Input: ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
Output: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
Note:
Both n and the length of each word will not exceed 400.
The length of each word is greater than 1.
The words consist of lowercase English letters only.
The return answers should be in the same order as the original array.
"""

class Solution:
    def wordsAbbreviation(self, dict: List[str]) -> List[str]:
        def get_abv(word, i):
            if len(word) - i <= 3:
                return word
            return word[:i+1] + str(len(word) - i - 2) + word[-1]

        n = len(dict)
        prefix = [0] * n
        abbrevations = [get_abv(word, 0) for word in dict]
        for i in range(n):
            while True:
                dup = set([i])
                for j in range(i + 1, n):
                    if abbrevations[j] == abbrevations[i]:
                        dup.add(j)
                if len(dup) == 1:
                    break
                for k in dup:
                    prefix[k] += 1
                    abbrevations[k] = get_abv(dict[k], prefix[k])
        return abbrevations

    def wordsAbbreviation(self, dict: List[str]) -> List[str]:
        import collections
        groups = collections.defaultdict(list)
        n = len(dict)
        for index, word in enumerate(dict):
            groups[(word[0], word[-1], len(word))].append((word, index))
        abbrevations = [None for _ in range(n)]
        for (first, last, l), group in groups.items():
            if len(group) == 1:
                word, index = group[0]
                if l >= 4:
                    abbrevations[index] = first + str(l - 2) + last
                else:
                    abbrevations[index] = word
                continue
            trie = Trie()
            for word, index in group:
                trie.add(word[1:-1]) 
            
            for word, index in group:
                prefix = trie.query(word[1:-1])
                if l - len(prefix) - 2 > 1:
                    abbrevations[index] = first + prefix + str(l - len(prefix) - 2) + last
                else:
                    abbrevations[index] = word    
        return abbrevations


class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.count += 1
    
    def query(self, word):
        """ return shortest unique prefix"""
        node = self.root
        prefix = []
        i = 0
        while i < len(word):
            if node.count == 1:
                break
            prefix.append(word[i])
            node = node.children[word[i]]
            i += 1
        return "".join(prefix)
