class Node:
    def __init__(self, data= None, next=None):
        self.data = data
        self.next = next

        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node 
    
    def print(self):
        # itr is head node 
        
        itr= self.head 
        llstr= ""
        
        while itr:
            suffix = ""
            if itr.next:
                suffix = " --> "
            llstr += str(itr.data) + suffix
            itr = itr.next
        print(llstr)
        
        if self.head is None:
            print("Linked list is empty")
            return
        
 
    def insert_at_end(self, data):
        if self.head is None:
            self.head= Node(data, None )
            return
            
        itr = self.head
        while itr.next:
            itr= itr.next
            
        itr.next= Node(data)
        
    def get_length(self):
            count = 0
            itr= self.head 
            while itr:
                count +=1
                itr = itr.next
            return count
    
    def insert_at(self, index, data):
        itr= self.head
        count=0
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_beginning(data)
            return
        
        while itr:
            count+=1
            if count==index-1:
                itr.next= Node(data, itr.next)
                break
            itr= itr.next

        
        
if __name__ == "__main__":
    root = LinkedList()
    
    root.insert_at_end(50)
    root.insert_at_beginning(5)
    root.insert_at_beginning(15)
    root.insert_at_beginning(10)
    root.insert_at(4, 20)
    print(root.get_length())
    root.print()