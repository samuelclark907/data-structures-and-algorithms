class Graph:
  def __init__(self):
    self._adjacency_list = {}

  def add_node(self,value):
    v = Vertex(value)
    self._adjacency_list[v] = []
    return v

  def add_edge(self,start_vertex,end_vertex,weight=1):
    if start_vertex not in self._adjacency_list:
      return "Start vertex not here"
    if end_vertex not in self._adjacency_list:
      return "End vertex not here"
    edge = Edge(end_vertex,weight)
    adjacencies = self._adjacency_list[start_vertex]
    adjacencies.append(edge)
    return (start_vertex.value, end_vertex.value, weight)

  def get_node(self):
    output = []
    if self.size() == 0:
      return 'NULL'
    for vert in self._adjacency_list:
      output.append(vert.value)
    return output

  def get_neighbor(self, node):
    neighbors = self._adjacency_list[node]
    output = []
    for edge in neighbors:
      lst = []
      lst.append((edge.vertex.value, edge.weight))
      output.append(lst)
    return output

  def size(self):
    return len(self._adjacency_list)

class Vertex:
  def __init__(self,value):
    self.value = value

class Edge:
  def __init__(self,vertex,weight=1):
    self.vertex = vertex
    self.weight = weight

if __name__ == '__main__':
    g = Graph()
    a = g.add_node('a')
    b = g.add_node('b')
    c = g.add_node('c')
    d = g.add_node('d')
    # print(g._adjacency_list)
    # keys = g._adjacency_list.keys()
    # lst = g.get_node()
    # print(lst)
    g.add_edge(a,b)
    # print(edge)
    g.add_edge(a,c)
    print(g.get_neighbor(a))
    neighbors = g.get_neighbor(a)
    print(neighbors[0][0][0])