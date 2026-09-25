
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at a given position
    def insert(self, data, pos):
        if pos < 1:
            print("Invalid position")
            return

        new_node = Node(data)

        if pos == 1:
            new_node.next = self.head

            if self.head:
                self.head.prev = new_node

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
        new_node.prev = temp

        if temp.next:
            temp.next.prev = new_node

        temp.next = new_node

    # Delete from a given position
    def delete(self, pos):
        if self.head is None or pos < 1:
            print("List is empty or position is invalid")
            return

        temp = self.head

        if pos == 1:
            self.head = temp.next

            if self.head:
                self.head.prev = None
            return

        for _ in range(pos - 1):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next

        if temp is None:
            print("Position out of range")
            return

        if temp.prev:
            temp.prev.next = temp.next

        if temp.next:
            temp.next.prev = temp.prev

    # Reverse the linked list
    def reverse(self):
        current = self.head
        new_head = None

        while current:
            current.prev, current.next = current.next, current.prev
            new_head = current
            current = current.prev

        self.head = new_head

    # Concatenate two linked lists
    def concatenate(self, other):
        result = DoublyLinkedList()

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
        print("None <-> " + " <-> ".join(map(str, values)) + " <-> None"
              if values else "List is empty")


# Main Program
if __name__ == "__main__":
    dll = DoublyLinkedList()

    while True:
        print("\n--- Doubly Linked List ---")
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
            dll.insert(data, pos)

        elif choice == 2:
            pos = int(input("Enter position to delete: "))
            dll.delete(pos)

        elif choice == 3:
            dll.reverse()
            print("List reversed")

        elif choice == 4:
            dll.display()

        elif choice == 5:
            dll2 = DoublyLinkedList()
            n = int(input("Enter number of elements in second list: "))

            for i in range(n):
                value = int(input("Enter element: "))
                dll2.insert(value, i + 1)

            dll = dll.concatenate(dll2)
            print("Lists concatenated")

        elif choice == 6:
            break

        else:
            print("Invalid choice")
