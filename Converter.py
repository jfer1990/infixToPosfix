from Stack import Stack

#-----predicate functions-----
def isOperator(char):
    return True if char == '+'or char == '-'or char == '*' or char == '/'or char == '^'or char == '(' or char == '{' or char == '[' else False
def isClosure(char):
    return True if char == ')' or char =='}' or char == ']' else False

#-----------------------

def f(stack, operator, output):
    precedenceRule = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '(': 4, '{': 4, '[': 4}
    op = precedenceRule.get(operator)
    if stack.__len__() == 0:
        stack.push(operator)
    else:
        if stack.peek() == '(' or stack.peek() == '{' or stack.peek() == '[':
            if not isClosure(operator):
                stack.push(operator)
        else:
            if isClosure(operator):
                if operator == ')':
                    if stack.peek() != '(':
                        output.append(stack.pop())
                        f(stack,operator,output)
                if operator == ']':
                    if stack.peek() != '[':
                        output.append(stack.pop())
                        f(stack, operator, output)
                if operator == '}':
                    if stack.peek() != '{':
                        output.append(stack.pop())
                        f(stack, operator, output)

                stack.pop()  # limpia el stack del parentesis de apertura
            else:
                comparator = precedenceRule.get(stack.top())
                print("aqui"+str(stack.top()))
                if op > comparator:
                    stack.push(operator)
                else:
                    output.append(stack.pop())
                    f(stack,operator,output)

def infixToPosfix(statement):
    stack = Stack()
    output = []
    precedenceRule = {'+':1,'-':1,'*':2,'/':2,'^':3,'(':4,'{':4,'[':4}
    for char in statement:
        if isOperator(char):
            f(stack,char,output)
        if isClosure(char):
            f(stack, char, output)
        if not isOperator(char) and not isClosure(char):
            output.append(char)
    for i in range(len(stack)):
        output.append(stack.pop())

    return output

expression = "3x*2/(3-5)*4"
posfix = infixToPosfix(expression)
print (posfix)



