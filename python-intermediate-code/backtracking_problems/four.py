
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
        
print(solveNQueens(n=1))