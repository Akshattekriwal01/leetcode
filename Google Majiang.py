"""
5. 打麻将，输入一组数字，你要验证你能不能胡牌。
    规则是，123 11 --> 胡
                 111 22 --> 胡
                 111 123 --> 不胡
    然后面试官被我一点点挤牙膏，问出来，胡牌规则就是只能有1组pair，然后顺子和碰子可以有任何组，包括0组。
"""

class Solution:
    def canHu(self, arr: List[int]) -> bool:
        counts = [0 for _ in range(10)]
        for x in arr:
            counts[x] += 1
        
        for x in range(1, 10):
            if counts[x] >= 2:
                counts[x] -= 2
                if self.backtrack(1, counts):
                    return True
                counts[x] += 2
        return False

    def backtrack(self, start, counts: List[int]) -> bool:
        if start >= 8:
            return counts[8] == 0 and counts[9] == 0
        cnt = counts[start] % 3
        if counts[start+1] < cnt or counts[start+2] < cnt:
            return False
        counts[start+1] -= cnt
        counts[start+2] -= cnt
        if self.backtrack(start + 1, counts):
            return True
        counts[start + 1] += cnt
        counts[start + 2] += cnt
        return False