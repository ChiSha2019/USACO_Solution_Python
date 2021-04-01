class DisjSet:
    def __init__(self, n):
        # initialize sets of n items
        self.rank = [1] * n
        self.parent = [i for i in range(n+1)]
        self.current_representitve = set()

    # Finds set of given item x
    def find(self, x):

        if (self.parent[x] != x):
            self.parent[x] = self.find(self.parent[x])
        else:
            self.current_representitve.add(x)
        return self.parent[x]

    def Union(self, x, y):

        xset = self.find(x)
        yset = self.find(y)

        if xset == yset:
            return

        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
            self.current_representitve.remove(xset)

        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
            self.current_representitve.remove(yset)

        else:
            self.parent[yset] = xset
            self.rank[xset] = self.rank[xset] + 1
            self.current_representitve.remove(yset)


with open("1.in", "r") as input_file:
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

    with open("closing.out", "w") as output_file:
        close_node = [None]*N
        for i in range(N):
            close_node[i] = int(input_file.readline())

        #revese the closing process, make it adding one by one
        close_node.reverse()
        disjSet = DisjSet(N)

        for n in adjList[close_node[0]]:
            disjSet.Union(n,close_node[0])

        is_connected = "NO"
        for i in range(0,N):
            #if this added node's parent is in existing_representitive
            rep_set = disjSet.current_representitve
            if disjSet.find(close_node[i]) in rep_set:
                is_connected = "YES"
            else:
                is_connected = "NO"
                #else create an independent graph with it's adj nodes
                for n in adjList[close_node[i]]:
                    disjSet.Union(n, close_node[0])
            output_file.write(is_connected + "\n")





