'''
79. Word Search
'''

def exist(board: list[list[str]], word: str) -> bool:


    if word.isspace():
        return False
    if len(board)==0:
        return False
    
    if len(word)>len(board)*len(board[0]):
        return False

    def dfs(row,column,index):

        if index==len(word):
            return True
        if row <0 or row>=len(board) or column<0 or column>=len(board[row]):
            return False

        if board[row][column]!=word[index]:
            return False
        
        board[row][column]="#"
    
        if dfs(row,column+1,index+1):
            return True
        if dfs(row,column-1,index+1):
            return True

        if dfs(row+1,column,index+1):
            return True
        if dfs(row-1,column,index+1):
            return True

        board[row][column]=word[index]
        return False
    

    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column]==word[0]:
                if dfs(row,column,index=0):
                    return True

    return False


# print(exist(board=[["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]], word = "aaaaaaaaaaab"))

'''
200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

'''
def numIslands(grid: list[list[str]]) -> int:

    islands=0
    visited=set()

    def dfs(row,column):
    
        if row<0 or column< 0 or row>=len(grid) or column>=len(grid[0]):
            return 

        if grid[row][column]=="1" and (row,column) not in visited:
        
            visited.add((row,column))   
            dfs(row,column+1)
            dfs(row,column-1)
            dfs(row+1,column)
            dfs(row-1,column)


    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column]=="1" and (row,column) not in visited:
                islands+=1
                dfs(row,column)
                
    return islands

'''

695. Max Area of Island

'''
def maxAreaOfIsland(grid: list[list[str]]) -> int:

    islands=0
    max_area=0
    area=0
    visited=set()

    def dfs(row,column):
        nonlocal max_area,area
      
        if row<0 or column< 0 or row>=len(grid) or column>=len(grid[0]):
            return 0

        if grid[row][column]==1 and (row,column) not in visited:
          area+=1
          
          visited.add((row,column))   
          dfs(row,column+1)
          dfs(row,column-1)
          dfs(row+1,column)
          dfs(row-1,column)
    
          return area


    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column]==1 and (row,column) not in visited:
                islands+=1
                max_area=max(max_area,dfs(row,column))
                area=0
                
    return max_area

print(maxAreaOfIsland(grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],
[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
))

