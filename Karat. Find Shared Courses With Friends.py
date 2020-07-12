"""
You are a developer for a university. Your current project is to develop a system for students to find courses they share with friends. The university has a system for querying courses students are enrolled in, returned as a list of (ID, course) pairs.

Write a function that takes in a list of (student ID number, course name) pairs and returns, for every pair of students, a list of all courses they share.
"""

import unittest
from typing import List, Dict, Tuple


class Solution:
    def findSharedCourses(self, 
        student_course_pairs: List[List[str]]) -> Dict[Tuple[int], List[int]]:
        student_courses = {}
        for student, course in student_course_pairs:
            if int(student) not in student_courses:
                student_courses[int(student)] = set()
            student_courses[int(student)].add(course)
        ans = {}
        for s1, c1 in student_courses.items():
            for s2, c2 in student_courses.items():
                if s1 == s2 or tuple(sorted((s1, s2))) in ans:
                    continue
                ans[tuple(sorted((s1, s2)))] = sorted(c1.intersection(c2))
        return ans


    def findMidCourse(self, prerequisites: List[List[str]]) -> str:
        import collections
        graph = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        courses = set()
        for u, v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1
            courses.add(u)
            courses.add(v)
        
        path = [course for course in courses if indegree[course] == 0]
        while len(graph[path[-1]]) > 0:
            prev = path[-1]
            path.append(graph[prev][0])
        n = len(path)
        return path[(n + 1) // 2 - 1]


    def findMidCourses(self, prerequisites: List[List[str]]) -> str:
        import collections
        graph = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        courses = set()
        for u, v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1
            courses.add(u)
            courses.add(v)
        
        tracks = []
        paths = collections.deque([[u] for u in courses if indegree[u] == 0])
        while paths:
            path = paths.popleft()
            if not graph[path[-1]]:
                tracks.append(path[:])
            else:
                for v in graph[path[-1]]:
                    paths.append(path + [v])
        return sorted(set([track[(len(track) + 1) // 2 - 1] for track in tracks]))



class TestSolution(unittest.TestCase):
    def test1(self):
        student_course_pairs = [
            ["58", "Software Design"],
            ["58", "Linear Algebra"],
            ["94", "Art History"],
            ["94", "Operating Systems"],
            ["17", "Software Design"],
            ["58", "Mechanics"],
            ["58", "Economics"],
            ["17", "Linear Algebra"],
            ["17", "Political Science"],
            ["94", "Economics"],
            ["25", "Economics"],
        ]
        output = {
            tuple(sorted((58, 17))): sorted(["Software Design", "Linear Algebra"]),
            tuple(sorted((58, 94))): sorted(["Economics"]),
            tuple(sorted((58, 25))): sorted(["Economics"]),
            tuple(sorted((94, 25))): sorted(["Economics"]),
            tuple(sorted((17, 94))): [],
            tuple(sorted((17, 25))): []
        }
        self.assertEqual(
            Solution().findSharedCourses(student_course_pairs),
            output, "Should be equal."
        )

    def test2(self):
        student_course_pairs = [
            ["42", "Software Design"],
            ["0", "Advanced Mechanics"],
            ["9", "Art History"],
        ]
        output = {
            tuple(sorted((0, 42))): [],
            tuple(sorted((0, 9))): [],
            tuple(sorted((9, 42))): []
        }
        self.assertEqual(
            Solution().findSharedCourses(student_course_pairs),
            output, "Should be equal."
        )

    def test3(self):
        all_courses = [
            ["Logic", "COBOL"],
            ["Data Structures", "Algorithms"],
            ["Creative Writign", "Data Structures"],
            ["Algorithms", "COBOL"],
            ["Intro to Computer Science", "Data Structures"],
            ["Logic", "Compilers"],
            ["Data Structures", "Logic"],
            ["Creative Writing", "System Administration"],
            ["Databases", "System Administration"],
            ["Creative Writing", "Databases"]
        ]
        output = sorted(["Creative Writing", "Databases", "Data Structures"])
        self.assertEqual(
            Solution().findMidCourses(all_courses), 
            output, "Should be equal")


if __name__ == "__main__":
    unittest.main()
