'''
try all possible combinations of which cow is patient zero and the value of K
There are N choices for patient zero,
and K can be from 0 up to T (K > T behaves the same as K=T).
Simulating the course of the infection for each possible combination takes O(T) time.
So the total runtime is O(NT2) - approximately 6.25M steps - which is fine.
'''

'''Simulate handshakes over time to see 
if data agrees with this choice of patient_zero and K...'''
def consistent_with_data (patient_zero_position, K, cowx, cowy, cow_ends_infected):
    infected = [False] * 101 #potential
    num_handshakes = [0] * 101 #like a dictionary with index the number of cows
    infected[patient_zero_position] = True
    for t in range(0, 251):
        x = cowx[t]
        y = cowy[t]
        if x > 0 and y > 0: #???
            if infected[x]:
                num_handshakes[x] += 1
            if infected[y]:
                num_handshakes[y] += 1
            if num_handshakes[x] <= K and infected[x]:
                infected[y] = True
            if num_handshakes[y] <= K and infected[y]:
                infected[x] = True

    #comparison problem
    for i in range(0, len(infected)):
        if infected[i] != cow_ends_infected[i]:
            return False
    return True

with open("tracing.in", "r") as input_file:
    line1 = input_file.readline().split()
    N = int(line1[0])
    T = int(line1[1])
    line2 = input_file.readline()
    cow_infected_final_state = [False] * 101
    for i in range(0, N):
        cow_infected_final_state[i+1] = line2[i] == '1'

    cowx = [0] * 251
    cowy = [0] * 251

    #avoid sorting time
    for i in range(0, T):
        line_t_x_y = input_file.readline().split()
        cowx[int(line_t_x_y[0])] = int(line_t_x_y[1])
        cowy[int(line_t_x_y[0])] = int(line_t_x_y[2])


    possible_i = [False] * 101
    possible_K = [False] * 252


    for i in range(1, N+1):
        for K in range(0, 252):
            if consistent_with_data(i, K, cowx, cowy, cow_infected_final_state):
                possible_i[i] = True
                possible_K[K] = True


    lower_K = 251
    upper_K = 0
    num_patient_zero = 0


    for index_K in range(0, 252):
        if possible_K[index_K]:
            lower_K = index_K
            break

    for index_K in range(251, -1, -1):
        if possible_K[index_K]:
            upper_K = index_K
            break

    for i in range(1, N+1):
        if possible_i[i]:
            num_patient_zero += 1

    with open("tracing.out", "w") as output_file:
        output_file.write(str(num_patient_zero) + " ")
        output_file.write(str(lower_K) + " ")
        if upper_K == 251:
            output_file.write("Infinity")
        else:
            output_file.write(str(upper_K))










