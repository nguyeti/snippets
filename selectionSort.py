# worst-case: O(n²)
# avg-case: O(n²)
# best-case: O(n²)

input = [10,5,2,604,98,2]

def selectionSort(input):
   for fillslot in range(len(input)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if input[location]>input[positionOfMax]:
                positionOfMax = location

        temp = input[fillslot]
        input[fillslot] = input[positionOfMax]
        input[positionOfMax] = temp
        print("fillslot: {0}, array: {1}".format(fillslot, input))
selectionSort(input)


# Output
# fillslot: 5, array: [10, 5, 2, 2, 98, 604]
# fillslot: 4, array: [10, 5, 2, 2, 98, 604]
# fillslot: 3, array: [2, 5, 2, 10, 98, 604]
# fillslot: 2, array: [2, 2, 5, 10, 98, 604]
# fillslot: 1, array: [2, 2, 5, 10, 98, 604]