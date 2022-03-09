def get_all_multiples(number, start, end):
    """Q2: Multiples [*]"""
    
    pass

if __name__ == '__main__':

    print('\n', get_all_multiples.__doc__.upper(), '\n')

    print("-----------[ Test Case 1 ]-----------")
    print("Expected output: [7, 14, 21, 28]")
    actual = get_all_multiples(7, 1, 30)
    print("Actual output: ", actual)
    
    print()

    print("-----------[ Test Case 2 ]-----------")
    print("Expected output: [2, 4, 6, 8, 10]")
    actual = get_all_multiples(2, 1, 11)
    print("Actual output: ", actual)

    print()

    print("-----------[ Test Case 3 ]-----------")
    print("Expected output: []")
    actual = get_all_multiples(0, 1, 100)
    print("Actual output: ", actual)


