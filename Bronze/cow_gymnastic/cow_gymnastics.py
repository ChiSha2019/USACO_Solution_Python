
def better(N, a, b, session):
    apos = -1
    bpos = -1
    for i in range(0,N):
        if data[session][i] == a:
            apos = i
        if data[session][i] == b:
            bpos = i
    return apos < bpos

def N_better(a, b, K):
    total = 0
    for session in range(0, K):
        if better(a,b,session):
            total += 1
    return total

with open("gymnastics.in", "r") as input_file:
    line1 = input_file.readline().split()
    K = int(line1[0])
    N = int(line1[1])
    data = [[None] * K for _ in range(N)]
    for k in range(0,K):
        line_k = input_file.readline().split()
        for n in range(0, N):
            data[k][n] = int(line_k[n])

    answer = 0
    for a in range(1,N+1):
        for b in range(1,N+1):
            if N_better(a,b,K) == K:
                answer += 1

    print(answer)


