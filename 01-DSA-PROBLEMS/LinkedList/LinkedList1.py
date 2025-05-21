class Node:
    def __init__(self, data= None, next=None):
        self.data = data
        self.next = next

        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self, data):
        node = Node(data)
        self.head = node if self.head is None else self.head
        
if __name__ == "__main__":
    pass