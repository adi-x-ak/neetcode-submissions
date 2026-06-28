class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        timer=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==2:
                    queue.append((i,j,timer))
        while(queue):
            i,j,timer = queue.pop(0)
            alldir=[(i+1,j) , (i-1,j),(i,j+1) ,(i,j-1)]
            for di,dj in alldir:
                if(di>=0 and dj>=0 and di<len(grid) and dj<len(grid[0]) and grid[di][dj]==1):
                    queue.append((di ,dj,timer+1))
                    grid[di][dj]=2
        

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    return -1
        return timer

        