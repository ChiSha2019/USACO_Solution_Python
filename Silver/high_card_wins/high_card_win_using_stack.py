with open("highcard.in", "r") as input_file:
    N = int(input_file.readline())
    whole_card = [False] * (2*N+1)  # bessie is false
    for i in range(N):
        else_card = int(input_file.readline())
        whole_card[else_card] = True

    stack = []
    score = 0
    # when we have a elsie we push it to the stack, otherwise we pop it.
    #when stack is empty and we have a bessie, we skip
    for i in range(1, 2*N+1):
        if whole_card[i]:
            stack.append(i)
        elif len(stack) != 0:
            stack.pop()
            score += 1

    with open("highcard.out", "w") as output_file:
        output_file.write(str(score))