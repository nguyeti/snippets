# worst-case: O(n²)
# avg-case: O(n²)
# best-case: O(n) when the array is already sorted

input = [10,5,2,604,98,2, 1]

def insertionSort(input):
    for index in range(1, len(input)):
        currentvalue = input[index]
        position = index

        while position>0 and input[position-1]>currentvalue:
            input[position] = input[position-1]
            position = position-1
            input[position]=currentvalue
insertionSort(input)

print(input)
