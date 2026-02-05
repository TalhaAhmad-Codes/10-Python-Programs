"""
  0123456789 (j)
0 **********
1 *|======|*
2 *|=~~~~=|*
3 *|=¦××¦=|*
4 *|=¦××¦=|*
5 *|=<__>=|*
6 *|======|*
7 *|======|*
8 **********
(i)
"""

for i in range(9):
    for j in range(10):
        if i == 0 or i == 8:
            print('*', end='')
        else:
            if j == 0 or j == 9:
                print('*', end='')
            elif j == 1 or j == 8:
                print('|', end='')
            else:
                if i == 1 or i == 6 or i == 7:
                    print('=', end='')
                else:
                    if j == 2 or j == 7:
                        print('=', end='')
                    else:
                        if i == 2:
                            print('~', end='')
                        elif i == 5:
                            if j == 3:
                                print('<', end='')
                            elif j == 6:
                                print('>', end='')
                            else:
                                print('_', end='')
                        else:
                            if j == 3 or j == 6:
                                print('¦', end='')
                            else:
                                print('x', end='')
    print()
