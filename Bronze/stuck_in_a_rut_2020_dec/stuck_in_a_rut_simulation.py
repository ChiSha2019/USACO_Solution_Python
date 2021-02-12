import sys

N = int(sys.stdin.readline())

cows = []
for i in range(N):
    each_line = []
    each_line1 = sys.stdin.readline().split()
    # convert each line into "string" "int" "int"
    each_line.append(each_line1[0])
    each_line.append(int(each_line1[1]))
    each_line.append(int(each_line1[2]))
    cows.append(each_line)

'''create a square board to move'''
board_size = 0  # board size should be the max distance of two cows
for i in range(N):
    x = cows[i][1]
    y = cows[i][2]
    if x + 1 > board_size:
        board_size = x + 1
    if y + 1 > board_size:
        board_size = y + 1

board = [[0] * board_size for _ in range(board_size)]
previous_board = [row[:] for row in board]



'''cows numbered from 0 to N-1'''
'''board initializetion'''
for i in range(0, N):
    x = cows[i][1]
    y = cows[i][2]
    board[x][y] = 1
    previous_board[x][y] = 1

cows_step = [1] * N
cows_shall_stop = [False] * N

'''simulation'''
for t in range(0, board_size):
    '''
    for i in range(board_size):
        print(board[i])
    print("------------------------")
    '''

    for num in range(0, N):  # every cows moves by 1 step
        x = cows[num][1]
        y = cows[num][2]
        if not cows_shall_stop[num]:
            if cows[num][0] == "N":
                if y + 1 > board_size - 1:
                    cows_step[num] = -1  # infinity
                    cows_shall_stop[num] = True  # if moving out of board, no need to do more simulation
                elif previous_board[x][y + 1] == 0:  # no other cow has arrived here before
                    board[x][y + 1] = 1
                    cows_step[num] += 1
                    cows[num][2] = y + 1 #update cow's current position
                else:
                    cows_shall_stop[num] = True

            if cows[num][0] == "E":
                #print("num = " + str(num) + " x+1 = " + str(x + 1))
                if x + 1 > board_size - 1:
                    cows_step[num] = -1  # infinity
                    cows_shall_stop[num] = True #mark it stop cuz we dont want any more calculation about this cow
                elif previous_board[x + 1][y] == 0:  # no other cow has arrived here before
                    board[x + 1][y] = 1
                    cows_step[num] += 1
                    cows[num][1] = x + 1 #update cow's current position
                else:
                    cows_shall_stop[num] = True

    '''update previous border with the new border after all the cows made their move'''
    for i in range(0, N):
        x = cows[i][1]
        y = cows[i][2]
        previous_board[x][y] = 1
    #print(cows)
    #previous_board = [x[:] for x in board]

for item in cows_step:
    if item == -1:
        print("Infinity")
    else:
        print(str(item))
