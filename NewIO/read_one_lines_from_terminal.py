'''How to read from terminal'''

'''
sys.stdin.readline().split() reads in one line
int(x) for x in converts string to int

input example: 
4
1 2 3 4
'''

import sys

N = int(sys.stdin.readline())
#List = sys.stdin.readline().split()
List = [int(x) for x in sys.stdin.readline().split()]
print(N)
print(List)