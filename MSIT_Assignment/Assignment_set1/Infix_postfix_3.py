PRECEDENCE = {'+':1,'-':1,'*':2,'/':2,'^':3}
OPERATORS = ['+','-','*','/','^']
stack = []
output = []
present_number = 0
expression = '23*53-12'
for ch in expression:
    if ch in PRECEDENCE:
        output.append(present_number)
        present_number = 0

        while stack and PRECEDENCE[stack[-1]]>PRECEDENCE[ch]:
            output.append(stack.pop())
        stack.append(ch)
            
    else:
        present_number = (present_number*10)+int(ch)
        
stack.append(present_number)

while stack:
    output.append(stack.pop())

print(output)
