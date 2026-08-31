
class Array1D:
    def __init__(self):
        self.arr = []

    # Insert at a given position (1-based)
    def insert(self, value, pos):
        if pos < 1 or pos > len(self.arr) + 1:
            print("Invalid position!")
            return

        self.arr.insert(pos - 1, value)
        print("Element inserted successfully.")

    # Delete from a given position
    def delete(self, pos):
        if pos < 1 or pos > len(self.arr):
            print("Invalid position!")
            return

        removed = self.arr.pop(pos - 1)
        print("Deleted element:", removed)

    # Search an element
    def search(self, value):
        positions = [
            i + 1 for i, x in enumerate(self.arr)
            if x == value
        ]

        if positions:
            print("Element found at position(s):", positions)
        else:
            print("Element not found.")

    # Rotate left by k positions
    def rotate_left(self, k):
        n = len(self.arr)

        if n == 0:
            print("Array is empty.")
            return

        k %= n
        self.arr = self.arr[k:] + self.arr[:k]
        print("Array rotated left successfully.")

    # Rotate right by k positions
    def rotate_right(self, k):
        n = len(self.arr)

        if n == 0:
            print("Array is empty.")
            return

        k %= n
        self.arr = self.arr[-k:] + self.arr[:-k] if k else self.arr[:]
        print("Array rotated right successfully.")

    # Display array
    def display(self):
        print("Array:", self.arr if self.arr else "Empty")


def main():
    a = Array1D()

    n = int(input("Enter number of elements: "))

    if n < 0:
        print("Invalid size!")
        return

    for i in range(n):
        value = int(input("Enter element: "))
        a.insert(value, i + 1)

    while True:
        print("\n===== 1D ARRAY OPERATIONS =====")
        print("1. Insert")
        print("2. Delete")
        print("3. Search")
        print("4. Rotate Left")
        print("5. Rotate Right")
        print("6. Display")
        print("7. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            value = int(input("Enter value: "))
            pos = int(input("Enter position: "))
            a.insert(value, pos)

        elif choice == 2:
            pos = int(input("Enter position: "))
            a.delete(pos)

        elif choice == 3:
            value = int(input("Enter value to search: "))
            a.search(value)

        elif choice == 4:
            k = int(input("Enter rotations: "))
            a.rotate_left(k)

        elif choice == 5:
            k = int(input("Enter rotations: "))
            a.rotate_right(k)

        elif choice == 6:
            a.display()

        elif choice == 7:
            print("Program terminated.")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
