# worst-case: O(n²)
# avg-case: O(n²)
# best-case: O(n)

input = [1,5,2,604,98]

def bubbleSort(array):
  for i in range(len(array)):
    for j in range(len(array) - 1):
      if array[j] > array[j + 1]:
        print("Swapping {0} and {1}".format(array[j], array[j+1]))
        temp = array[j+1]
        array[j+1] = array[j]
        array[j] = temp
      print("[{0},{1}]: {2}".format(i, j, array))
  print("Sorted array: {0}".format(array))

bubbleSort(input)