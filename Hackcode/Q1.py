def autocomplete(char, words):
    """Q1: Autocomplete [*]"""
    

    pass


if __name__ == '__main__':
    from mark import mark

    test_cases = [
        ( ('de', ['dog', 'deer', 'deal']), ['deer', 'deal'] ),
        ( ('lol', ['lollipop', 'lol', 'ferlolfel']), ['lollipop', 'lol'] ),
        ( ('top', ['topgun', 'toplel', 'topology']), ['topgun', 'toplel', 'topology'] ),
        ( ('', ['abc', 'def', 'ghi']), ['abc', 'def', 'ghi'] ),
        ( ('a', []), [] )
    ]

    mark(autocomplete, test_cases)

