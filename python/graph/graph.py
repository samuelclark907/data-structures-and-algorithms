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
      output.append(vert)
    return output

  def get_neighbor(self, node):
    neighbors = self._adjacency_list[node]
    output = []
    for edge in neighbors:
      node = []
      node.append(edge.vertex.value)
      node.append(edge.weight)
      tuple_node = tuple(node)
      output.append(tuple_node)
      if len(output) == 0:
        return 'No Neighbors'
    return output

  def size(self):
    return len(self._adjacency_list)

  def breadth_first(self, vertex):
    breadth = []
    visited = []

    breadth.append(vertex)
    visited.append(vertex.value)

    while len(breadth) != 0:
        node = breadth.pop()
        neighbor = self._adjacency_list[node]
        for edge in neighbor:
            if edge.vertex.value not in visited:
                visited.append(edge.vertex.value)
                breadth.append(edge.vertex)
    return visited
    
  
  def get_edge(self, graph, list_cities):

    def get_starting_city(city_name):
      for node in graph.get_node():
        if node.value == city_name:
          return node
      return None

    start_city = get_starting_city(list_cities[0])

    
    for i in range(1,len(list_cities)):
      # print(list_cities[i])
      end_city = list_cities[i]
      neighbors = graph.get_neighbor(start_city)
      # print(end_city)
      for neighbor in neighbors:
        if neighbor[0] != end_city:
          return False
        if neighbor[0] == end_city:
          start_city = get_starting_city(end_city)
          print(start_city.value)
          available = True
          break
      return available



class Vertex:
  def __init__(self,value):
    self.value = value

class Edge:
  def __init__(self,vertex,weight=1):
    self.vertex = vertex
    self.weight = weight

if __name__ == '__main__':
    g = Graph()
    a = g.add_node('seattle')
    b = g.add_node('juneau')
    c = g.add_node('houston')
    cities = ['seattle', 'juneau', 'houston']
    # d = g.add_node('d')
    # print(g._adjacency_list)
    # keys = g._adjacency_list.keys()
    # lst = g.get_node()
    # print(lst)
    g.add_edge(a,b)
    # print(edge)
    # g.add_edge(b,c)
    # print(g.get_node())
    # print(g.get_neighbor(a))
    # hus = g.get_neighbor(b)
    # print(hus[0][0])
   
    print(g.get_edge(g,cities))