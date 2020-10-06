def Matrix(number_of_rows, number_of_columns, fill_with=0):
    l = [[fill_with for i in range(number_of_columns)]]*number_of_rows
    return l

def Add(m1, row, column, ch):
    if row==1 and column==1:
        row=0
        column=0
    else:
        row-=1
        column-=1

    empty = []
    for item in m1[row]:
        empty.append(item)
    empty[column] = ch
    m1[row] = empty
    return m1


def Get_value(m1, row, column):
    list = []
    if row==1 and column==1:
        row = 0
        column = 0
    else:
        row-=1
        column-=1
    for index in m1[row]:
        list.append(index)
    value = list[column]
    return value

number_of_rows = 2
number_of_columns = 3
m1 = Matrix(number_of_rows, number_of_columns, fill_with=0)
m2 = Add(m1,row = 1, column = 1, ch = 9)
m3 = Get_value(m1, row = 1, column = 1)
print(m3)

























# class Matrix:
#     def __init__(self, number_of_rows, number_of_columns, fill_with):
#         self.number_of_rows = number_of_rows
#         self.number_of_columns = number_of_columns
#         self.fill_with = fill_with


# def Matrix(m,n,fill_with):
#     mat = [ [ fill_with for i in range(n) ] for j in range(m) ]
#     return mat
#
# def Matrix2(m,n,fill_with):
#     mat = [[fill_with for i in range(n)]]*m
#     return mat
#
#
#
#
#
# number_of_rows = 2
# number_of_columns = 3
#
# #p = Matrix(number_of_rows, number_of_columns, fill_with=9)
# #print(p)
# print(Matrix2(number_of_rows,number_of_columns, fill_with=0))


# r = 2
# c = 3
# f = 8
# ch = 9
# emp = []
# l = [[f for i in range(1,c+1)]]*r
# print(l)
#
# for j in l[0]:
#     emp.append(j)
# emp[0] = ch
#
# l[0]=emp
# print(l)