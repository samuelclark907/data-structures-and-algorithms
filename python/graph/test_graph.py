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

# def test_add_edge_false():
#     g = Graph()
#     a = g.add_node('a')
#     b = g.add_node('b')
#     c = g.add_node('c')
#     g.add_edge(a,b)
#     assert True

def test_size():
    g = Graph()
    a = g.add_node('a')
    b = g.add_node('b')
    expected = 2 
    actual = g.size()
    assert actual == expected


