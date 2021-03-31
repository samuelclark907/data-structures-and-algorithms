import pytest
from graph import Vertex, Graph, Edge

def test_add_vertex_pass():
    vertex = Vertex('a')
    actual = vertex.value
    expected = 'a'
    assert actual == expected

def test_add_vertex_fail():
    vertex = Vertex('a')
    actual = vertex.value
    expected = 'b'
    assert actual != expected

def test_add_node():
    g = Graph()
    expected = 'a'
    actual = g.add_node('a').value
    assert expected == actual


def test_add_edge_true():
    g = Graph()
    a = g.add_node('a')
    b = g.add_node('b')
    g.add_edge(a,b)
    assert True


def test_size():
    g = Graph()
    a = g.add_node('a')
    b = g.add_node('b')
    expected = 2 
    actual = g.size()
    assert actual == expected

def test_graph_empty():
    g = Graph()
    expected = 'NULL' 
    actual = g.get_node()
    assert actual == expected


def test_get_node():
    g = Graph()
    a = g.add_node('a')
    b = g.add_node('b')
    expected = ['a', 'b'] 
    actual = g.get_node()
    assert actual == expected

def test_get_neighbor():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    graph.add_edge(a, b)
    graph.add_edge(b, a)
    graph.add_edge(b, c)
    actual = graph.get_neighbor(b)
    expected = [[('a', 1)], [('c', 1)]]
    assert actual == expected

def test_one_node_and_edge():
    graph = Graph()
    a = graph.add_node('a')
    graph.add_edge(a, a)
    actual = graph.get_neighbor(a)
    expected = [[('a',1)]]
    assert actual == expected


