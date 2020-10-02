OPERATORS = ['+', '-', '*', '/', '^']
PRIORITY = {'+':1, '-':1, '*':2, '/':2, '^':3}
stack = []
output = ''
expression='a+b*c-d'
for ch in expression:
    if ch not in OPERATORS:
        output=output+ch
    else:
        while stack and PRIORITY[ch]<=PRIORITY[stack[-1]]:
            output+=stack.pop()
        stack.append(ch)
        
while stack:
    output=output+stack.pop()

print(output)
