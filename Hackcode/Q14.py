def minimum_bribes(string):
    """Q14: New Year Chaos [</>]"""

    pass 

if __name__ == '__main__':
    from mark import mark 

    test_cases = [
        ([3, 1, 2, 5, 4], 3),
        ([2, 3, 5, 4, 1], 5),
        ([5, 3, 1, 4, 2], 'Too Chaotic'),
        ([1, 2, 5, 3, 7, 8, 6, 4], 7),
        ([5, 1, 2, 3, 7, 8, 6, 4], 'Too Chaotic'),
        ([1, 2, 3, 4, 5, 6, 7, 8], 0),
        ([2, 3, 4, 5, 6, 7, 8, 1], 7),
    ]

    mark(minimum_bribes, test_cases)