OPERATORS = ['+', '-', '*', '/', '^']
PRIORITY = {'+':1, '-':1, '*':2, '/':2, '^':3}
stack = []
output = ''
expression='a+b*c-d'
#'x*y+z'
#'x+y*z'
for ch in expression:
    if ch not in OPERATORS:
        output+=ch
    else:
        if stack and PRIORITY[ch]<=PRIORITY[stack[-1]]:
            output=output+stack.pop()
    stack.append(ch)
while stack:
    output+=stack.pop()
    
print(output)


