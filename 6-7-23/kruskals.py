def kruskals(graph):
    edge_list=[]
    for source in graph:
        for edge in graph[source]:
            weight,dest=edge
            edge_list.append((weight,source,dest))
    edge_list.sort()
    print(*edge_list,sep='\n')
    parents={}
    for vertex in graph:
        parents[vertex]=vertex
    print(parents)
    mst=[]
    def find_parent(vertex):
        if parents[vertex]!=vertex:
            parents[vertex]=find_parent(parents[vertex])
        return parents[vertex]
    
    for edge in edge_list:
        weight,source,dest=edge
        if find_parent(source)!=find_parent(dest):
            mst.append(edge)
            parents[find_parent(source)]=find_parent(dest)
    print(parents)
    return mst
graph={
    'A':[(10,'F'),(28,'B')],
    'B':[(14,'G'),(16,'C'),(28,'A')],
    'C':[(16,'B'),(12,'D')],
    'D':[(12,'C'),(22,'E'),(18,'G')],
    'E':[(22,'D'),(25,'F'),(24,'G')],
    'F':[(10,'A'),(25,'E')],
    'G':[(14,'B'),(18,'D'),(24,'E')],
}
mst=kruskals(graph)
print(mst)
