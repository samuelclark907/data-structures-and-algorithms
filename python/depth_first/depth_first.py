from graph import Graph, Vertex

def dfs_graph(visited_nodes, graph, node):
    def get_starting_city(city_name):
        for node in graph.get_node():
            if node.value == city_name:
                return node
        return None

    visited_nodes = set()
    if node.value not in visited_nodes:
        visited_nodes.add(node.value)
        
        # print(node.value)
        for neighbor in graph.get_neighbor(node):
            neighbor = get_starting_city(f"{neighbor[0]}")
            dfs_graph(visited_nodes, graph, neighbor)
    print(visited_nodes)






if __name__ == '__main__':
    # print('Hello World')
    graphy = Graph()
    a = graphy.add_node('a')
    b = graphy.add_node('b')
    c = graphy.add_node('c')
    d = graphy.add_node('d')
    e = graphy.add_node('e')
    f = graphy.add_node('f')
    g = graphy.add_node('g')
    h = graphy.add_node('h')
    graphy.add_edge(a, b)
    graphy.add_edge(b, c)
    graphy.add_edge(c, g)
    graphy.add_edge(b, d)
    graphy.add_edge(a, d)
    graphy.add_edge(b, d)
    graphy.add_edge(d, e)
    graphy.add_edge(d, h)
    graphy.add_edge(d, f)
    graphy.add_edge(f, h)
    

    # print(g._adjacency_list)
    visited_nodes = set()
    # print(g.get_neighbor(a))
    dfs_graph(visited_nodes, graphy, a)