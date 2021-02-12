'''read in from terminal'''
import sys
for line in sys.stdin:
    line1 = line.split()
    break

list_read = [int(i) for i in line1]
list_read.sort()
N = len(list_read)
'''
It's either
A = list_read[0], B = list_read[1], C = list_read[2] or
A = list_read[0], B = list_read[1], C = list_read[3]
'''
A = list_read[0]
B = list_read[1]

if list_read[3] == A + B:
    C = list_read[2]
else:
    C = list_read[3]

print(str(A) + " " + str(B) + " " + str(C))

