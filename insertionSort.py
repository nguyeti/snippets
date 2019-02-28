# worst-case: O(n²)
# avg-case: O(n²)
# best-case: O(n) when the array is already sorted

def insertionSort(input):
    for index in range(1, len(input)):
        currentvalue = input[index]
        position = index

        while position>0 and input[position-1]>currentvalue:
            input[position] = input[position-1]
            position = position-1
            input[position]=currentvalue

        print("step: {0}, array: {1}".format(index, input))

if __name__ == "__main__":        
    input = [10,5,2,604,98,2, 1]
    insertionSort(input)

print(input)

# Output
# step: 1, array: [5, 10, 2, 604, 98, 2, 1]
# step: 2, array: [2, 5, 10, 604, 98, 2, 1]
# step: 3, array: [2, 5, 10, 604, 98, 2, 1]
# step: 4, array: [2, 5, 10, 98, 604, 2, 1]
# step: 5, array: [2, 2, 5, 10, 98, 604, 1]
# step: 6, array: [1, 2, 2, 5, 10, 98, 604]
# [1, 2, 2, 5, 10, 98, 604]