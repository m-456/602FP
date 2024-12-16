# Robert Plastina
# Provides functions that solve for Graphs.

class GraphDFS:
    def __init__(self):
        self.__adjList = {}

    def addEdge(self, src, dest):
        if src not in self.__adjList:
            self.__adjList[src] = []
        if dest not in self.__adjList:
            self.__adjList[dest] = []
        self.__adjList[src].append(dest)
        self.__adjList[dest].append(src)

    def runDFS(self, start):
        list = []
        list.append((start, None))  # (node, parent)

        visited = set()
        discTime = {}
        lowTime = {}
        pred = {start: None}
        apSet = set()
        timeCtr = [1]

        while list:
            curr, parent = list[-1]

            if curr not in visited:
                visited.add(curr)
                discTime[curr] = lowTime[curr] = timeCtr[0]
                timeCtr[0] += 1
                childCnt = 0


                for nbr in sorted(self.__adjList[curr]):
                    if nbr not in visited:
                        list.append((nbr, curr))
                        pred[nbr] = curr
                        childCnt += 1

                    elif nbr != parent:
                        lowTime[curr] = min(lowTime[curr], discTime[nbr])


                if parent is not None and lowTime[curr] >= discTime[parent]:
                    apSet.add(parent)
                if parent is None and childCnt > 1:
                    apSet.add(curr)

            else:
                list.pop()
                if parent is not None:
                    lowTime[parent] = min(lowTime[parent], lowTime[curr])

        return discTime, pred, apSet


class Kruskal:
    def __init__(self):
        self.__edges = []

    def kEdge(self, src, dest, weight):
        self.__edges.append((src, dest, weight))

    def find(self, parent, i):
        if parent[i] == i:
            return i
        else:
            parent[i] = self.find(parent, parent[i])
            return parent[i]

    def union(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)

        if x_root != y_root:
            if rank[x_root] < rank[y_root]:
                parent[x_root] = y_root
            elif rank[x_root] > rank[y_root]:
                parent[y_root] = x_root
            else:
                parent[y_root] = x_root
                rank[x_root] += 1

    def runKruskal(self):
        self.__edges.sort(key=lambda edge: edge[2])

        parent = {}
        rank = {}
        mst = []
        t_weight = 0

        for edge in self.__edges:
            src, dest, weight = edge
            if src not in parent:
                parent[src] = src
                rank[src] = 0
            if dest not in parent:
                parent[dest] = dest
                rank[dest] = 0

        for src, dest, weight in self.__edges:
            x = self.find(parent, src)
            y = self.find(parent, dest)

            if x != y:
                mst.append((src, dest, weight))
                t_weight += weight
                self.union(parent, rank, x, y)

        return mst, t_weight
