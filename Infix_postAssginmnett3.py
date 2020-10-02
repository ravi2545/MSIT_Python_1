import re 
stack = []#I am taking list for stack
OPERATORS = ['+', '-', '*', '/', '^'] #I am taking operators
PRIORITY = {'+':1, '-':1, '*':2, '/':2} #PRIORITY operator
NUMBER = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
expression='23*55-12' #Input
output = ''  #output
postfix = [] #Saving output Result in the list(Name postfix)
#'x*y+z'
#'x+y*z'
for ch in expression:
    if ch not in OPERATORS:
        output=output+ch
    else:
        output=output+','
        if stack and PRIORITY[ch]<=PRIORITY[stack[-1]]:
            output+=stack.pop()
        stack.append(ch)
        
while stack:
    output+=stack.pop()

print(output)
    
