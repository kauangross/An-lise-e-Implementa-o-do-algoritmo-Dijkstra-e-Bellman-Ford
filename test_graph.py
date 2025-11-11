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
    assert path is not None
    assert dist != -1  # por exemplo, sabemos que não é o correto


def test_bellman_ford_funciona_com_peso_negativo(graph1):
    """
    Bellman-Ford deve encontrar o caminho correto mesmo com pesos negativos.
    """
    path, dist = graph1.shortest_path("A", "D", "bellman-ford")

    assert path == ["A", "F", "B", "D"]
    assert pytest.approx(dist, rel=1e-3) == -3.0  # distância esperada


def graph2():
    return Graph({
        "A": {"B": 4, "C": 2},
        "C": {"B": 2, "D": 3},
        "B": {"D": 3},
        "D": {}
    })
def test_dijkstra_sem_pesos_negativos(graph2):
    """
    Dijkstra deve funcionar corretamente em grafos sem pesos negativos.
    """

    path, dist = graph2.shortest_path("A", "D", "dijkstra")
    assert path == ["A", "C", "D"]
    assert dist == 5
