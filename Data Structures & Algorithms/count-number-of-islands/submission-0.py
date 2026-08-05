from collections import deque
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # first always check validation
        if not grid:
            return 0
        #lets get the dimensions of the grid 
        rows,cols = len(grid) , len(grid[0])
        #lets create a set to keep tarck of visited nodes
        visited = set()
        #keep track of number od islands encounterd so far
        islands=0
        #lets write the  bfs function 
        def bfs(r,c):
            q=deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                #pop the element
                row,col=q.popleft()
                #now we need to check all the adacent posotions 
                directions=[[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    if ((row+dr) in range(rows) and 
                        (col+dc) in range(cols)and      
                        grid[row+dr][col+dc]=="1"
                        and (row+dr,col+dc) not in visited):
                        q.append((row+dr,col+dc))
                        visited.add((row+dr,col+dc))


 #lets traverse the matrix 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c)not in visited:
                    bfs(r,c)
                    islands+=1
        return islands 