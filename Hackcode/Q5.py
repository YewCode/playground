def deduplicate(numbers):
    """Q5: Dedup da dups [**]"""
    pass

if __name__ == '__main__':
    from mark import mark
    
    test_cases = [
        # input, expected output
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([12, 24, 35, 24, 88, 120, 155, 88, 120, 155], [12, 24, 35, 88, 120, 155]),
        ([5, 1, 1, 2, 2, 4, 3, 4, 5], [5, 1, 2, 4, 3])
    ]

    mark(deduplicate, test_cases)