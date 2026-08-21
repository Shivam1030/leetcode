class Solution:
    def dfs(self, grid: List[List[str]], row: int, col: int, R: int, C: int):
        diff = [0,1,0,-1,0]
        grid[row][col] = '0'
        for di in range(4):
            adjR,adjC = row+diff[di],col+diff[di+1]
            if(adjR>=0 and adjR<R and adjC>=0 and adjC<C and grid[adjR][adjC] == '1'):
                self.dfs(grid,adjR,adjC,R,C)

    def numIslands(self, grid: List[List[str]]) -> int:
        R,C,count = len(grid),len(grid[0]), 0
        for row in range(R):
            for col in range(C):
                if(grid[row][col] == '1'):
                    self.dfs(grid,row,col,R,C)
                    count+=1
        return count