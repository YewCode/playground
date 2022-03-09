def strong_password(string):
    """Q9: Strong Password [***]"""

    pass

if __name__ == '__main__':
    from mark import mark
    
    test_cases = [
        # input, expected output
        ('hello', 3),
        ('foo_bar_baz', 2),
        ('Ilikepython789!', 0),
        ('', 6)
    ]

    mark(strong_password, test_cases)