"""

*****
****
***
**
*

*
**
***
****
*****

*****
 ****
  ***
   **
    *

*****
*
***
*
*****

"""

def pattern1():
    for i in range(5):
        for j in range(5 - i):
            print('*', end='')
        print()
    print()

def pattern2():
    for i in range(5):
        for j in range(i + 1):
            print('*', end='')
        print()
    print()

def pattern3():
    for i in range(5):
        for k in range(i):
            print(' ', end='')

        for j in range(5 - i):
            print('*', end='')
        print()
    print()

def pattern4():
    for i in range(5):
        print('*', end='')
    print('\n*')

    for i in range(3):
        print('*', end='')
    print('\n*')

    for i in range(5):
        print('*', end='')
    print()

if __name__ == '__main__':
    pattern1()
    pattern2()
    pattern3()
    pattern4()
