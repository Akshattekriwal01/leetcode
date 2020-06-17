"""
273. Integer to English Words

Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
"""

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        def less_than_20(x: int) -> str:
            switcher = {
                1: "One",
                2: "Two",
                3: "Three",
                4: "Four",
                5: "Five",
                6: "Six",
                7: "Seven",
                8: "Eight",
                9: "Nine",
                10: "Ten",
                11: "Eleven",
                12: "Twelve",
                13: "Thirteen",
                14: "Fourteen",
                15: "Fifteen",
                16: "Sixteen",
                17: "Seventeen",
                18: "Eighteen",
                19: "Nineteen"
            }
            return switcher[x]

        def tens(x: int) -> str:
            switcher = {
                20: "Twenty",
                30: "Thirty",
                40: "Forty",
                50: "Fifty",
                60: "Sixty",
                70: "Seventy",
                80: "Eighty",
                90: "Ninety"
            }
            return switcher[x]

        def less_than_1000(x: int) -> str:
            res = []
            while x > 0:
                if x >= 100:
                    res.append(less_than_20(x // 100))
                    res.append("Hundred")
                    x %= 100
                elif x >= 20:
                    res.append(tens(x // 10 * 10))
                    x %= 10
                else:
                    res.append(less_than_20(x))
            return " ".join(res)

        def more_than_1000(x: int) -> str:
            switcher = {
                1000: "Thousand",
                1000000: "Million",
                1000000000: "Billion"
            }
            return switcher[x]

        res = []
        base = 10 ** 9
        while base > 0:
            if num >= base:
                res.append(less_than_1000(num // base))
                if base > 1:
                    res.append(more_than_1000(base))
            num %= base
            base //= 1000
        return " ".join(res)
         

