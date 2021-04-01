#Remaking the graph and running the search takes O(n+m) time.
#Since there are a total of n barn closings, we have a O(n2+nm) algorithm
with open("closing.in", "r") as input_file:
    line1 = input_file.readline().split()
    N = int(line1[0])
    M = int(line1[1])
    adjList = {}

    #create an adjacentlist
    for i in range(M):
        line2 = input_file.readline().split()
        x = int(line2[0])
        y = int(line2[1])
        if x in adjList:
            adjList[x].append(y)
        else:
            adjList[x] = [y]

        if y in adjList:
            adjList[y].append(x)
        else:
            adjList[y] = [x]

    visited = [False] * (N+1)
    stack = []

    # switch to an implementation of DFS that uses your own stack allocated independently of Java stack
    def dfs(node):
        visited[node] = True
        stack.append(node)
        while len(stack) > 0:
            node = stack.pop()
            if node in adjList:
                for next in adjList[node]:
                    if not visited[next]:
                        visited[next] = True
                        stack.append(next)

    def update_adjlist(nodeToBeDeleted):
        adjList.pop(nodeToBeDeleted)


    with open("closing.out", "w") as output_file:
        for i in range(N):
            visited = [False] * (N + 1)
            node = int(input_file.readline())
            dfs(node)

            #update adjacentlist!
            update_adjlist(node)

            #check if all remaining nodes connected
            is_all_connected = "YES"
            for n in adjList:
                if not visited[n]:
                    is_all_connected = "NO"
                    break

            output_file.write(is_all_connected + '\n')
