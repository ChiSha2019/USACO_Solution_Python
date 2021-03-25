def FFDFS(node):
    print(node)
    r = node[0]
    c = node[1]
    visited[r][c] = True
    if c-1>=0:
        if not visited[r][c-1]:
            FFDFS([r,c-1])
    if c+1 >= 4:
        if not visited[r][c+1]:
            FFDFS([r, c+1])
    if r- 1>=0:
        if not visited[r-1][c]:
            FFDFS([r-1, c])
    if r+1>=0:
        if not visited[r+1][c]:
            FFDFS([r+1, c])






table = [[2,2,2,1,1], [2,1,2,1,1],[2,2,2,2,1],[1,1,1,2,2],[1,1,1,1,1]]
startNode = [2,2]
visited = [[False]*5]*5
FFDFS(startNode)

