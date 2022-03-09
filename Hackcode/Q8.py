def avicii(string):
    """Q8: Avicii [**]"""
    pass

if __name__ == '__main__':
    import textwrap

    print('\n', avicii.__doc__.upper(), '\n')

    print("-----------[ Test Case 1 ]-----------")
    print('Expected output:')
    print(textwrap.dedent('''
        * *****
      *** ***
    ***** *'''))

    print('\nActual output:\n')
    print(avicii(3))

    # n = 5
    print("-----------[ Test Case 2 ]-----------")
    print('Expected output:')
    print(textwrap.dedent('''
            * *********
          *** *******
        ***** *****
      ******* ***
    ********* *'''))

    print('\nActual output:\n')
    print(avicii(5))

    # n = 7
    print("-----------[ Test Case 3 ]-----------")
    print('Expected output:')
    print(textwrap.dedent('''
                * *************
              *** ***********
            ***** *********
          ******* *******
        ********* *****
      *********** ***
    ************* *'''))
    
    print('\nActual output:\n')
    print(avicii(7))
