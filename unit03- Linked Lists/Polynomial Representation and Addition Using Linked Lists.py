
class Node:
    def __init__(self, coeff, exp):
        self.coeff = coeff
        self.exp = exp
        self.next = None


class Polynomial:
    def __init__(self):
        self.head = None

    # Insert a term in descending exponent order
    def insert_term(self, coeff, exp):
        if coeff == 0:
            return

        new_node = Node(coeff, exp)

        # Insert at beginning
        if self.head is None or self.head.exp < exp:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        # Find correct position
        while temp.next and temp.next.exp > exp:
            temp = temp.next

        # Combine terms with same exponent
        if temp.exp == exp:
            temp.coeff += coeff

            if temp.coeff == 0:
                self.head = temp.next
            return

        if temp.next and temp.next.exp == exp:
            temp.next.coeff += coeff

            if temp.next.coeff == 0:
                temp.next = temp.next.next
            return

        new_node.next = temp.next
        temp.next = new_node

    # Add two polynomials
    def add(self, poly2):
        result = Polynomial()

        p1 = self.head
        p2 = poly2.head

        while p1 and p2:
            if p1.exp == p2.exp:
                result.insert_term(p1.coeff + p2.coeff, p1.exp)
                p1 = p1.next
                p2 = p2.next

            elif p1.exp > p2.exp:
                result.insert_term(p1.coeff, p1.exp)
                p1 = p1.next

            else:
                result.insert_term(p2.coeff, p2.exp)
                p2 = p2.next

        # Copy remaining terms
        while p1:
            result.insert_term(p1.coeff, p1.exp)
            p1 = p1.next

        while p2:
            result.insert_term(p2.coeff, p2.exp)
            p2 = p2.next

        return result

    # Display polynomial
    def display(self):
        if self.head is None:
            print("0")
            return

        temp = self.head
        terms = []

        while temp:
            coeff = temp.coeff
            exp = temp.exp

            if exp == 0:
                term = str(abs(coeff))
            elif exp == 1:
                term = str(abs(coeff)) + "x"
            else:
                term = str(abs(coeff)) + "x^" + str(exp)

            if not terms:
                if coeff < 0:
                    terms.append("-" + term)
                else:
                    terms.append(term)
            else:
                sign = " - " if coeff < 0 else " + "
                terms.append(sign + term)

            temp = temp.next

        print("".join(terms))


# Input polynomial
def create_polynomial():
    poly = Polynomial()

    n = int(input("Enter number of terms: "))

    for i in range(n):
        print("Term", i + 1)
        coeff = int(input("Enter coefficient: "))
        exp = int(input("Enter exponent: "))

        poly.insert_term(coeff, exp)

    return poly


# Main Program
if __name__ == "__main__":
    print("\nEnter First Polynomial")
    p1 = create_polynomial()

    print("\nEnter Second Polynomial")
    p2 = create_polynomial()

    print("\nFirst Polynomial:")
    p1.display()

    print("\nSecond Polynomial:")
    p2.display()

    result = p1.add(p2)

    print("\nResultant Polynomial:")
    result.display()
