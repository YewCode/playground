def snake_to_camel(string):
    """Q6: Sneks & Camels [**]"""
    pass


if __name__ == '__main__':
    from mark import mark
    
    test_cases = [
        # input, expected output
        ('hello_world', 'helloWorld'),
        ('foo_bar_baz', 'fooBarBaz'),
        ('123', '123'),
        ('', '')
    ]

    mark(snake_to_camel, test_cases)