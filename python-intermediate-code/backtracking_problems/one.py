'''
in backtracking follow this 4 principles 

1.base class (same as for recursion)
2.choose
3.explore (recursion)
4.unchoose (pop())

Practice in this order:

Subsets
Combinations
Permutations
Combination Sum
N Queens
Sudoku

GENERIC TEMPLATE

def backtrack(path):

    if solution_found:
        print(path)
        return

    for choice in choices:

        # choose
        path.append(choice)

        # explore
        backtrack(path)

        # undo
        path.pop()


https://chatgpt.com/share/6a0af5f5-d9a8-8323-ae52-8b254f7f44bb
'''

'''
Generate all subsets of a list - [1,2,3] → [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]

'''

def subset(list1:list[int])->list[list[int]]:
    result=[]
    current=[]

    def backtract(start):

        result.append(current[:])

        for i in range(start,len(list1)):

            current.append(list1[i]) #choose

            backtract(i+1) #explore

            current.pop()  # unchoose
        
    backtract(0)

    print(result)


subset(list1=[1,2,3])


'''
Generate all valid parentheses combinations - For n=2: ["(())", "()()"]

generate everything -> then validate  (Dont do this) rather -> only build valid paths

'''

def valid_parentheses(n:int):

    result=[]

    def backtrack(current,opend,closed):


        if len(current)==n*2:
            result.append(current)
            return 

        if opend < n:
            backtrack(current+'(',opend+1,closed)
        
        if closed < opend:
            backtrack(current+')',opend,closed+1)

    backtrack("",0,0)

    return result

print(valid_parentheses(2))