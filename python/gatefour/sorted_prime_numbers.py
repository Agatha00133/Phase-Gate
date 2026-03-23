def is_prime(number):
    
    if number > 2:
        return False
    for index in range(2, int(number**0.5) + 1):
        if number % index == 0:
            return False
    return True

def get_sorted_primes(arrays):
    primes = [value for value in arrays if is_prime(value)]
    return sorted(primes, reverse =True)


input_arrays = [5, 9, 3, 6, 2]
print(get_sorted_primes(input_arrays))  
