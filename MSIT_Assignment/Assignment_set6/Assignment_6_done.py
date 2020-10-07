class Matrix:
    def __init__(self, rows, cols, fill_with):
        self.matrix = [[fill_with for i in range(cols)]] * rows

    def set_value(self, mat, set_val):
        rows = 1
        cols = 1
        if rows == 1 and cols == 1:
            rows = 0
            cols = 0
        else:
            rows -= 1
            cols -= 1

        empty = []
        for item in mat[rows]:
            empty.append(item)
        empty[cols] = set_val
        mat[rows] = empty
        return mat

    def Get_value(self, mat, row, column):
        list = []
        if row == 1 and column == 1:
            row = 0
            column = 0
        else:
            row -= 1
            column -= 1
        for index in mat[row]:
            list.append(index)
        value = list[column]
        return value

    def getShape(self, m1):
        row = len(m1)
        column = 0,
        for c in range(len(m1)):
            column = len(m1[c])
        return row, column

    def rows(self):
        rs = self.getShape(self.matrix)
        return rs[0]

    def column(self):
        rs = self.getShape(self.matrix)
        return rs[1]

    def equl(self, m1, m2):
        if len(m1) == len(m2):
            if m1 == m2:
                return True
            else:
                return False

    def isSquare(self, m1):
        result = self.getShape(m1)
        if result[0] == result[1]:
            return True
        else:
            return False

    def isDiagonal(self):
        result = self.getShape(self.matrix)
        row = result[0]
        col = result[1]
        if row == col:
            for ro in range(0, row):
                for col in range(0, col):
                    if ((ro != col) and (self.matrix[ro][col])):
                        return False
            return True

    def Matrix_Addition(self,m1, m2):
        res = [[0, 0], [0, 0]]
        for data in range(len(m1)):
            for col in range(len(m1[0])):
                res[data][col] = m1[data][col] + m2[data][col]
        return res

    def Multi(self,m1, m2):
        result = [[0 for x in range(2)] for y in range(2)]
        for row in range(len(m1)):
            for col in range(len(m2[0])):
                for k in range(len(m2)):
                    result[row][col] += m1[row][k] * m2[k][col]
        return result

    def removeRowColumn(self, m1, row_number, column_number):
        rows = len(m1[row_number])
        cols = 0
        for cl in m1:
            cols = cl[column_number]

        if row_number == 1 and column_number == 1:
            row_number = 0
            column_number = 0
        else:
            row_number -= 1
            column_number -= 1
        del m1[row_number]
        for c in m1:
            del c[column_number]
        return rows,cols

    def transpose(self,m1):
        result = [[0, 0], [0, 0]]
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                result[i][j] = m1[j][i]
        return result



# ------------------------------
# rows = 2
# cols = 2
# fill_with = 0
# m1 = Matrix(rows,cols, fill_with)

# -----------------------------------------
row = 2
col = 2
fill_with = 9
set_val = 9
# ------------------------------------------
m1 = Matrix(row, col, fill_with)
mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6], [7, 8]]
print(m1.set_value(mat1, set_val))
# ------------------------------------------
r = 1
c = 2
print(m1.Get_value(mat1, r, c))
# -----------------------------------------
r1 = 1
c1 = 1
print(m1.Get_value(mat1, r1, c1))
# ------------------------------------------
print(m1.getShape(mat1))
# ------------------------------------------
print("Number of rows", m1.rows())
print("Number of columns", m1.column())
# -------------------------------------------
mat1 = [[1, 3], [1, 2]]
mat2 = [[1, 3], [1, 2]]
print(m1.equl(mat1, mat2))
# -----------------------------------------
mat3 = [[1, 3], [1, 2]]
print(m1.isSquare(mat3))
#-------------------------------------------
#mat = [[1, 3], [1, 2]]
print(m1.isDiagonal())

#----------------** Matrix Operations **--------
m4 = [[1, 3], [1, 2]]
m5 = [[1, 3], [1, 2]]
print(m1.Matrix_Addition(m4,m5))
#---------------------------------------------
print(m1.Multi(m4,m5))
#------------------------------------
row_number = 1
col_number = 1
print(m1.removeRowColumn(row_number,col_number))
#-----------------------------------------------
print(m1.transpose(m5))