
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at a given position
    def insert(self, data, pos):
        if pos < 1:
            print("Invalid position")
            return

        new_node = Node(data)

        if self.head is None:
            if pos != 1:
                print("Position out of range")
                return

            new_node.next = new_node
            self.head = new_node
            return

        if pos == 1:
            last = self.head

            while last.next != self.head:
                last = last.next

            new_node.next = self.head
            last.next = new_node
            self.head = new_node
            return

        temp = self.head

        for _ in range(pos - 2):
            temp = temp.next

            if temp == self.head:
                print("Position out of range")
                return

        new_node.next = temp.next
        temp.next = new_node

    # Delete from a given position
    def delete(self, pos):
        if self.head is None or pos < 1:
            print("List is empty or position is invalid")
            return

        if pos == 1:
            if self.head.next == self.head:
                self.head = None
                return

            last = self.head

            while last.next != self.head:
                last = last.next

            last.next = self.head.next
            self.head = self.head.next
            return

        temp = self.head

        for _ in range(pos - 2):
            temp = temp.next

            if temp.next == self.head:
                print("Position out of range")
                return

        if temp.next == self.head:
            print("Position out of range")
            return

        temp.next = temp.next.next

    # Reverse the circular linked list
    def reverse(self):
        if self.head is None or self.head.next == self.head:
            return

        prev = None
        current = self.head
        old_head = self.head

        while True:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

            if current == old_head:
                break

        old_head.next = prev
        self.head = prev

    # Convert circular list into Python list
    def to_list(self):
        values = []

        if self.head is None:
            return values

        temp = self.head

        while True:
            values.append(temp.data)
            temp = temp.next

            if temp == self.head:
                break

        return values

    # Concatenate two circular linked lists
    def concatenate(self, other):
        result = CircularLinkedList()

        for value in self.to_list() + other.to_list():
            result.insert(value, len(result.to_list()) + 1)

        return result

    # Display linked list
    def display(self):
        values = self.to_list()

        if values:
            print(" -> ".join(map(str, values)), "-> (back to head)")
        else:
            print("List is empty")


# Main Program
if __name__ == "__main__":
    cll = CircularLinkedList()

    while True:
        print("\n--- Circular Linked List ---")
        print("1. Insert")
        print("2. Delete")
        print("3. Reverse")
        print("4. Display")
        print("5. Concatenate")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter data: "))
            pos = int(input("Enter position: "))
            cll.insert(data, pos)

        elif choice == 2:
            pos = int(input("Enter position to delete: "))
            cll.delete(pos)

        elif choice == 3:
            cll.reverse()
            print("List reversed")

        elif choice == 4:
            cll.display()

        elif choice == 5:
            cll2 = CircularLinkedList()
            n = int(input("Enter number of elements in second list: "))

            for i in range(n):
                value = int(input("Enter element: "))
                cll2.insert(value, i + 1)

            cll = cll.concatenate(cll2)
            print("Lists concatenated")

        elif choice == 6:
            break

        else:
            print("Invalid choice")
