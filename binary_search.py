def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence) - 1

    if not sequence:
        return None

    while begin_index <= end_index:
        mid_index = begin_index + (end_index - begin_index) // 2
        print(mid_index)
        mid_value = sequence[mid_index]
        if mid_value == item:
            return mid_index
        
        elif item < mid_value:
            end_index = mid_index - 1

        else:
            begin_index = mid_index + 1

    return None

sequence_1 = [1,3,5,8,9]
item_1 = 8
print(binary_search(sequence_1, item_1))
