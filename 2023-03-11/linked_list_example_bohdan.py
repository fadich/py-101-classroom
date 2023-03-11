class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

    def add_to_end(self, newdata):
        newnode = Node(newdata)
        if self.head is None:
            self.head = newnode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newnode

    def del_from_end(self):
        if self.head is None:
            return None
        if self.head.next is None:
            self.head = None
            return None
        prev = self.head
        current = self.head.next
        while current.next:
            prev = current
            current = current.next
        prev.next = None
        return current

    def max_ll(self):
        current = self.head
        max_elem = current
        while current.next:
            if max_elem.dataval < current.next.dataval:
                max_elem = current.next
            current = current.next
        return max_elem.dataval

    def search(self, val):
        current = self.head
        while True:
            if current.dataval == val:
                return current.dataval
            if current.next is None:
                break
            current = current.next
        return None

    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.dataval, "-> ", end="")
            printval = printval.next
        print()
