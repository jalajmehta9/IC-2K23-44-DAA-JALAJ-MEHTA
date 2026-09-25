
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at a given position
    def insert(self, data, pos):
        new_node = Node(data)

        if pos < 1:
            print("Invalid position")
            return

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        for _ in range(pos - 2):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next

        if temp is None:
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
            self.head = self.head.next
            return

        temp = self.head
        for _ in range(pos - 2):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next

        if temp is None or temp.next is None:
            print("Position out of range")
            return

        temp.next = temp.next.next

    # Reverse the linked list
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    # Concatenate two linked lists
    def concatenate(self, other):
        result = SinglyLinkedList()

        for value in self.to_list() + other.to_list():
            result.insert(value, len(result.to_list()) + 1)

        return result

    def to_list(self):
        values = []
        temp = self.head

        while temp:
            values.append(temp.data)
            temp = temp.next

        return values

    # Display linked list
    def display(self):
        values = self.to_list()
        print(" -> ".join(map(str, values)) + " -> None"
              if values else "List is empty")


# Main Program
if __name__ == "__main__":
    l1 = SinglyLinkedList()

    while True:
        print("\n--- Singly Linked List ---")
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
            l1.insert(data, pos)

        elif choice == 2:
            pos = int(input("Enter position to delete: "))
            l1.delete(pos)

        elif choice == 3:
            l1.reverse()
            print("List reversed")

        elif choice == 4:
            l1.display()

        elif choice == 5:
            l2 = SinglyLinkedList()
            n = int(input("Enter number of elements in second list: "))

            for i in range(n):
                value = int(input("Enter element: "))
                l2.insert(value, i + 1)

            l1 = l1.concatenate(l2)
            print("Lists concatenated")

        elif choice == 6:
            break

        else:
            print("Invalid choice")
