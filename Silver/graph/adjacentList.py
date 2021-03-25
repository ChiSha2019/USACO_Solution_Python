N = 6
M = 7

class Edge:
    def __init__(self, node, weight):
        self.n = node
        self.w = weight

ListNode = {}
ListNode[0] = [Edge(1,9),Edge(3,4),Edge(4,3)]
ListNode[1] = [Edge(0,9),Edge(2,5),Edge(3,2)]
ListNode[2] = [Edge(1,5),Edge(4,4),Edge(5,1)]
ListNode[3] = [Edge(0,4),Edge(1,2),Edge(5,3)]
ListNode[4] = [Edge(0,3),Edge(2,4)]
ListNode[5] = [Edge(2,1),Edge(3,3)]

print(ListNode)