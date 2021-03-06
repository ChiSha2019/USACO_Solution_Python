class Edge:
    def __init__(self, other_node, weight):
        self.other_node = other_node
        self.weight = weight


with open("mootube.in", "r") as input_file:
    line1 = input_file.readline().split()
    N = int(line1[0])
    Q = int(line1[1])
    adjList = {} #N+1 because list index starts from 0, but a node starts from 1

    #create an adjacentlist
    for i in range(N-1):
        line2 = input_file.readline().split()
        x = int(line2[0])
        y = int(line2[1])
        w = int(line2[2])
        if x in adjList:
            adjList[x].append([y,w])
        else:
            adjList[x] = [[y,w]]

        if y in adjList:
            adjList[y].append([x, w])
        else:
            adjList[y] = [[x, w]]

    visited = [False] * (N+1)
    stack = []

    # switch to an implementation of DFS that uses your own stack allocated independently of Java stack
    def dfs(node, k):
        visited[node] = True
        stack.append(node)
        while(len(stack) > 0):
            node = stack.pop()
            for next in adjList[node]:
                if (not visited[next[0]]) and next[1] >= k:
                    visited[next[0]] = True
                    stack.append(next[0])


    with open("mootube.out", "w") as output_file:
        for i in range(Q):
            line3 = input_file.readline().split()
            dfs(int(line3[1]), int(line3[0]))
            count = 0

            for item in visited:
                if item:
                    count += 1
            output_file.write(str(count - 1) + '\n')
            visited = [False] * (N+1)








