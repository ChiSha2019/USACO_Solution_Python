import sys
'''
4
1 1 2 3
'''
N = int(sys.stdin.readline())
all_flower = [int(x) for x in sys.stdin.readline().split()]

result = N
for i in range(0,N-1):
    for j in range(i+1,N):
        '''must be evenly divided by the number of flower to have average'''
        all_flower_i2j = all_flower[i:j + 1]
        sum_i_j = sum(all_flower_i2j)
        if sum_i_j % (j-i+1) == 0:
            average = sum_i_j / (j-i+1)
            if average in all_flower_i2j:
                result += 1
print(result)




