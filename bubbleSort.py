# worst-case: O(n²)
# avg-case: O(n²)
# best-case: O(n)

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

def bubble(list_a):
  indexing_length = len(list_a) - 1
  sorted = False

  while not sorted:
    sorted = True
    for i in range(0, indexing_length):
      if list_a[i] > list_a[i+1]:
        sorted = False
        list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
  return list_a

if __name__ == "__main__":
    input = [1,5,2,604,98]
    print(bubble(input))

# Output
# [0,0]: [1, 5, 2, 604, 98]
# Swapping 5 and 2
# [0,1]: [1, 2, 5, 604, 98]
# [0,2]: [1, 2, 5, 604, 98]
# Swapping 604 and 98
# [0,3]: [1, 2, 5, 98, 604]
# [1,0]: [1, 2, 5, 98, 604]
# [1,1]: [1, 2, 5, 98, 604]
# [1,2]: [1, 2, 5, 98, 604]
# [1,3]: [1, 2, 5, 98, 604]
# [2,0]: [1, 2, 5, 98, 604]
# [2,1]: [1, 2, 5, 98, 604]
# [2,2]: [1, 2, 5, 98, 604]
# [2,3]: [1, 2, 5, 98, 604]
# [3,0]: [1, 2, 5, 98, 604]
# [3,1]: [1, 2, 5, 98, 604]
# [3,2]: [1, 2, 5, 98, 604]
# [3,3]: [1, 2, 5, 98, 604]
# [4,0]: [1, 2, 5, 98, 604]
# [4,1]: [1, 2, 5, 98, 604]
# [4,2]: [1, 2, 5, 98, 604]
# [4,3]: [1, 2, 5, 98, 604]
# Sorted array: [1, 2, 5, 98, 604]