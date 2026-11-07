'''
24. Basic Calculator

Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:
Input: s = "1 + 1"
Output: 2

Example 2:
Input: s = " 2-1 + 2 "
Output: 3

Example 3:
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23

'''

def calculate(s:int):
    result=0
    number=0
    stack=[]
    sign=1

    for ch in s:
        if (ch.isdigit()):
            number=number*10+int(ch)

        elif ch=="+":
            result+=sign*number
            number=0
            sign=1

        elif ch=="-":
            result+=sign*number
            number=0
            sign=-1

        elif ch=='(': 
            # result+=sign*number
            stack.append(result)
            stack.append(sign)

            result=0
            sign=1

        elif ch==")":
            result+=sign*number
            number=0

            prev_sign=stack.pop()
            prev_result=stack.pop()

            result=prev_result+prev_sign*result

        # print(result,number,ch,stack)

    result += sign * number

    return result

# print(calculate("1+2+(1+2)"))

'''
227. Basic Calculator II

Given a string s which represents an expression, evaluate this expression and return its value. 
The integer division should truncate toward zero.
You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:
Input: s = "3+2*2"
Output: 7

Example 2:
Input: s = " 3/2 "
Output: 1

Example 3:
Input: s = " 3+5 / 2 "
Output: 5
'''

def calculator2(s: str):

    stack=[]
    # =0
    sign='+'
    number=0

    for i,ch in enumerate(s):

        if ch.isdigit():
            number=number*10+int(ch)         
    
        if (not ch.isdigit() and ch != " ") or i == len(s) - 1:

            if sign =="+":
                stack.append(number)

            elif sign =="-":
                stack.append(-number)

            elif sign=="/":
                stack.append(int(stack.pop()/number))

            elif sign == "*":
                stack.append(stack.pop()*number)

            number=0
            sign=ch
                
    return sum(stack)

print(calculator2(s="9/3"))

'''
s = "10+(2*3)"

'''

def calculator3(s:str):

    stack=[]
    number=0
    sign='+'

    for ch in s:

        if ch.isdigit():
            number=number*10+int(ch)

        elif ch=="(":
            stack.append(number)
            stack.append(sign)

        elif ch==")":
            current_result=stack.pop()
            prev_sign=stack.pop()
            # prev_sign=


        elif not ch.isdigit() and ch!=' ':

            if sign =="+":
                stack.append(number)

            elif sign =="-":
                stack.append(-number)

            elif sign=="/":
                stack.append(int(stack.pop()/number))

            elif sign == "*":
                stack.append(stack.pop()*number)

            number=0
            sign=ch

    return sum(stack)
            

class Solution:
    def calculate(self, s: str) -> int:

        def helper():

            stack = []
            num = 0
            sign = '+'

            while self.i < len(s):

                ch = s[self.i]

                if ch.isdigit():
                    num = num * 10 + int(ch)

                if ch == '(':
                    self.i += 1
                    num = helper()

                if (not ch.isdigit() and ch != ' ') or self.i == len(s) - 1:

                    if sign == '+':
                        stack.append(num)

                    elif sign == '-':
                        stack.append(-num)

                    elif sign == '*':
                        stack.append(stack.pop() * num)

                    elif sign == '/':
                        stack.append(int(stack.pop() / num))

                    num = 0
                    sign = ch

                if ch == ')':
                    break

                self.i += 1

            return sum(stack)

        self.i = 0
        return helper()