def factorial(number):
    """Q3: Factorial [*]"""
    pass

if __name__ == '__main__':
    from mark import mark
    
    test_cases = [
        # input, expected output
        (5, 120),
        (10, 3628800),
        (-9, -362880),
        (0, 1)
    ]

    mark(factorial, test_cases)