def encode(string):
    """Q11: Run-Length Encoding [***]"""

    pass

if __name__ == '__main__':
    from mark import mark

    test_cases = [
        # input, expected_output
        ('aaabbccc', '3a2b3c'),
        ('AAaabBBBcCCd', '2A2a1b4B1c2C1d'),
        ('xxyxyx', '2x1y1x1y1x'),
        ('111122', '4[1]2[2]'),
        ('aa22b888cc', '2a2[2]1b3[8]2c'),
    ]

    mark(encode, test_cases)