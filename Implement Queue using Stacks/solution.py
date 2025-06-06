"""A QUEUE"""
class Node:
    """A CLASS NODE"""
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    """A CLASS FOR A LINKEDLIST OBJECT"""
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        """A STRING METHOD"""
        current_node = self.head
        string = ""
        while current_node is not None:
            string += str(current_node.data) + " -> "
            current_node = current_node.next_node
        string += str(current_node)
        return string

    def append(self, next_data):
        """AN APPEND METHOD"""
        current_node = self.head
        if self.head is None:
            self.head = Node(next_data)
            return
        while current_node.next_node is not None:
            current_node = current_node.next_node
        current_node.next_node = Node(next_data)
        self.size += 1

    def pop(self):
        """POP METHOD"""
        current_node = self.head
        prev_node = None
        while current_node.next_node is not None:
            prev_node = current_node
            current_node = current_node.next_node
        if prev_node is not None:
            prev_node.next_node = None
        else:
            self.head = None
        return current_node.data

    def index(self, value):
        """INDEX METHOD"""
        current_node = self.head
        i = 0
        while current_node is not None:
            if current_node.data == value:
                return i
            current_node = current_node.next_node
            i += 1

class LinkedStack:
    """A LINKED STACK"""
    def __init__(self):
        self.items = LinkedList()
        self._size = 0

    def push(self, item):
        """A PUSH METHOD"""
        self.items.head = Node(item, self.items.head)
        self._size += 1

    def pop(self):
        """A POP METHOD"""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        head = self.items.head
        self.items.head = head.next_node
        self._size -= 1
        return head.data

    def peek(self):
        """A PEEK METHOD"""
        if self.is_empty():
            return None
        return self.items.head.data

    def __iter__(self):
        nodes = []
        current_node = self.items.head
        while current_node:
            nodes.append(current_node.data)
            current_node = current_node.next_node
        return iter(nodes[::-1])

    def __len__(self):
        return self._size

    def is_empty(self):
        """IS EMPTY METHOD"""
        return self._size == 0

    def __str__(self):
        current_node = self.items.head
        string = ""
        while current_node is not None:
            string += str(current_node.data) + " <- "
            current_node = current_node.next_node
        string += str(current_node)
        return string

class MyQueue:
    """Queue implemented using two stacks"""
    def __init__(self):
        self.in_stack = LinkedStack()
        self.out_stack = LinkedStack()

    def push(self, x: int) -> None:
        """PUSH METHOD"""
        self.in_stack.push(x)

    def _transfer(self):
        """TRANSFER helping METHOD"""
        while not self.in_stack.is_empty():
            self.out_stack.push(self.in_stack.pop())

    def pop(self) -> int:
        """POP METHOD"""
        if self.empty():
            raise IndexError("Pop from empty queue")
        if self.out_stack.is_empty():
            self._transfer()
        return self.out_stack.pop()

    def peek(self) -> int:
        """PEEK METHOD"""
        if self.empty():
            raise IndexError("Peek from empty queue")
        if self.out_stack.is_empty():
            self._transfer()
        return self.out_stack.peek()

    def empty(self) -> bool:
        """EMPTY METHOD"""
        return self.in_stack.is_empty() and self.out_stack.is_empty()

    def __len__(self):
        return len(self.in_stack) + len(self.out_stack)
