def all_palindromes(string):
    """Q10: All Palindromes [***]"""
    
    return



if __name__ == '__main__':
    from mark import mark
    
    test_cases = [
        # input, expected output
        ('abcba', ['abcba', 'bcb']),
        ('bbbaa', ['bbb', 'bb', 'aa']),
        ('xxyxyx', ['xyxyx', 'xyx', 'yxy', 'xx']),
        ('aaaayzxzya', ['aaaa', 'aaa', 'aa', 'ayzxzya', 'yzxzy', 'zyz'])
    ]

    mark(all_palindromes, test_cases)