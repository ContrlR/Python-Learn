class Matrix:

    def menu(self):
        import sys

        print()
        print('1. Add matrices')
        print("2. Multiply matrix by a constant")
        print('3. Multiply matrices')
        print('4. Transpose matrix')
        print('5. Calculate a determinant')
        print('6. Inverse Matrix')
        print('0. Exit')
        choice = input('Your choice: ')
        if choice == '1':
            self.add()
        elif choice == '2':
            self.scalar()
        elif choice == '3':
            self.multiply()
        elif choice == '4':
            self.transpose()
        elif choice == '5':
            self.determinant()
        elif choice == '6':
            self.inverse()
        elif choice == '0':
            sys.exit()
        else:
            pass

    @staticmethod
    def printer(result):

        print('The result is:')
        for i in range(len(result)):
            print(*result[i])

    @staticmethod
    def create(x, y):
        m_create = [[int(i) if i.isdigit() else float(i) for i in input().split()] for _ in range(int(x))]
        return m_create

    @staticmethod
    def matrix_minor(m, i, j):
        return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

    def add(self):

        x, y = input('Enter size of first matrix: ').split()
        print('Enter first matrix:')
        m_xy = self.create(x, y)
        a, b = input('Enter size of second matrix: ').split()
        print('Enter second matrix:')
        m_ab = self.create(a, b)

        # Checking if the dimensions meet requirements
        if x == a and y == b:
            self.printer([[m_xy[i][j] + m_ab[i][j] for j in range(int(y))] for i in range(int(x))])
        else:
            print('The operation cannot be performed.')

    def scalar(self):

        x, y = input('Enter size of matrix: ').split()
        print('Enter matrix:')
        m_xy = self.create(x, y)
        scalar = input('Enter constant: ')
        if '.' in scalar:
            scalar = float(scalar)
        else:
            scalar = int(scalar)
        self.printer([[m_xy[i][j] * scalar for j in range(int(y))] for i in range(int(x))])

    def multiply(self):

        x, y = input('Enter size of first matrix: ').split()
        print('Enter first matrix:')
        m_xy = self.create(x, y)
        a, b = input('Enter size of second matrix: ').split()
        print('Enter second matrix:')
        m_ab = self.create(a, b)

        # Checking if the dimensions meet requirements
        if y == a:
            result = []
            for i in range(int(x)):
                row = []
                for j in range(int(b)):
                    cell = 0
                    for k in range(int(a)):
                        cell += m_xy[i][k] * m_ab[k][j]
                    row.append(cell)
                result.append(row)
            self.printer(result)
        else:
            print('The operation cannot be performed.')

    def transpose(self, menu=0, m_xy=[], choice=0):
        
        if menu == 0:
            # Transpose menu
            print('1. Main diagonal')
            print('2. Side diagonal')
            print('3. Vertical line')
            print('4. Horizontal line')
            choice = input('Your choice: ')
            x, y = input('Enter size of matrix: ').split()
            print('Enter matrix:')
            m_xy = self.create(x, y)
            menu = 1

        if menu == 1:   
            if choice == '1':
                self.printer([[m_xy[j][i] for j in range(len(m_xy[0]))] for i in range(len(m_xy))])
            elif choice == '2':
                self.printer([[m_xy[-j-1][-i-1] for j in range(len(m_xy[0]))] for i in range(len(m_xy))])
            elif choice == '3':
                self.printer([[m_xy[i][-j-1] for j in range(len(m_xy[0]))] for i in range(len(m_xy))])
            elif choice == '4':
                self.printer([[m_xy[-i-1][j] for j in range(len(m_xy[0]))] for i in range(len(m_xy))])
            if choice == '5':
                return [[m_xy[j][i] for j in range(len(m_xy[0]))] for i in range(len(m_xy))]

    def determinant(self, d_mat=None):

        # Original Case
        if d_mat is None:
            x, y = input('Enter size of matrix: ').split()
            print('Enter matrix:')
            m_xy = self.create(x, y)
            print('The result is:')
            print(self.determinant(m_xy))

        # Base Case
        elif len(d_mat) == 2:
            return (d_mat[0][0] * d_mat[1][1]) - (d_mat[0][1] * d_mat[1][0])
        elif len(d_mat) == 1:
            return d_mat[0][0]
        # Recursive Case
        else:
            determinant = 0
            for c in range(len(d_mat)):
                determinant += ((-1)**c)*d_mat[0][c]*self.determinant(self.matrix_minor(d_mat, 0, c))
            return determinant

    def inverse(self):
        
        x, y = input('Enter size of matrix: ').split()
        print('Enter matrix:')
        m = self.create(x, y)

        determinant = self.determinant(m)
        # special case for 2x2 matrix:
        if len(m) == 2:
            return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                    [-1*m[1][0]/determinant, m[0][0]/determinant]]

        cofactors = []
        for r in range(len(m)):
            cofactor_row = []
            for c in range(len(m)):
                minor = self.matrix_minor(m, r, c)
                cofactor_row.append(((-1)**(r+c)) * self.determinant(minor))
            cofactors.append(cofactor_row)
        cofactors = self.transpose(menu=1, m_xy=cofactors, choice='5')
        for r in range(int(x)):
            for c in range(int(x)):
                cofactors[r][c] = cofactors[r][c]/determinant
        self.printer(cofactors)


def main():
    power = Matrix()
    while True:
        power.menu()


if __name__ == '__main__':
    main()
