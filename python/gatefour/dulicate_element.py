def find_duplicates(arrays):
    seen = set()
    duplicates = set()

    for number in arrays:
        if number in seen:
            duplicates.add(number)
        else:
            seen.add(number)

    return list(duplicates)


input_arr = [45, 60, 3, 0, 67, 2, 45, 3, 22, 0]
print(find_duplicates(input_arr))  
