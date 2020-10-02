OPERATORS = ['+','-','*','/','^']
PRECEDENCE = {'+':1,'-':1,'*':2,'/':2,'^':3}
stack = []
output = ''
expression = 'a+b*c-d'
for ch in expression:
    if ch not in OPERATORS:
        output+=ch
    else:
        while stack and PRECEDENCE[ch]<=PRECEDENCE[stack[-1]]:
            output+=stack.pop()
        stack.append(ch)

while stack:
    output+=stack.pop()

print(output)
