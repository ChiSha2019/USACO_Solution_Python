ans = 100
with open('output_demon.out', 'w') as f:
    for i in range(ans, 0, -1):
        f.write(str(i))
        f.write('\n')
