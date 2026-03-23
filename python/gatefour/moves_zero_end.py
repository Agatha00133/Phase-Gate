def move_zeros(arrays):
    result = []

    
    for number in arrays:
        if number != 0:
            result.append(number)

    
    zeros_count = len(arrays) - len(result)

   
    result.extend([0] * zeros_count)

    return result

input_arrays = [5, 0, 3, 0, 2, 0]
print(move_zeros(input_arrays))  
