'''
idea:
1.Instead of removing the farms, we reverse the process by adding farms
2.When adding a new farm, increase number of disjoint set by one cuz it may result in a new dijoint set.
    check if its adjacent farm are already visited.
        If visited, we union them and decrease the number of disjoint set by one.
        Otherwise, do nothing
'''

class DisjSet:
    def __init__(self, n):
        # initialize sets of n items
        self.rank = [1] * (n+1)
        self.parent = [i for i in range(n+1)]
        self.parent[0] = -99

    # Finds set of given item x
    def find(self, x):

        if (self.parent[x] != x):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    '''def Union(self, x, y):

        xset = self.find(x)
        yset = self.find(y)

        if xset == yset:
            return

        self.parent[yset] = xset'''

    def Union(self, x, y):

        # Find current sets of x and y
        xset = self.find(x)
        yset = self.find(y)

        # If they are already in same set
        if xset == yset:
            return

        # Put smaller ranked item under
        # bigger ranked item if ranks are
        # different
        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset

        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset

        # If ranks are same, then move y under
        # x (doesn't matter which one goes where)
        # and increment rank of x's tree
        else:
            self.parent[yset] = xset
            self.rank[xset] = self.rank[xset] + 1


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

    with open("closing.out", "w") as output_file:
        close_node = [-1]*N
        for i in range(N):
            close_node[i] = int(input_file.readline())

        #revese the closing process, make it adding one by one
        close_node.reverse()
        disjSet = DisjSet(N)

        num_of_disjoint_set =0
        is_connected = []
        visited = [False] * (N + 1) #whether a node is currently inside of my graph
        for i in range(N):
            node_to_add = close_node[i]
            num_of_disjoint_set += 1

            #add any new edges
            visited[node_to_add] = True

            for adj_n in adjList[node_to_add]:
                #make sure this node and the adjacent node are all added in the graph
                #
                if visited[node_to_add] and visited[adj_n] and disjSet.find(node_to_add) != disjSet.find(adj_n):
                    disjSet.Union(node_to_add, adj_n)
                    num_of_disjoint_set -= 1 #union two set will decrease the number of disjset

            is_connected.append(num_of_disjoint_set == 1) # all connected is equivalent to num of disjoint set is 1

        #this is outputed reversely
        is_connected.reverse()
        for bool in  is_connected:
            if bool:
                output_file.write("YES" + "\n")
            else:
                output_file.write("NO" + "\n")





