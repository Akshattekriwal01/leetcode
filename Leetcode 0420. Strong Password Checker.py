"""
420. Strong Password Checker

A password is considered strong if below conditions are all met:

It has at least 6 characters and at most 20 characters.
It must contain at least one lowercase letter, at least one uppercase letter, and at least one digit.
It must NOT contain three repeating characters in a row ("...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).
Write a function strongPasswordChecker(s), that takes a string s as input, and return the MINIMUM change required to make s a strong password. If s is already strong, return 0.

Insertion, deletion or replace of any one character are all considered as one change.

"""

class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        missing_type = 3
        if any("a" < c < "z" for c in s): missing_type -= 1
        if any("A" < c < "Z" for c in s): missing_type -= 1
        if any(c.isdigit() for c in s): missing_type -= 1

        n = len(s)
        # change: to fix seq of three or more, number of changes needed
        # one: # of seq 3k
        # two: # of seq 3k + 1
        change = one = two = 0
        i = 2
        while i < n:
            if s[i] == s[i-1] == s[i-2]:
                l = 2
                while i < n and s[i] == s[i-1]:
                    i += 1
                    l += 1
                if l % 3 == 0:
                    one += 1
                if l % 3 == 1:
                    two += 1
                change += l // 3
            else:
                i += 1

        if n < 6:
            return max(6 - n, missing_type)
        elif n <= 20:
            return max(change, missing_type)
        else:
            delete = n - 20 # mininum delete needed
            change -= min(delete, one) # every delete, change can reduce by one
            change -= min(max(delete - one, 0), two * 2) // 2
            change -= max(delete - one - 2 * two, 0) // 3
            return delete + max(missing_type, change)
                
                