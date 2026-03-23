def replace_negatives(array):
    result = []
    for numb in array:
        if numb < 0:
            result.append(0)
        else:
            result.append(numb)
    return result


input_arr = [5, -9, 3, -6, 2, -11]
print(replace_negatives(input_arr))  
