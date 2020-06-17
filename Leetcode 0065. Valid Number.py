"""
65. Valid Number

Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.

"""

class Solution:
    def isNumber(self, s: str) -> bool:
        """
        intuitions: FSA (finite state automata)
        what are the types of (partial) valid numbers and how these types transition given a new input character?

        states:
            S0: empty or spaces only (partially valid), i.e. " "
            S1: number without dot, i.e. " 1"
            S2: (spaces) + dot (partially valid), i.e. " ."
            S3: number ending with dot, i.e. " 1."
            S4: (spaces) + sign (partially valid), i.e. " +"
            S5: scientific number ending with e (partially valid), i.e. "1e"
            S6: scientific number ending with sign (partially valid), i.e. "1e+"
            S7: scientific number ending with digit, i.e. "-1.2e+1"
            S8: number + (spaces)
            -1: invalid 
        input:
            space: 0
            digit: 1
            dot: 2
            sign: 3
            exp: 4
            invalid: 5
        """

        transitions = [
        # input type:
            # 0: space
            # 1: digit
            # 2: dot
            # 3: sign
            # 4: exp
            # 5: invalid
            [0, 1, 2, 4, -1, -1], # S0: empty or spaces only
            [8, 1, 3, -1, 5, -1], # S1: digits only
            [-1, 3, -1, -1, -1, -1], # S2: dot only
            [8, 3, -1, -1, 5, -1], # S3: digits and one dot
            [-1, 1, 2, -1, -1, -1], # S4: sign only
            [-1, 7, -1, 6, -1, -1], # S5: exp
            [-1, 7, -1, -1, -1, -1], # S6: exp and sign
            [8, 7, -1, -1, -1, -1], # S7: exp and digits
            [8, -1, -1, -1, -1, -1], # S8: valid number + spaces
        ]
        state = 0
        input_type = -1
        for c in s:
            if c == " ":
                input_type = 0
            elif c.isdigit():
                input_type = 1
            elif c == ".":
                input_type = 2
            elif c == "+" or c == "-":
                input_type = 3
            elif c == "e":
                input_type = 4
            else:
                input_type = 5
            state = transitions[state][input_type]
            if state == -1:
                return False
        return state in [1, 3, 7, 8]