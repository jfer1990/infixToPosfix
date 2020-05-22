from model.predicates import isOperand, isOperator
from model.Stack import Stack
def getLiteral(exp):
    if len(exp)>0 and isOperand(exp[0]):
        return str(exp[0])+getLiteral(exp[1:])
    return ""


#precondicion: debe recibir una exp válida infija sin espacios
def evaluatePosfix(exp):
    stack = Stack()
    op = {'+': lambda x, y: x + y,
          '-': lambda x, y: x - y,
          '*': lambda x, y: x * y,
          '/': lambda x, y: x / y,
          '^': lambda x, y: x**y,
          '%': lambda x, y: x % y,
          '>': lambda x, y: True if x>y else False,
          '<': lambda x, y: True if x<y else False,
          '=': lambda x, y: True if x == y else False}
    for element in exp:
        if isOperand(element):
            stack.push(element)
        if isOperator(element):
            y = float(stack.pop())
            x = float(stack.pop())
            x = op[element](x,y)
            stack.push(x)
    return stack.pop()
