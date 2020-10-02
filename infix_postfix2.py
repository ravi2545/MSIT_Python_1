import re
stack = []
OPERATORS = ['+', '-', '*', '/', '^']
PRIORITY = {'+':1, '-':1, '*':2, '/':2}
NUMBER = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
output = ''
expression='a+b*c-d'
postfix = []
#'x*y+z'
#'x+y*z'
for ch in expression:
    if ch not in OPERATORS:
        output=output+ch
    else:
        if stack and PRIORITY[ch]<=PRIORITY[stack[-1]]:
            output+=stack.pop()
        stack.append(ch)
        
while stack:
    output+=stack.pop()

for line in output:
    if line in NUMBER:
        n = int(line)
        postfix.append(n)
    else:
        postfix.append(line)

print(postfix)

