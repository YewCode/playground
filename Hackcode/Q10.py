def all_palindromes(string):
    """Q10: All Palindromes [***]"""
    pass




if __name__ == '__main__':
    from mark import mark
    
    test_cases = [
        # input, expected output
        ('abcba', ['abcba', 'bcb']),
        ('bbbaa', ['bbb', 'bb', 'aa']),
        ('xxyxyx', ['xyxyx', 'xyx', 'yxy', 'xx']),
        ('aaaayzxzya', ['aaaa', 'aaa', 'aa', 'ayzxzya', 'yzxzy', 'zxz'])
    ]

    mark(all_palindromes, test_cases)

# for i in range(len(my_str)):
#     print(my_str[i],end = " ") 
    
# print("\n")

# reverse = my_str[::-1]
# for j in range(len(reverse)):
#     print(reverse[j], end = " ")