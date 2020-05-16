'''

Given a singly-linked list, find the middle value in the list.
Example: If the given linked list is A → B → C → D → E, return C.
Assumptions: The length (n) is odd so the linked list has a definite middle.

'''


# Traverse linked list using two pointers. Move one pointer by one and other pointer by two. When the fast pointer reaches end slow pointer will reach middle of the linked list.


# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data  
        self.next = None 
  
class LinkedList: 
  
    def __init__(self, items=None): 
        self.head = None
        # Append given items
        if items is not None:
            for item in items:
                self.push(item)
  
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  
    # Function to get the middle of the linked list 
    def printMiddle(self): 
        slow_pointer = self.head 
        fast_pointer = self.head 
  
        if self.head is not None: 
            while (fast_pointer is not None and fast_pointer.next is not None): 
                fast_pointer = fast_pointer.next.next
                slow_pointer = slow_pointer.next
            print("The middle element is: ", slow_pointer.data) 
  
# Driver code 
list1 = LinkedList([5, 4, 3, 2, 1])
list1.printMiddle() 

list2 = LinkedList(["A", "B", "C", "D", "E"])
list2.printMiddle() 