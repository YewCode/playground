def is_pangram(sentence):
    """Q4: Pangrams [*]"""
    pass

if __name__ == '__main__':
    from mark import mark
    
    test_cases = [
        # input, expected output
        ("The quick brown fox jumps over the lazy dog", True),
        ("abcdefghijklmnopqrstuvwxyz", True),
        ("'Hello world' is my favorite phrase ever", False),
        ("I think python is lit fam", False)
    ]

    mark(is_pangram, test_cases)
