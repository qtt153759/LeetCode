class Solution(object):
    def numIslands(self, grid):
        result=0
        rowLength=len(grid)
        colLength=len(grid[0])
        def inbound(row,col):
            if row<0 or row==rowLength:
                return False
            if col<0 or col==colLength:
                return False
            return True
        def dfs(row,column):
            for direction in ((-1,0),(1,0),(0,-1),(0,1)):
                newRow=row+direction[0]
                newCol=column+direction[1]
                if inbound(newRow,newCol) and  grid[newRow][newCol]=="1":
                    grid[newRow][newCol]="2"
                    dfs(row+direction[0],column+direction[1])
        for row in range(rowLength):
            for column in range(colLength):
                if grid[row][column]=="1":
                    grid[row][column]="2"
                    dfs(row,column)
                    result+=1
        return result

sol=Solution()
print(sol.numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))