def seek_and_destroy(maze):
    """Q17: Seek & Destroy [*****]"""

    pass 


if __name__ == '__main__':
    from mark import mark 

    test_cases = [
        (["OOOOOO",
          "XOXOXO",
          "XOXXXO",
          "OOXOOO",
          "OXOOXO"], 35),
          
        (["OOOOO",
          "OXXOX",
          "OXOXX",
          "OXOOO", # There's an area in the maze that cannot
          "OXOXX", # be reached!
          "OXOOX",
          "OXOXX"], 17),

        (["OOXXOO",
          "XOOOOX",
          "XOXXOX",
          "XOXOOO",
          "XXXOXO"], 33),

        (["OOXOXOXOXOXO",
          "XOXOXOXOXOXO",
          "XOXOXOXOXOXO",
          "XOOOOOOOOOOO",
          "XOXOXOXOXOXO",
          "XOXOXOXOXOXO",
          "XOXOXOXOXOXO"], 148),

        (["OXOOOOOOOOO",
          "OXOXXXXXXXO",
          "OXOXOOOOOXO",
          "OXOXXXXXOXO", 
          "OXOOOOOOOXO",
          "OXXXXXXXXXO",
          "OOOOOOOOOOO"], 47),
    ]

    mark(seek_and_destroy, test_cases)