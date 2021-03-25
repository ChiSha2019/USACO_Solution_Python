
ListNode = {}
ListNode[0] = [1,3,4]
ListNode[1] = [0,2,3]
ListNode[2] = [1,4,5]
ListNode[3] = [0,1,5]
ListNode[4] = [0,2]
ListNode[5] = [2,3]

isVisited = [False] * len(ListNode)
queue = []
def bfs(node):
    queue.append(node)
    while len(queue) > 0:
        head = queue.pop()
        for n in ListNode[head]:
            if not isVisited:
                print(n)
                queue.append(n)
