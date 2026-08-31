
class SparseMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.terms = []

    # Add non-zero element
    def add_term(self, row, col, value):
        if not (0 <= row < self.rows and
                0 <= col < self.cols):
            raise ValueError("Invalid matrix position!")

        if value != 0:
            self.terms.append((row, col, value))

            # Maintain row-major order
            self.terms.sort(key=lambda x: (x[0], x[1]))

    # Convert normal matrix into sparse representation
    @classmethod
    def from_matrix(cls, matrix):
        if not matrix or not matrix[0]:
            raise ValueError("Matrix cannot be empty!")

        rows = len(matrix)
        cols = len(matrix[0])

        if any(len(row) != cols for row in matrix):
            raise ValueError("Matrix must be rectangular!")

        sparse = cls(rows, cols)

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] != 0:
                    sparse.add_term(i, j, matrix[i][j])

        return sparse

    # Display triplet representation
    def display_triplet(self):
        print("\nTriplet Representation:")
        print("Row\tColumn\tValue")

        # Header row
        print(f"{self.rows}\t{self.cols}\t{len(self.terms)}")

        for row, col, value in self.terms:
            print(f"{row+1}\t{col+1}\t{value}")

    # Convert sparse matrix into normal matrix
    def display_matrix(self):
        matrix = [
            [0] * self.cols for _ in range(self.rows)
        ]

        for row, col, value in self.terms:
            matrix[row][col] = value

        print("\nOriginal Matrix:")

        for row in matrix:
            print(*row)

    # Transpose sparse matrix
    def transpose(self):
        result = SparseMatrix(self.cols, self.rows)

        for row, col, value in self.terms:
            result.add_term(col, row, value)

        return result

    # Add two sparse matrices
    def add(self, other):
        if (self.rows != other.rows or
                self.cols != other.cols):
            raise ValueError(
                "Matrix dimensions do not match!"
            )

        result = SparseMatrix(self.rows, self.cols)

        i = 0
        j = 0

        # Merge the two sorted term lists
        while i < len(self.terms) and j < len(other.terms):
            a = self.terms[i]
            b = other.terms[j]

            if a[:2] == b[:2]:
                total = a[2] + b[2]

                if total != 0:
                    result.terms.append(
                        (a[0], a[1], total)
                    )

                i += 1
                j += 1

            elif a[:2] < b[:2]:
                result.terms.append(a)
                i += 1

            else:
                result.terms.append(b)
                j += 1

        # Remaining terms
        result.terms.extend(self.terms[i:])
        result.terms.extend(other.terms[j:])

        return result


def input_matrix(rows, cols):
    matrix = []

    print("Enter matrix elements:")

    for i in range(rows):
        row = []

        for j in range(cols):
            value = int(input(f"Element [{i+1}][{j+1}]: "))
            row.append(value)

        matrix.append(row)

    return matrix


def main():
    r = int(input("Enter rows of first matrix: "))
    c = int(input("Enter columns of first matrix: "))

    if r <= 0 or c <= 0:
        print("Invalid matrix dimensions!")
        return

    matrix1 = input_matrix(r, c)

    A = SparseMatrix.from_matrix(matrix1)

    A.display_matrix()
    A.display_triplet()

    # Transpose
    T = A.transpose()

    print("\nTranspose of Matrix:")
    T.display_matrix()
    T.display_triplet()

    # Input second matrix
    r2 = int(input("\nEnter rows of second matrix: "))
    c2 = int(input("Enter columns of second matrix: "))

    if r2 <= 0 or c2 <= 0:
        print("Invalid matrix dimensions!")
        return

    matrix2 = input_matrix(r2, c2)

    B = SparseMatrix.from_matrix(matrix2)

    B.display_matrix()
    B.display_triplet()

    # Addition
    if r == r2 and c == c2:
        C = A.add(B)

        print("\nResult after Addition:")
        C.display_matrix()
        C.display_triplet()

    else:
        print("\nAddition is not possible!")
        print("Matrix dimensions must be equal.")


if __name__ == "__main__":
    main()
