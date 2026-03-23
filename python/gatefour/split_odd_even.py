def split_even_odd(arrays):
    odd = []
    even = []

    for number in arrays:
        if number % 2 != 0:
            odd.append(number)
        else:
            even.append(number)

    return [odd, even]


input_arrays = [45, 60, 3, 10, 9, 22]
print(split_even_odd(input_arrays))  
