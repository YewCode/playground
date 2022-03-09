def get_primes(limit):
    """Q7: Prime Numbers [**]"""
    pass

    

if __name__ == '__main__':
    from mark import mark
    
    test_cases = [
        # input, expected output
        (10, '2, 3, 5, 7'),
        (20, '2, 3, 5, 7, 11, 13, 17, 19'),
        (100, '2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97'),
        (-10, ''),
    ]

    mark(get_primes, test_cases)