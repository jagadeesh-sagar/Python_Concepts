'''
Check if string has balanced parentheses - "(())" → True, "(()" → False

⚡ Pro Tip

If you hear:

"nested"
"matching"
"undo"
"previous element"

👉 Think STACK immediately

'''


def parentheses_balanced(string1:str)->bool:
    if string1=='':
        return True

    opened=0
    for i in string1:
        if i=="(":
            opened+=1
        elif i==")"and opened==0:
            return False
        elif i==")":
             opened-=1

    return opened==0


if (parentheses_balanced(string1='()(()())')):
    print('balanced parenthesis')
else:
    print('not balanced parenthesis')

def parentheses_stack(string1:str):
    parentheses_maping={")":"(","]":"[","}":"{"}
    stack:list=[]
    if string1=='':
        return True
    for i in string1:
        if len(stack)==0 and parentheses_maping.get(i):
            return False
        elif len(stack)==0:
            stack.append(i)
        elif stack[-1]==parentheses_maping.get(i):
            stack.pop()
        elif not parentheses_maping.get(i):
            stack.append(i)
        elif parentheses_maping.get(i):
            return False
    return len(stack)==0

if (parentheses_stack(string1='([}])')):
    print('balanced parenthesis')
else:
    print('not balanced parenthesis')

def parentheses_stack_2(string1:str)->bool:
    mapping={")":"(","]":"[","}":"{"}
    stack=[]

    for ch in string1:
        if ch in mapping:
            if not stack or stack[-1]!=mapping[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)
    return len(stack)==0

if (parentheses_stack_2(string1="([])")):
    print('balanced parenthesis')
else:
    print('not balanced parenthesis')
# ///////////////////////////////////////////////////////////////