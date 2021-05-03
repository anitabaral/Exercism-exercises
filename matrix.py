class Matrix:
    coloumns = []
    def __init__(self, matrix_string):
        self.matrix = [[int(item) for item in row.split(' ')] for row in matrix_string.split('\n')]


    # def matrix_here(self):
    #     return self.matrix[:]

    def row(self, index):
        return self.matrix[index-1]

.
    def column(self, index):
        return[[row[i] for row in self.matrix] for i in range (index)][index-1]


# matrix = Matrix('''9 8 7
# 6 5 4
# 3 2 1''')
# print(matrix.matrix_here())
# print(matrix.column(3))
# print(matrix.row(3))
