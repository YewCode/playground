def min_flips(string):
    """Q12: Minimum Flips [***]"""

    pass 

if __name__ == '__main__':
    from mark import mark 

    test_cases = [
        ('xyxy', 1),
        ('yyyxxx', 4),
        ('xxyxx', 2),
        ('yxyx', 2),
        ('xyyxxyxyxxxyxx', 6),
    ]

    mark(min_flips, test_cases)