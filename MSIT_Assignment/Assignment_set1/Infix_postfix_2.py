OPERATORS = ['+', '-', '*', '/', '^']
PRECEDENCE = {'+':1, '-':1, '*':2, '/':2, '^':3}
NUMBERS = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
stack = []
output = ''
expression = '2+3*4-5'
postfix = []
for n in expression:
    if n not in OPERATORS:
        output+=n
    else:
        while stack and PRECEDENCE[n]<=PRECEDENCE[stack[-1]]:
            output+=stack.pop()
        stack.append(n)

while stack:
    output+=stack.pop()

for number in output:
    if number in NUMBERS:
        temp = int(number)
        postfix.append(temp)
    else:
        postfix.append(number)

print(postfix)
    
