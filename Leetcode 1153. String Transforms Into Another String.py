"""
1153. String Transforms Into Another String

Given two strings str1 and str2 of the same length, determine whether you can transform str1 into str2 by doing zero or more conversions.

In one conversion you can convert all occurrences of one character in str1 to any other lowercase English character.

Return true if and only if you can transform str1 into str2.

 

Example 1:

Input: str1 = "aabcc", str2 = "ccdee"
Output: true
Explanation: Convert 'c' to 'e' then 'b' to 'd' then 'a' to 'c'. Note that the order of conversions matter.
Example 2:

Input: str1 = "leetcode", str2 = "codeleet"
Output: false
Explanation: There is no way to transform str1 to str2.
 

Note:

1 <= str1.length == str2.length <= 10^4
Both str1 and str2 contain only lowercase English letters.
"""

class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        """
        scenario 1: one to many
        str1: aa
        str2: bc
        conversion: a -> b, a -> c
        
        scenario 2: one to one
        str1: ab
        str2: cd
        conversion: a -> c, b -> d
        
        scenario 3: chain
        str1: ab
        str2: bc
        conversion: a -> b -> c
        step1: b -> x, ab => ax
        step2: a -> b, ax => bx
        step3: x -> c, bx => bc
        
        scenario 4: circle
        str1: abc
        str2: bca
        conversion: a -> b -> c -> a
        step1: c -> x, abc => abx
        step2: b -> c, abx => acx
        step3: a -> b, acx => bcx
        step4: x -> a, bcx => bca
        
        scenario 5: target str2 contain all letters
        """
        if str1 == str2:
            return True
        conversion = {}
        for c1, c2 in zip(str1, str2):
            if conversion.get(c1, c2) != c2:
                return False
            conversion[c1] = c2
        return len(set(str2)) < 26