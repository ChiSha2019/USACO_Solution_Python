a = [4,3,8,4,7,3]
x = 15
n = 6

a.sort()
print(a)
sum = 0
for i in range(n):
    sum = sum + a[i]
    if sum >= x:
        print(i)
        break
