import predicates as P

def f(stack, operator, output):
    precedenceRule = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '(': 4, '{': 4, '[': 4}
    op = precedenceRule.get(operator)
    if stack.__len__() == 0:
        stack.push(operator)
    else:
        if stack.peek() == '(' or stack.peek() == '{' or stack.peek() == '[':
            if not P.isClosure(operator):
                stack.push(operator)
        else:
            if P.isClosure(operator):
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