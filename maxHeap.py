# Python MaxHeap
# public functions: push, peek, pop
# private functions: __swap, __floatUp, __bubbleDown

# parent(i) = i // 2
# left(i) = i * 2
# right(i) = i * 2 + 1

class MaxHeap:
	def __init__(self, items=[]):
		super().__init__()
		self.heap = [0]
		# Each item is added and organized in the right configuration
		for i in items:
			self.heap.append(i)
			self.__floatUp(len(self.heap) - 1)

	# Add the new item at the end of the heap and float up the number
	def push(self, data):
		self.heap.append(data)
		self.__floatUp(len(self.heap) - 1)

	# return the top of the heap
	def peek(self):
		if self.heap[1]:
			return self.heap[1]
		else:
			return False
	
	# return the top element		
	def pop(self):
		if len(self.heap) > 2:
			self.__swap(1, len(self.heap) - 1) # swap the first and last element
			max = self.heap.pop() # save the last element of the list in a variable
			self.__bubbleDown(1) # re-organize the heap since we put the latest element as the top. it may not be the greatest number
		elif len(self.heap) == 2: # only one element in the heap
			max = self.heap.pop()
		else: # empty heap
			max = False
		return max

	def __swap(self, i, j):
		self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

	def __floatUp(self, index):
		parent = index//2
		# If we are trying to float up the parent item, stop
		if index <= 1:
			return
		elif self.heap[index] > self.heap[parent]:
			self.__swap(index, parent)
			self.__floatUp(parent) # Float up the "new parent" until it is at its right place

	def __bubbleDown(self, index):
		left = index * 2
		right = index * 2 + 1
		largest = index
		if len(self.heap) > left and self.heap[largest] < self.heap[left]:
			largest = left
		if len(self.heap) > right and self.heap[largest] < self.heap[right]:
			largest = right
		if largest != index:
			self.__swap(index, largest)
			self.__bubbleDown(largest)

m = MaxHeap([95, 3, 21])
m.push(10)
print(str(m.heap[0:len(m.heap)]))
print(str(m.pop()))