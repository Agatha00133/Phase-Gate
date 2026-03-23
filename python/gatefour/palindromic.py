def is_palindromic(arrays):
    return arrays == arrays[::-1]


arrays = [45, 0, 8, 0, 45]
print(is_palindromic(arrays))  
