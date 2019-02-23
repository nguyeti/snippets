# worst-case: O(n²)
# avg-case: O(n²)
# best-case: O(n²)

input = [10,5,2,604,98,2]

def selectionSort(input):
    print("The input is {0}".format(input))
    for i in range(len(input)):
        iMin = i
        print("iMin: {0}".format(iMin))
        for j in range(i + 1, len(input)):
            if input[j] <= input[iMin]:
                print("Swapping {0} and {1}".format(input[j], input[iMin]))
                temp = input[iMin]
                input[iMin] = input[j]
                input[j] = temp
                print(input)
        print("The smallest number is at the leftmost position: {0}".format(iMin))
        
    print("Sorted array: {0}".format(input))
        
selectionSort(input)