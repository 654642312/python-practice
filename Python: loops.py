'''
    The provided code stub reads and integer, n, from STDIN. for all
    non-negative integers i < n, print i^2.
    example
    n = 3
    the list of non-negative that are less than n = 3 is [0, 1, 2]
    print the square of each number on a separate line.

    0
    1
    4

    Input Format

    The first and only line contains the integer, n.

    Constraints

    1 <= n <= 20

    output Format

    print n lines, one corresponding to each i.

    sample input 0

    5

    Sample Output 0

    0
    
    1

    4

    9

    16
'''

# Solution

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        print(i**2)
