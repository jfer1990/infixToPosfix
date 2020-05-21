from model.Stack import Stack
from model import predicates  as P, recursiveInfixToPosfix
from model.evaluatePosfix import evaluatePosfix




def infixToPosfix(exp):
    exp = exp.replace(" ", "")
    stack = Stack()
    output = []
    while len(exp)>0:
        char = exp[0]
        if P.isOperator(char):
            recursiveInfixToPosfix.f(stack, char, output)
            exp = exp[1:]
        if P.isClosure(char):
            recursiveInfixToPosfix.f(stack, char, output)
            exp = exp[1:]
        if P.isOperand(char):
            var =""
            while P.isOperand(exp[0]) :
                var = var + exp[0]
                exp = exp[1:]
                if len(exp) <= 0: # si no se pone un break, el while de la linea 21 va a fallar evaluando.
                    break
            output.append(var)


    for i in range(len(stack)):
        if stack.peek()!='(' and stack.peek()!='{' and stack.peek()!='[':
            output.append(stack.pop())

    return output

def isInfixValid(exp):
    pass #falta implementacion



