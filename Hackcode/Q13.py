def is_well_formed(string):
    """Q13: Well-formed Strings [****]"""

    pass 

if __name__ == '__main__':
    from mark import mark 

    test_cases = [
        ('([])[]({})', True),
        ('((()))[{()}]', True),
        ('[(])', False),
        (')[](', False),
        ('[]}{()', False),
    ]

    mark(is_well_formed, test_cases)