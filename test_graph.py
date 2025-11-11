import pytest
from graph import Graph

@pytest.fixture
def graph1():
    return Graph({
        "A": {"B": 4, "C": 2, "F": 40},
        "C": {"B": 2, "C": 3},
        "B": {"D": -3},
        "D": {},
        "F": {"B": -40}
    })

def test_dijkstra_caminho_errado_com_peso_negativo(graph1):
    """
    Dijkstra deve falhar (dar resultado incorreto) quando há pesos negativos.
    """
    path, dist = graph1.shortest_path("A", "D", "dijkstra")
    # O algoritmo não deve retornar -1 (resultado incorreto)
    # mas sim um valor incorreto diferente do Bellman-Ford
    assert path == ["A", "F", "B", "D"]
    assert pytest.approx(dist, rel=1e-3) == -3.0  # distância esperada


def test_bellman_ford_funciona_com_peso_negativo(graph1):
    """
    Bellman-Ford deve encontrar o caminho correto mesmo com pesos negativos.
    """
    path, dist = graph1.shortest_path("A", "D", "bellman-ford")

    assert path == ["A", "F", "B", "D"]
    assert pytest.approx(dist, rel=1e-3) == -3.0  # distância esperada

@pytest.fixture
def graph2():
    return Graph({
        "A": {"B": 4, "C": 2},
        "C": {"B": 2, "D": 3},
        "B": {"D": 3},
        "D": {}
    })

def test_dijkstra_sem_pesos_negativos(graph2):
    #Dijkstra deve funcionar corretamente em grafos sem pesos negativos.
    path, dist = graph2.shortest_path("A", "D", "dijkstra")
    assert path == ["A", "C", "D"]
    assert dist == 5

# Comparação de tempo 

@pytest.fixture
def graph3():
    return Graph({
        "A": {"B": 2, "C": 5, "D": 3},
        "B": {"A": 2, "E": 3, "F": 4},
        "C": {"A": 5, "F": 2, "G": 6},
        "D": {"A": 3, "G": 2, "H": 4},
        "E": {"B": 3, "I": 5, "J": 2},
        "F": {"B": 4, "C": 2, "J": 3, "K": 4},
        "G": {"C": 6, "D": 2, "K": 1, "L": 3},
        "H": {"D": 4, "L": 2, "M": 5},
        "I": {"E": 5, "M": 3, "N": 4},
        "J": {"E": 2, "F": 3, "N": 2, "O": 4},
        "K": {"F": 4, "G": 1, "O": 3, "P": 2},
        "L": {"G": 3, "H": 2, "P": 4, "Q": 3},
        "M": {"H": 5, "I": 3, "Q": 2, "R": 4},
        "N": {"I": 4, "J": 2, "R": 3, "S": 5},
        "O": {"J": 4, "K": 3, "S": 2, "T": 4},
        "P": {"K": 2, "L": 4, "T": 3, "U": 5},
        "Q": {"L": 3, "M": 2, "U": 2, "V": 4},
        "R": {"M": 4, "N": 3, "V": 3, "W": 2},
        "S": {"N": 5, "O": 2, "W": 3, "X": 4},
        "T": {"O": 4, "P": 3, "X": 2, "Y": 5},
        "U": {"P": 5, "Q": 2, "Y": 3, "Z": 4},
        "V": {"Q": 4, "R": 3, "Z": 2},
        "W": {"R": 2, "S": 3, "Z": 3},
        "X": {"S": 4, "T": 2, "Z": 3},
        "Y": {"T": 5, "U": 3, "Z": 2},
        "Z": {}
    })

def test_dijkstra_deve_funcionar(graph3):
    #Dijkstra deve funcionar corretamente em grafos sem pesos negativos.
    path, dist = graph3.shortest_path("A", "Z", "dijkstra")
    assert path == ["A", "D", "G", "K", "P", "T", "X", "Z"]
    assert dist == 16

def test_bellman_ford_deve_funcionar(graph3):
    #Dijkstra deve funcionar corretamente em grafos sem pesos negativos.
    path, dist = graph3.shortest_path("A", "Z", "bellman-ford")
    assert path == ["A", "D", "G", "K", "P", "T", "X", "Z"]
    assert dist == 16