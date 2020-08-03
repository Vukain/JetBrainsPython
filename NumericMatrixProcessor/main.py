class Matrix:

    def __init__(self):
        self.rows, self.columns = input().split()

    def create(self):
        self.matrix = [[float(n) for n in input().split()] for _row in range(int(self.rows))]

    def add(self, mtx):
        if self.rows == mtx.rows and self.columns == mtx.columns:
            result = [[self.matrix[i][j] + mtx.matrix[i][j] for j in range(len(self.matrix[0]))] for i in
                      range(len(self.matrix))]
            for row in result:
                for number in row:
                    print(number, end=" ")
                print()
        else:
            print("ERROR")

    def multiply(self, number):
        result = [[self.matrix[i][j] * number for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
        for row in result:
            for number in row:
                print(int(number), end=" ")
            print()

    def transpose(self):
        transposed = [[self.matrix[i][j] for i in range(len(self.matrix))] for j in range(len(self.matrix[0]))]
        self.matrix = transposed

    def transpose_side(self):
        transposed = [[self.matrix[i][j] for i in range(-1, -len(self.matrix) - 1, -1)] for j in
                      range(-1, -len(self.matrix[0]) - 1, -1)]
        self.matrix = transposed

    def transpose_vertical(self):
        for row in self.matrix:
            row.reverse()

    def transpose_horizontal(self):
        self.matrix.reverse()

    def printer(self):
        for row in self.matrix:
            for number in row:
                print(int(number), end=" ")
            print()

    def multiply_matrices(self, mtx):
        if self.columns != mtx.rows:
            print("The operation cannot be performed.")
        else:
            result = [[sum([self.matrix[i][k] * mtx.matrix[j][k] for k in range(len(mtx.matrix[0]))]) for j in
                       range(len(mtx.matrix))] for i in range(len(self.matrix))]

            for row in result:
                for number in row:
                    print(round(number, 2), end=" ")
                print()
                
    def determinant(self, mtx):
        determinant = 0
        if len(mtx.matrix[0]) == 2:
            det = mtx[0][0] * mtx[1][1] - mtx[1][0] * mtx[0][1]
        else:
            eva = "-"
            recur = ""
            for i, e in enumerate(mtx):
                recur += mtx[0][i] * determinant([e for e in i, e in enumerate(mtx[1:] if i != 0)])
                recur += eva
                if eva == '-':
                    eva = "+"
                else:
                    eva = "-"
            return eval(recur)
            
        


def menu():
    while True:
        print("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n4. Transpose matrix\n0. Exit")
        choice = input()
        if choice == "1":
            print("Enter size of first matrix: ")
            matrix_a = Matrix()
            print("Enter first matrix: ")
            matrix_a.create()

            print("Enter size of second matrix: ")
            matrix_b = Matrix()
            print("Enter second matrix: ")
            matrix_b.create()

            print("The result is:")
            matrix_a.add(matrix_b)

        elif choice == "2":
            print("Enter size of matrix: ")
            matrix_a = Matrix()
            print("Enter matrix: ")
            matrix_a.create()

            const = int(input("Enter constant: "))
            print("The result is:")
            matrix_a.multiply(const)

        elif choice == "3":
            print("Enter size of first matrix: ")
            matrix_a = Matrix()
            print("Enter first matrix: ")
            matrix_a.create()

            print("Enter size of second matrix: ")
            matrix_b = Matrix()
            print("Enter second matrix: ")
            matrix_b.create()
            matrix_b.transpose()
            # print(matrix_b.matrix)
            print("The result is:")
            matrix_a.multiply_matrices(matrix_b)

        elif choice == "4":
            print('1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line')
            tran_choice = input("Your choice: ")
            print("Enter size of matrix: ")
            matrix_a = Matrix()
            print("Enter matrix: ")
            matrix_a.create()
            if tran_choice == "1":
                matrix_a.transpose()
            elif tran_choice == "2":
                matrix_a.transpose_side()
            elif tran_choice == "3":
                matrix_a.transpose_vertical()
            elif tran_choice == "4":
                matrix_a.transpose_horizontal()

            matrix_a.printer()
            
        elif choice == "5":
            print("Enter size of matrix: ")
            matrix_a = Matrix()
            print("Enter matrix: ")
            matrix_a.create()
            
            matrix_a.determinant(matrix_a.matrix)
        else:
            break


menu()
