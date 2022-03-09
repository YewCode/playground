def add_subtract(n):
    """Q16: Call Chain [****]"""

    pass 

if __name__ == '__main__':
    print('\n', add_subtract.__doc__.upper(), '\n')
    
    print('-----------[ Test Case 1 ]-----------')
    print('Expected output: 7')
    print('Actual output:  ', add_subtract(7))

    print('-----------[ Test Case 2 ]-----------')
    print('Expected output: 0')
    print('Actual output:  ', add_subtract(7)(2)(3))

    print('-----------[ Test Case 3 ]-----------')
    print('Expected output: 11')
    print('Actual output:  ', add_subtract(-5)(10)(3)(9))

    print('-----------[ Test Case 4 ]-----------')
    print('Expected output: 180')
    print('Actual output:  ', add_subtract(10)(200)(10))