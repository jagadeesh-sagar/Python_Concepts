
def generateParenthesis(n: int) -> list[str]:
        result=[]

        def backtrack(current,opend,closed):

            if len(current)==n*2:
                result.append(current)
                return
        
            if opend<n:                
                backtrack(current+"(",opend=opend+1,closed=closed)

            if closed<opend:
                backtrack(current+")",opend=opend,closed=closed+1)
            
        backtrack(current='',opend=0,closed=0)

        return result

# print(generateParenthesis(n=3))

'''
LC 51 — N-Queens

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]
'''

def solveNQueens(n:int) -> list[list[str]]:
    result=[]
    current=[]


    def queen_place(p):
        s=''
        for k in range(n):
            if k==p:
                s+="Q"
            else:
              s+="."
        return s


    def backtrack(start,n,row,column,diagonal1,diagonal2):
        if len(current)==n:
            result.append(current.copy())
            return 
                    
        i=start
        for p in range(n) :
            if p in column:
                continue
            if i+p not in diagonal2 and i-p not in diagonal1:
                row[i]=True
                column[p]=True
                diagonal1[i-p] = True
                diagonal2[i+p] = True  
                current.append(queen_place(p))            

                backtrack(start+1,n,row=row,column=column,diagonal1=diagonal1,diagonal2=diagonal2)

                current.pop()
                row.pop(i)
                column.pop(p)
                diagonal1.pop(i-p)
                diagonal2.pop(i+p)
    
    backtrack(0,n,row={},column={},diagonal1={},diagonal2={})
    return result

'''
https://chatgpt.com/s/t_6aedec0dfb448191bae37700c07add91
'''
        
# print(solveNQueens(n=1))


'''
37. Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

Example 1:
Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:


'''

def solveSudoku(board: list[list[str]]) -> None:

    numbers={"1","2","3","4","5","6","7","8","9"}
    rows:dict[int[set]]={i:set() for i in range(9)}
    columns:dict[int[set]]={i:set() for i in range(9)}
    box_grid={i:set() for i in range(9)}

    for row in range(9):
        for column in range(9):
            box_index=(row//3)*3+(column//3)

            if board[row][column] in numbers:
                rows[row].add(board[row][column])
                columns[column].add(board[row][column])
                box_grid[box_index].add(board[row][column])


    def backtrack(row:int,column:int):
        next_row=row
        next_column=column+1

        if row==9:
            return True
        
        if next_column==9:
            next_row+=1
            next_column=0
        
        if board[row][column] in numbers:
            return backtrack(row=next_row,column=next_column)

        for i in range(1,10):
            box_index=(row//3)*3+(column//3)
            i=str(i)

            if i not in box_grid[box_index]:
                if i not in rows[row] and i not in columns[column]:
                    board[row][column]=i
                    rows[row].add(i)
                    columns[column].add(i)
                    box_grid[box_index].add(i)

                    if backtrack(row=next_row,column=next_column):
                        return True

                    board[row][column]="."
                    rows[row].remove(i)
                    columns[column].remove(i)
                    box_grid[box_index].remove(i)

        return False

  
    return backtrack(row=0,column=0)

'''

for any sudoko there is only one solution so every step you get true or false
'''

# print(solveSudoku(board=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))

