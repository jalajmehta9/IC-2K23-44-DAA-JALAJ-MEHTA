# Linked List Operations and Polynomial Addition in Python

This repository contains Python 3 implementations of different types of linked lists and polynomial operations using linked lists as part of Data Structures and Algorithms (DSA) lab practicals.

## 📚 Practicals Included

### 1. Singly Linked List
**File:** `Singly_Linked_List.py`

A singly linked list consists of nodes where each node stores data and a pointer to the next node.

**Operations:**
- Insert an element at a specified position.
- Delete an element from a specified position.
- Reverse the linked list.
- Concatenate two linked lists.
- Display the linked list.

### 2. Doubly Linked List
**File:** `Doubly_Linked_List.py`

A doubly linked list consists of nodes containing data and two pointers: one pointing to the previous node and another pointing to the next node.

**Operations:**
- Insert an element at a specified position.
- Delete an element from a specified position.
- Reverse the linked list.
- Concatenate two linked lists.
- Display the linked list.

### 3. Circular Linked List
**File:** `Circular_Linked_List.py`

A circular linked list is a linked list in which the last node points back to the first node, forming a circular structure.

**Operations:**
- Insert an element at a specified position.
- Delete an element from a specified position.
- Reverse the circular linked list.
- Concatenate two circular linked lists.
- Display the linked list.

### 4. Polynomial Representation and Addition Using Linked Lists
**File:** `Polynomial_Addition.py`

A polynomial is represented using a linked list in which each node stores:
- Coefficient
- Exponent
- Pointer to the next node

**Operations:**
- Create a polynomial using linked lists.
- Insert polynomial terms in descending order of exponents.
- Combine terms having the same exponent.
- Add two polynomials.
- Display the resultant polynomial.

**Example:**

Polynomial 1:

`5x^3 + 4x^2 + 2x + 7`

Polynomial 2:

`3x^3 + 2x^2 + 5x + 1`

Result:

`8x^3 + 6x^2 + 7x + 8`

## 🛠️ Technologies Used

- **Programming Language:** Python 3
- **Concepts:** Data Structures, Linked Lists, Pointers (References), Polynomial Representation, Polynomial Addition.

## 📁 Project Structure

```text
Linked-List-Practicals/
│
├── Singly_Linked_List.py
├── Doubly_Linked_List.py
├── Circular_Linked_List.py
├── Polynomial_Addition.py
│
└── README.md
```

## ⚙️ Requirements

- Python 3.x
- VS Code, PyCharm, or any Python IDE.

No external libraries are required.

## ▶️ How to Run

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd Linked-List-Practicals
   ```

3. Run any practical independently:

   **Singly Linked List**
   ```bash
   python Singly_Linked_List.py
   ```

   **Doubly Linked List**
   ```bash
   python Doubly_Linked_List.py
   ```

   **Circular Linked List**
   ```bash
   python Circular_Linked_List.py
   ```

   **Polynomial Addition**
   ```bash
   python Polynomial_Addition.py
   ```

## ⏱️ Time Complexity

Let `n` be the number of nodes in the first linked list and `m` be the number of nodes in the second linked list.

| Operation | Singly | Doubly | Circular |
|---|---|---|---|
| Insertion at position | O(n) | O(n) | O(n) |
| Deletion at position | O(n) | O(n) | O(n) |
| Reversal | O(n) | O(n) | O(n) |
| Display | O(n) | O(n) | O(n) |
| Concatenation (current implementation) | O((n+m)²) | O((n+m)²) | O((n+m)²) |

**Polynomial Addition:** O(n + m), assuming both polynomials are sorted by descending exponent.

## 🎯 Learning Objectives

- Understand the concept and structure of linked lists.
- Differentiate between singly, doubly, and circular linked lists.
- Implement insertion, deletion, reversal, and concatenation.
- Understand dynamic memory structures using Python references.
- Represent polynomials using linked lists.
- Perform polynomial addition efficiently.
