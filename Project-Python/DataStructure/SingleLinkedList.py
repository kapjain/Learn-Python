class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
    

    def insertAtEnding(self, data):
        temp = self.head
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            while(temp.next != None):
                temp = temp.next
            temp.next = new_node
            return
    
    def insertAtbegining(self, data):
        temp = self.head
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        else:
            self.head = new_node
            new_node.next = temp
            return
    
    def deleteFromEnd(self):
        curr_node = self.head
        prev_node = None
        if curr_node is None:
            print("List is empty, can not delete an element")
        elif curr_node.next is None:
            self.head = None
        else:
            while(curr_node.next != None):
                prev_node = curr_node
                curr_node = curr_node.next
            prev_node.next = None
                
    def printList(self):
        temp = self.head
        if temp is None:
            print("List is empty. There is no element in the linked list")
        else:
            while(temp != None):
                print(temp.data)
                temp = temp.next
                
sll = SLinkedList()


sll.insertAtEnding(1)
sll.insertAtEnding(2)
sll.insertAtEnding(3)
sll.insertAtEnding(4)
sll.insertAtEnding(5)
sll.printList()
sll.deleteFromEnd()

sll.printList()