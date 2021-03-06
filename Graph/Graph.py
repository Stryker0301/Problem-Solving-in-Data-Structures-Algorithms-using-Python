#!/usr/bin/env python
import heapq
from collections import deque

class Graph(object):
    class AdjNode(object):
        def __init__(self, src, dst, cst=1):
            self.source = src
            self.destination = dst
            self.cost = cst
            self.next = None

    class AdjList(object):
        def __init__(self):
            self.head = None
            

    def __init__(self, cnt):
        self.count = cnt
        self.array = [None] * cnt
        i = 0
        while i < cnt:
            self.array[i] = self.AdjList()
            self.array[i].head = None
            i += 1
    
    def AddEdge(self, source, destination, cost=1):
        node = self.AdjNode(source, destination, cost)
        node.next = self.array[source].head
        self.array[source].head = node
    
    def AddBiEdge(self, source, destination, cost=1):
        self.AddEdge(source, destination, cost)
        self.AddEdge(destination, source, cost)

    def Print(self):
        ad = self.AdjNode()
        i = 0
        while i < self.count:
            ad = self.array[i].head
            if ad != None:
                print "Vertex " , i , " is connected to : ",
                while ad != None:
                    print ad.destination,
                    ad = ad.next
                print ""
            i += 1

    @classmethod
    def Dijkstra(cls, gph, source):
        previous = [-1] * gph.count
        dist = [sys.maxint] * gph.count

        dist[source] = 0
        previous[source] = -1

        pqarray = []
        node = cls.AdjNode(source, source, 0)        
        heapq.heappush(pqarray, (0, node))
        
        while len(pqarray) != 0:
            val = heapq.heappop(pqarray)
            node = val[1]
            
            adl = gph.array[node.destination]
            adn = adl.head
            
            while adn != None:
                alt = adn.cost + dist[adn.source]
                if alt < dist[adn.destination]:
                    dist[adn.destination] = alt
                    previous[adn.destination] = adn.source
                    node = cls.AdjNode(adn.source, adn.destination, alt)
                    heapq.heappush(pqarray, (alt, node))
                adn = adn.next
        count = gph.count
        i = 0
        while i < count:
            if dist[i] == sys.maxint:
                print "node id" , i , "prev" , previous[i] , "distance : Unreachable"
            else:
                print "node id" , i , "prev" , previous[i] , "distance :" , dist[i]
            i += 1
            
    @classmethod
    def Prims(cls, gph):
        previous = [-1] * gph.count
        dist = [sys.maxint] * gph.count
        source = 1
        dist[source] = 0
        previous[source] = -1

        pqarray = []
        node = cls.AdjNode(source, source, 0)        
        heapq.heappush(pqarray, (0, node))
        
        while len(pqarray) != 0:
            val = heapq.heappop(pqarray)
            node = val[1]
            
            if dist[node.destination] < node.cost:
                continue
            
            dist[node.destination] = node.cost;
            previous[node.destination] = node.source;
            
            adl = gph.array[node.destination]
            adn = adl.head
            
            while adn != None:
                if previous[adn.destination]==-1:
                    node = cls.AdjNode(adn.source, adn.destination, adn.cost)
                    heapq.heappush(pqarray, (adn.cost, node))
                adn = adn.next
        count = gph.count
        i = 0
        while i < count:
            if dist[i] == sys.maxint:
                print "node id" , i , "prev" , previous[i] , "distance : Unreachable"
            else:
                print "node id" , i , "prev" , previous[i] , "distance :" , dist[i]
            i += 1
            
 
    @classmethod
    def TopologicalSortDFS(cls, gph, index, visited, stk):
        head = gph.array[index].head
        while head != None:
            if visited[head.destination] == 0:
                visited[head.destination] = 1
                cls.TopologicalSortDFS(gph, head.destination, visited, stk)
            head = head.next
        stk.append(index)
 
    @classmethod
    def TopologicalSort(cls, gph):
        stk = []
        count = gph.count
        visited = [0] * count
        i = 0
        while i < count:
            if visited[i] == 0:
                visited[i] = 1
                cls.TopologicalSortDFS(gph, i, visited, stk)
            i += 1
        while len(stk) != 0:
            print stk.pop(),
 
    @classmethod
    def PathExist(cls, gph, source, destination):
        count = gph.count
        visited = [False] * count
        visited[source] = True
        cls.DFSRec(gph, source, visited)
        return visited[destination]
    
    @classmethod
    def DFSRec(cls, gph, index, visited):
        head = gph.array[index].head
        while head != None:
            if visited[head.destination] == False:
                visited[head.destination] = True
                cls.DFSRec(gph, head.destination, visited)
            head = head.next
    
    @classmethod
    def isConnected(cls, gph):
        count = gph.count
        visited = [False] * count
        visited[0] = True
        cls.DFSRec(gph, 0, visited)
        i = 0
        while i < count:
            if visited[i] == False:
                return False
            i += 1
        return True
    
    @classmethod
    def DFSStack(cls, gph):
        count = gph.count
        visited = [0] * count
        stk = []
        visited[0] = 1
        stk.append(object)
        while len(stk) != 0:
            curr = stk.pop()
            head = gph.array[curr].head
            while head != None:
                if visited[head.destination] == 0:
                    visited[head.destination] = 1
                    cls.append(head.destination)
                head = head.next
 
    @classmethod
    def DFS(cls, gph):
        count = gph.count
        visited = [0] * count
        i = 0
        while i < count:
            if visited[i] == 0:
                visited[i] = 1
                cls.DFSRec(gph, i, visited)
            i += 1
 
    @classmethod
    def BFSQueue(cls, gph, index, visited):
        que = deque([])
        visited[index] = 1
        que.append(index)
        while len(que) != 0:
            curr = que.popleft()
            head = gph.array[curr].head
            while head != None:
                if visited[head.destination] == 0:
                    visited[head.destination] = 1
                    que.append(head.destination)
                head = head.next
 
    @classmethod
    def BFS(cls, gph):
        count = gph.count
        visited = [0] * count
        i = 0
        while i < count:
            if visited[i] == 0:
                cls.BFSQueue(gph, i, visited)
            i += 1
            
    @classmethod
    def ShortestPath(cls, gph, source):
        count = gph.count
        distance = [-1] * count
        path = [-1] * count
        que = deque([])

        que.append(source)
        distance[source] = 0
        while len(que) != 0:
            curr = que.popleft()
            head = gph.array[curr].head
            while head != None:
                if distance[head.destination] == -1:
                    distance[head.destination] = distance[curr] + 1
                    path[head.destination] = curr
                    que.append(head.destination)
                head = head.next
        i = 0
        while i < count:
            print path[i] , "to" , i , "weight" , distance[i]
            i += 1
 
    @classmethod
    def BellmanFordShortestPath(cls, gph, source):
        count = gph.count
        distance = [sys.maxint] * count
        path = [-1] * count

        distance[source] = 0
        i = 0
        while i < count - 1:
            j = 0
            while j < count:
                head = gph.array[j].head
                while head != None:
                    newDistance = distance[j] + head.cost
                    if distance[head.destination] > newDistance:
                        distance[head.destination] = newDistance
                        path[head.destination] = j
                    head = head.next
                j += 1
            i += 1
            
        i = 0
        while i < count:
            print path[i] , "to" , i , "weight" , distance[i]
            i += 1 
    
    @classmethod
    def main(cls, args):
        gph = Graph(9)
        gph.AddBiEdge(0, 2, 1)
        gph.AddBiEdge(1, 2, 5)
        gph.AddBiEdge(1, 3, 7)
        gph.AddBiEdge(1, 4, 9)
        gph.AddBiEdge(3, 2, 2)
        gph.AddBiEdge(3, 5, 4)
        gph.AddBiEdge(4, 5, 6)
        gph.AddBiEdge(4, 6, 3)
        gph.AddBiEdge(5, 7, 1)
        gph.AddBiEdge(6, 7, 7)
        gph.AddBiEdge(7, 8, 17)
        cls.Dijkstra(gph, 1)
        # cls.Prims(gph)
        """print cls.PathExist(gph, 1, 5)
        print cls.isConnected(gph)
        cls.ShortestPath(gph, 1)
        cls.BellmanFordShortestPath(gph, 1)
        g = Graph(6);
        g.AddEdge(5, 2);
        g.AddEdge(5, 0);
        g.AddEdge(4, 0);
        g.AddEdge(4, 1);
        g.AddEdge(2, 3);
        g.AddEdge(3, 1);
        print "Topological Sort::",
        Graph.TopologicalSort(g);"""

if __name__ == '__main__':
    import sys
    Graph.main(sys.argv)
