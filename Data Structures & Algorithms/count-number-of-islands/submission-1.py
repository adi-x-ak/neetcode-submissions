class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        we need to tarverse the matrix 
        when the row col ==1 nad its not in visited set 
        we do  bfson that row and col 
        '''
        row,col= len(grid) , len(grid[0])
        visted=set()
        islands=0

        def bfs(r,c):
            q=deque()
            visted.add((r,c))
            q.append((r,c))
            while q:
                x,y=q.popleft()
                dir=[(1,0),(-1,0),(0,1),(0,-1)]
                for dr ,dc in dir:
                    if((x+dr) in range(row)
                    and (y+dc) in range(col)
                    and grid[x+dr][y+dc]=="1"
                    and (x+dr,y+dc) not in visted):
                        q.append((x+dr,y+dc))
                        visted.add((x+dr,y+dc))




        for r in range(row):
            for c in range(col):
                if grid[r][c]=="1" and (r,c) not in visted:
                    bfs(r,c) 
                    islands+=1
        return islands 

        