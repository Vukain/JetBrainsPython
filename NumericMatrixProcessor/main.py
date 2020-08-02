class Matrix:

    def __init__(self):
        self.rows, self.columns = input().split()

        # print(self.matrix)

    def create(self):
        self.matrix = [[float(n) for n in input().split()] for row in range(int(self.rows))]

    def add(self, mtx):
        if self.rows == mtx.rows and self.columns == mtx.columns:
            result = [[self.matrix[i][j] + mtx.matrix[i][j] for j in range(len(self.matrix[0]))] for i in
                      range(len(self.matrix))]
            # print(result)
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

    def multiply_matrixes(self, mtx):
        if self.columns != mtx.rows:
            print("The operation cannot be performed.")
        else:
            result = [[sum([self.matrix[i][k] * mtx.matrix[j][k] for k in range(len(mtx.matrix[0]))]) for j in
                       range(len(mtx.matrix))] for i in range(len(self.matrix))]
            # print(result)
            for row in result:
                for number in row:
                    print(round(number, 2), end=" ")
                print()


def menu():
    while True:
        print("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n0. Exit")
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
            matrix_a.multiply_matrixes(matrix_b)
        else:
            break


menu()