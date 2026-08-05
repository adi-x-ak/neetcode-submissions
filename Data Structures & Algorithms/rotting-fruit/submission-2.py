class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        timer=0
        rows,cols=len(grid),len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r,c,timer))
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        while q:
            row,col,timer=q.popleft()
            directions=[[1,0],[-1,0],[0,1],[0,-1]]
            for dr,dc in directions:
                if(
                    (row+dr) in range(rows)
                    and (col+dc) in range(cols)
                    and grid[row+dr][col+dc]==1
                ):
                    grid[row+dr][col+dc]=2
                    q.append((row+dr,col+dc,timer+1))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    return -1
        return timer


        