class Infix:


    def __init__(self, Expression):
        self.Expression = Expression
        self.Operators = ['+','-','*','-','/']
        self.Precedence = {'+':1,'-':1,'*':2,'/':2,'^':3}
        self.Numbers = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        self.Stack = []



    def Infix_Postfix(self):
        output = ''
        for ch in self.Expression:
            if ch not in self.Operators:
                output+=ch
            else:
                while self.Stack and self.Precedence[ch]<=self.Precedence[self.Stack[-1]]:
                    output+=self.Stack.pop()
                self.Stack.append(ch)
        while self.Stack:
            output+=self.Stack.pop()
        return output


    
    def Infix_Postfix_list(self):
        post_fix_list = []
        result = self.Infix_Postfix()
        for data in result:
            if data in self.Numbers:
                temp = int(data)
                post_fix_list.append(temp)
            else:
                post_fix_list.append(data)
                
        print(post_fix_list)


    def Infix_Postfix_compl(self):
        present_number = 0
        output = []
        for ch in self.Expression:
            if ch in self.Precedence:
                output.append(present_number)
                present_number = 0
            
                while self.Stack and self.Precedence[self.Stack[-1]]>self.Precedence[ch]:
                    output.append(self.Stack.pop())
                self.Stack.append(ch)
            else:
                present_number = (present_number*10)+int(ch)
                
        self.Stack.append(present_number)
        while self.Stack:
            output.append(self.Stack.pop())
        print(output)
    



Expression = '23+55*44-56'

Inob = Infix(Expression)
#Inob.Infix_Postfix()
#Inob.Infix_Postfix_list()
Inob.Infix_Postfix_compl()
