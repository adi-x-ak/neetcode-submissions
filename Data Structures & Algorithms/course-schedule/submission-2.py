from collections import deque
from typing import List

class Solution:
    def canFinish(
        self,
        numCourses: int,
        prerequisites: List[List[int]]
    ) -> bool:

        # Build the adjacency list
        graph = [[] for _ in range(numCourses)]

        # indegree[i] = number of prerequisites course i still needs
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        # Add courses with no prerequisites to the queue
        q = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        finished = 0

        # Process available courses
        while q:
            current_course = q.popleft()
            finished += 1

            # Visit courses that depend on current_course
            for next_course in graph[current_course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    q.append(next_course)

        return finished == numCourses