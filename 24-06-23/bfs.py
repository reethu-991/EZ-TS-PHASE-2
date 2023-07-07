#IMPLEMENTATION OF BFS 

#Here graph is a dictionary
#with keys and multiple values

graph={
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
}
#BFS- we use queue
visited=[] #List for visited node
queue=[] #Initialize a queue

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)

    while queue:#Creating loop to visit each loop
        m=queue.pop(0)
        print(m,end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

bfs(visited,graph,'5') #function call
