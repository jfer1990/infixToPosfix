def isOperator(char):
    return True if char == '+'or char == '-'or char == '*' or char == '/'or char == '^'or char == '(' or char == '{' or char == '[' or char == '=' or char =='>' or char == '<' or char == '%' else False
def isClosure(char):
    return True if char == ')' or char =='}' or char == ']' else False
def isOperand(char):
    if not isOperator(char) and not isClosure(char):
        return True
    else:
        return False

