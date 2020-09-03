"""
世界杯淘汰赛阶段，每个球队夺冠的概率。
已知有个表格知道16强两两之间胜负的概率，以及一个16强对阵表。
求输入任意一个球队，返回这个球队最终夺冠概率。
"""
import collections
import unittest
from typing import List

class Solution:
    def winProb(self, match: List[int], table: List[List[float]]) -> List[float]:
        queue = collections.deque([{team: 1.0} for team in match]) # initial round, every team survives with proba = 1.0
        while len(queue) > 1:
            # each round, merge two groups using cartesian product
            # a team survives this round with probability of it survives previous round multiplies
            # the marginal probability that it wins any team in the other groups that survived previous round
            # p(team|r) = p(team|r-1) * sum(p(team|other team) * p(other team|r-1), other team in the neighbor group)
            group1 = queue.popleft()
            group2 = queue.popleft()
            new_group = {}
            for a in group1:
                p = 0.0
                for b in group2:
                    p += table[a][b] * group2[b]
                new_group[a] = group1[a] * p
            for b in group2:
                p = 0.0
                for a in group1:
                    p += table[b][a] * group1[a]
                new_group[b] = group2[b] * p
            queue.append(new_group)
        return [queue[0][i] for i in range(len(match))]


class TestSolution(unittest.TestCase):
    def test(self):
        match = [0, 1, 2, 3]
        table = [[1.0, 0.3, 0.8, 0.4],
                 [0.7, 1.0, 0.5, 0.6],
                 [0.2, 0.5, 1.0, 0.3],
                 [0.6, 0.4, 0.7, 1.0]]
        output = []
        print(Solution().winProb(match, table))
        self.assertTrue(abs(sum(Solution().winProb(match, table)) - 1.0) < 1e-10, "Probability should add up to 1.0")
    
    def test2(self):
        match = [0, 1, 2, 3]
        table = [[1.0, 0.5, 0.5, 0.5],
                 [0.5, 1.0, 0.5, 0.5],
                 [0.5, 0.5, 1.0, 0.5],
                 [0.5, 0.5, 0.5, 1.0]]
        output = []
        print(Solution().winProb(match, table))
        self.assertTrue(abs(sum(Solution().winProb(match, table)) - 1.0) < 1e-10, "Probability should add up to 1.0")

    def test3(self):
        match = [0, 1, 2, 3]
        table = [[1.0, 1.0, 0.5, 0.5],
                 [0.0, 1.0, 0.5, 0.5],
                 [0.5, 0.5, 1.0, 0.5],
                 [0.5, 0.5, 0.5, 1.0]]
        output = []
        print(Solution().winProb(match, table))
        self.assertTrue(abs(sum(Solution().winProb(match, table)) - 1.0) < 1e-10, "Probability should add up to 1.0")

if __name__ == "__main__":
    unittest.main()