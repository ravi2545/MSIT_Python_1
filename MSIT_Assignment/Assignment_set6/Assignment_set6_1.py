def Matrix(number_of_rows, number_of_columns, fill_with=0):
    l = [[fill_with for i in range(number_of_columns)]] * number_of_rows
    return l


def Add(m1, row, column, ch):
    if row == 1 and column == 1:
        row = 0
        column = 0
    else:
        row -= 1
        column -= 1

    empty = []
    for item in m1[row]:
        empty.append(item)
    empty[column] = ch
    m1[row] = empty
    return m1


def Get_value(m1, row, column):
    list = []
    if row == 1 and column == 1:
        row = 0
        column = 0
    else:
        row -= 1
        column -= 1
    for index in m1[row]:
        list.append(index)
    value = list[column]
    return value


def get_shape(m1):
    row = len(m1)
    column = 0,
    for c in range(len(m1)):
        column = len(m1[c])
    return row, column


def equl(m1, m2):
    if len(m1) == len(m2):
        if m1 == m2:
            return True
        else:
            return False


def isSquare(m1):
    result = get_shape(m1)
    if result[0] == result[1]:
        return True
    else:
        return False


def isDiagonal(m1):
    result = get_shape(m1)
    row = result[0]
    col = result[1]
    if row == col:
        for ro in range(0, row):
            for col in range(0, col):
                if ((ro != col) and (m1[ro][col])):
                    return False
        return True


def add(m1, m2):
    res = [[0, 0], [0, 0]]
    for data in range(len(m1)):
        for col in range(len(m1[0])):
            res[data][col] = m1[data][col] + m2[data][col]
    return res


def Multi(m1, m2):
    result = [[0 for x in range(2)] for y in range(2)]
    for row in range(len(m1)):
        for col in range(len(m2[0])):
            for k in range(len(m2)):
                result[row][col] += m1[row][k] * m2[k][col]
    return result


def removeRowColumn(m1, row_number, column_number):
    if row_number == 1 and column_number == 1:
        row_number = 0
        column_number = 0
    else:
        row_number -= 1
        column_number -= 1
    del m1[row_number]
    for c in m1:
        del c[column_number]
    return m1


def transpose(m1):
    result = [[0, 0], [0, 0]]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            result[i][j] = m1[j][i]
    return result

# ---------------------------------------------------------
# number_of_rows = 2
# number_of_columns = 3
# -------------------------------------------------------------
# m1 = Matrix(number_of_rows, number_of_columns, fill_with=0)
# m2 = Add(m1, row=1, column=1, ch=9)
# m3 = Get_value(m1, row=1, column=1)
# m4 = get_shape(m1)
# ------------------------------------------------------------
# m1 = [[0,0,0],[0,0,0]]
# m2 = [[0,0,0],[0,0,1]]
# m6 = equl(m1, m2)
# print(m6)
# ------------------------------------------------------------
# m7 = isSquare(m1)
# print(m7)
# -----------------------------------------------------------
# m1 = [[1,0,1],[0,1,0],[0,0,1]]
# m8 = isDiagonal(m1)
# print(m8)
# --------------------------------------------------------
# m1 = [[1,2],[3,4]]
# m2 = [[5,6],[7,8]]
# m9 = Matrix_Addition(m1, m2)
# print(m9)
# ----------------------------------------------------
# m1 = [[1,2],[3,1]]
# print(dia(m1))
# ---------------------------------------------------------
# m1 = [[1,2],[1,2]]
# m2 = [[3,4],[5,6]]
# print(add(m1,m2))
# ------------------------------------------------------
# m1 = [[1,2],[3,4]]
# m2 = [[5,6],[7,8]]
# print(Multi(m1, m2))
# -----------------------------------------------------
# m1 = [[1,2,3],[4,5,6],[7,8,9]]
# row = 2
# col = 2
# print(removeRowColumn(m1, row, col))
# -------------------------------------------------
# m1 = [[1,2],[3,4]]
# print(transpose(m1))


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
