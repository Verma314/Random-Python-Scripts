#code
#https://practice.geeksforgeeks.org/problems/snake-and-ladder-problem/0

import math

class Graph:
    def __init__(self):
        self.adjacents = {}
        self.vertices = 0
        self.edgeWeightRepo = {} 
        
    def addEdge( self, node1, node2):
        if ( node1 in self.adjacents.keys()):
            self.adjacents[node1] += [node2]
        else:
            self.adjacents[node1] = [node2]
    
    def getAdjacentVertices( self, node):
        return ( self.adjacents[node])
            
    def setWeight(self, node_a, node_b,weight):
        self.edgeWeightRepo[(node_a,node_b)] = weight
        
    def getWeight(self, node_a, node_b):
        return self.edgeWeightRepo[(node_a,node_b)]
    
    def show(self):
        return ( self.adjacents)
        
class Paths:
    def __init__(self,graph, source,target):
        self.counted = 0
        self.marked = {}
        self.graph = graph
        self.source = source
        self.target = target
        
        self.seq = []
        
        self.edgeTo = {}
        self.distTo = {}
        self.priorityQueue = {}
        
        for i in graph.show().keys():
            self.distTo[i] = math.inf
            
        for vertex in self.graph.show().keys():
            self.marked[vertex] = False
        
        self.distTo[source] = 0
        self.priorityQueue[source] = 0
                
        while ( self.priorityQueue != {} ):
            minTup = min(self.priorityQueue.items(), key=lambda kv: kv[1])
            del self.priorityQueue[minTup[0]]
            
            for adjNode in self.graph.getAdjacentVertices(minTup[0]):
                self.relax(minTup[0],adjNode)
                
        print (self.distTo[target]  ) 
        
        self.seq = [target]
        self.edgeTo[1] = None
        self.edgeTo[0] = None
        finalEdge = self.edgeTo[target]
        
        while ( finalEdge != None ):
            self.seq += [finalEdge]
            finalEdge = self.edgeTo[finalEdge]
        #print ("the seq is" +  str(self.seq))            
        
    def relax (self,start,end ):
        jumpMetric = self.graph.getWeight(start,end)
        if ( self.distTo[end] > self.distTo[start] + jumpMetric):
            self.distTo[end] = self.distTo[start] + jumpMetric
            self.edgeTo[end] = start
            self.priorityQueue[end] = self.distTo[end]
            
                   
T = int(input().strip())

while ( T > 0 ):
    noOfedges = int(input().strip())
    edges_ =  [int(i) for i in input().strip().split(" ")]
    edges = [edges_[i:i+2] for i in range(0,len(edges_),2)]

    graph = Graph()
    
    #initialize the graph
    for edge in range(1,31):
        for jump in range(1,7):
            if ( edge + jump <= 30):
                graph.setWeight(edge,edge + jump, 1)
                graph.addEdge ( edge, edge + jump)
    
    #edge case
    graph.setWeight(30,30,0)   
    graph.addEdge(30,30)
    
    for edge in edges:
        graph.setWeight(edge[0],edge[1], 0)
        graph.addEdge ( edge[0],edge[1])

    p = Paths (graph, 1, 30)
    T -= 1
