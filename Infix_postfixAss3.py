expression = '23+55-12'
stack, present_number = [], 0
precedence = {'*': 2, '/': 2, '+': 1, '-': 1}
output = []
for i in expression:
    if i in precedence:
        output.append(present_number)
        present_number = 0

        while stack and precedence[stack[-1]] > precedence[i]:
            output.append(stack.pop())

        stack.append(i)
    else:
        present_number = (present_number * 10) + int(i)

stack.append(present_number)

while stack:
    output.append(stack.pop())

print(output)
