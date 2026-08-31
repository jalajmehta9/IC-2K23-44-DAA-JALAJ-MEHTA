
class Array2D:
    def __init__(self, rows, cols):
        self.matrix = []
        self.rows = rows
        self.cols = cols

    # Input matrix
    def input_matrix(self):
        print("Enter matrix elements:")

        for i in range(self.rows):
            row = []

            for j in range(self.cols):
                value = int(input(f"Element [{i+1}][{j+1}]: "))
                row.append(value)

            self.matrix.append(row)

    # Insert a row (1-based position)
    def insert_row(self, pos):
        if pos < 1 or pos > self.rows + 1:
            print("Invalid position!")
            return

        new_row = []

        print(f"Enter {self.cols} elements:")

        for j in range(self.cols):
            new_row.append(int(input(f"Column {j+1}: ")))

        self.matrix.insert(pos - 1, new_row)
        self.rows += 1

        print("Row inserted successfully.")

    # Delete a row
    def delete_row(self, pos):
        if pos < 1 or pos > self.rows:
            print("Invalid position!")
            return

        self.matrix.pop(pos - 1)
        self.rows -= 1

        print("Row deleted successfully.")

    # Insert a column
    def insert_column(self, pos):
        if pos < 1 or pos > self.cols + 1:
            print("Invalid position!")
            return

        print(f"Enter {self.rows} elements:")

        for i in range(self.rows):
            value = int(input(f"Row {i+1}: "))
            self.matrix[i].insert(pos - 1, value)

        self.cols += 1
        print("Column inserted successfully.")

    # Delete a column
    def delete_column(self, pos):
        if pos < 1 or pos > self.cols:
            print("Invalid position!")
            return

        for i in range(self.rows):
            self.matrix[i].pop(pos - 1)

        self.cols -= 1
        print("Column deleted successfully.")

    # Search an element
    def search(self, value):
        found = False

        for i in range(self.rows):
            for j in range(self.cols):
                if self.matrix[i][j] == value:
                    print(
                        f"Element found at Row {i+1}, "
                        f"Column {j+1}"
                    )
                    found = True

        if not found:
            print("Element not found.")

    # Rotate matrix 90 degrees clockwise
    def rotate_clockwise(self):
        self.matrix = [
            list(row) for row in zip(*self.matrix[::-1])
        ]

        self.rows, self.cols = self.cols, self.rows

        print("Matrix rotated 90 degrees clockwise.")

    # Display matrix
    def display(self):
        if self.rows == 0 or self.cols == 0:
            print("Matrix is empty.")
            return

        print("\nMatrix:")

        for row in self.matrix:
            print(*row)


def main():
    r = int(input("Enter number of rows: "))
    c = int(input("Enter number of columns: "))

    if r <= 0 or c <= 0:
        print("Invalid matrix dimensions!")
        return

    a = Array2D(r, c)
    a.input_matrix()

    while True:
        print("\n===== 2D ARRAY OPERATIONS =====")
        print("1. Insert Row")
        print("2. Delete Row")
        print("3. Insert Column")
        print("4. Delete Column")
        print("5. Search Element")
        print("6. Rotate 90 Degrees Clockwise")
        print("7. Display Matrix")
        print("8. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            pos = int(input("Enter row position: "))
            a.insert_row(pos)

        elif choice == 2:
            pos = int(input("Enter row position: "))
            a.delete_row(pos)

        elif choice == 3:
            pos = int(input("Enter column position: "))
            a.insert_column(pos)

        elif choice == 4:
            pos = int(input("Enter column position: "))
            a.delete_column(pos)

        elif choice == 5:
            value = int(input("Enter value to search: "))
            a.search(value)

        elif choice == 6:
            a.rotate_clockwise()

        elif choice == 7:
            a.display()

        elif choice == 8:
            print("Program terminated.")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
