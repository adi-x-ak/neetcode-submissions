from collections import deque
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        maxarea = 0

        def bfs(r, c):
            q = deque()
            result = 1  # Count the starting cell

            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    if (
                        (row + dr) in range(rows)
                        and (col + dc) in range(cols)
                        and grid[row + dr][col + dc] == 1
                        and (row + dr, col + dc) not in visited
                    ):
                        q.append((row + dr, col + dc))
                        visited.add((row + dr, col + dc))
                        result += 1

            return result

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = bfs(r, c)
                    maxarea = max(maxarea, area)

        return maxarea