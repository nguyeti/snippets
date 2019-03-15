

class Stack:
    def __init__(self):
        self.stack = []

    def add(self, dataval):
    # Use list append method to add element
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

    # Use peek to look at the top of the stack
    def peek(self):     
	    return self.stack[0]

    def remove(self):
        if len(self.stack) <= 0:
            print("No data in the stack")
            return False
        else:
            return self.stack.pop()
        
    def traverse(self):
        [print(i) for i in self.stack]

if __name__ == "__main__":
    AStack = Stack()
    AStack.add("Mon")
    AStack.add("Tue")
    AStack.add("Wed")
    AStack.add("Thu")
    AStack.remove()
    AStack.traverse()