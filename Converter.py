from Stack import Stack
import recursiveStack
import predicates as P




def infixToPosfix(statement):
    stack = Stack()
    output = []
    precedenceRule = {'+':1,'-':1,'*':2,'/':2,'^':3,'(':4,'{':4,'[':4}
    for char in statement:
        if P.isOperator(char):
            recursiveStack.f(stack,char,output)
        if P.isClosure(char):
            recursiveStack.f(stack, char, output)
        if not P.isOperator(char) and not P.isClosure(char):
            output.append(char)
    for i in range(len(stack)):
        output.append(stack.pop())

    return output

expression = "3x*2/(3-5)*4"
posfix = infixToPosfix(expression)
print (posfix)



