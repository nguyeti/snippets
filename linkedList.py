

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    # Print the linked list
    def listprint(self):
        printval = self.head
        while printval is not None:
            print (printval.dataval)
            printval = printval.next

    # Function to add newnode
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return
        laste = self.head
        while(laste.next): # iterate until the end
            laste = laste.next
        laste.next=NewNode
        
    def AtBegining(self, newdata):
        NewNode = Node(newdata)
        # Update the new nodes next val to existing node
        NewNode.next = self.head
        self.head = NewNode

    def Inbetween(self, middle_node, newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(newdata)
        NewNode.next = middle_node.next
        middle_node.next = NewNode

    def reverse(self):
        prev = None
        current = self.head
        
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    
    def recursive_reverse(self, head):
        '''
            start with the current node
            1. if curr is null, return
            2. if curr's next element is null, this mean it is the last node, make this as head bc the last node will be the head of reversed list. return
            3. recursively traverse the list
            4. set current.next.next to current
            5. set current.next to null
        '''
        current = head
        if current == None: # if curr is null, return
            return
        
        if(current.next == None): # reach the last node, make it as head
            self.head = current
            return
        
        self.recursive_reverse(current.next)
        current.next.next = current # at this moment, the recursive calls reached the end, you come back to the previous node
        current.next = None

if __name__ == "__main__":
    list = SLinkedList()
    list.head = Node("Mon")
    e2 = Node("Tue")
    e3 = Node("Wed")

    list.head.next = e2
    e2.next = e3

    # list.AtBegining("Sun")

    # list.AtEnd("test")
    # list.Inbetween(e2, "inBetween")
    list.listprint()
    print('reverse')
    list.reverse()
    list.listprint()
    print('reverse')
    list.recursive_reverse(list.head)
    list.listprint()
