'''
Tower of Hanoi 

https://www.mathsisfun.com/games/towerofhanoi.html

=> always remember the n=3 tower how you move it that's the solution

2n-1 moves required

'''

def tower_hanoi(N,A,B,C):

    if N==1:
        print(f'move {N} from {A} to {C}')
        return 
    
    tower_hanoi(N-1,A,C,B)

    print(f'Move {N} from {A} to {C}') # largest disk 

    tower_hanoi(N-1,B,A,C)  # we make this to move largest disk here 

tower_hanoi(3,"a","b","c")