def solve(board: list[list[str]]) -> None:
    result=[]

    def dfs(row,column):
        if row<0 or column< 0 or row>=len(board) or column>=len(board[0]):
            return 
        
        if board[row][column]=='O':
          board[row][column]="T"
          dfs(row,column+1)
          dfs(row,column-1)
          dfs(row+1,column)
          dfs(row-1,column)
            
    def fill_zero():
        for row in range(len(board)):
            for column in range(len(board[0])):
            
                if board[row][column]=="O":
                    board[row][column]="X"
                    
                if board[row][column]=="T":
                    board[row][column]="O"
     
    

    for row in range(len(board)):
        for column in range(len(board[0])):
            if column==0 or row==0 or column==len(board[0])-1 or row==len(board)-1:
                print(row,column)
                dfs(row,column)
    fill_zero()

    # return board

print(solve(board=[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))