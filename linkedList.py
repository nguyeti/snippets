

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    # Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval

    # Function to add newnode
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval): # iterate until the end
            laste = laste.nextval
        laste.nextval=NewNode
        
    def AtBegining(self, newdata):
        NewNode = Node(newdata)
        # Update the new nodes next val to existing node
        NewNode.nextval = self.headval
        self.headval = NewNode

    def Inbetween(self, middle_node, newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode

if __name__ == "__main__":
    list = SLinkedList()
    list.headval = Node("Mon")
    e2 = Node("Tue")
    e3 = Node("Wed")

    list.headval.nextval = e2
    e2.nextval = e3

    list.AtBegining("Sun")

    list.AtEnd("test")
    list.Inbetween(e2, "inBetween")
    list.listprint()