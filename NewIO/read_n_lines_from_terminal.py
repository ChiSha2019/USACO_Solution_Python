'''How to read from terminal'''
'''
input example:
3
1 2 3
4 5 6
7 8 9
'''
import sys
N = int(sys.stdin.readline())
List = []
for i in range(0,N):
        List.append(sys.stdin.readline().split())

print(List)