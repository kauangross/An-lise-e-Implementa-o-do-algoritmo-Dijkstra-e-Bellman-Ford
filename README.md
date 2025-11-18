Este repositório contém a implementação dos algoritmos Dijkstra e Bellman–Ford, focado em estudo, entendimento e análise prática do comportamento de ambos.
Os testes foram escritos utilizando pytest, permitindo validar os resultados e medir o tempo de execução de cada algoritmo em grafos de teste.

# 📌 Objetivo do Trabalho
* Implementar os algoritmos Dijkstra e Bellman–Ford.
* Comparar os dois algoritmos.
* Entender o funcionamento interno de cada um:
* Relaxamento de arestas
* Propagação das distâncias
* Detecção de ciclos negativos (Bellman–Ford)
* Testar e comparar o tempo de execução entre os dois.
* Validar a corretude das implementações utilizando pytest.

# 🚀 Dijkstra
* O algoritmo de Dijkstra resolve o problema do caminho mínimo a partir de uma origem em grafos com pesos não negativos.
* Ele utiliza uma priority queue (heap) para sempre expandir o vértice com menor distância conhecida, tornando-o bastante eficiente.

## Características principais:
* Não funciona com pesos negativos.
* Muito rápido em grafos grandes.
* Usa heap para escolher o próximo vértice mais promissor.

# 🔁 Bellman–Ford
* Bellman–Ford calcula caminhos mínimos mesmo quando o grafo possui arestas com pesos negativos.
* Ele repete o processo de relaxamento de todas as arestas várias vezes até garantir que todas as distâncias foram propagadas corretamente.

## Características principais:
* Suporta pesos negativos.
* Detecta ciclos de peso negativo.
* Mais lento que Dijkstra, pois repete o relaxamento por várias iterações.

# ▶️ Como Executar o Projeto
Instale o Python 3.10+ <br/>

Clone o repositório:
```git clone https://github.com/SEU_USUARIO/SEU_REPO.git``` <br/><br/>
```cd SEU_REPO``` <br/><br/>
Execute os testes:<br/>
```python tests.py```
O terminal exibirá os tempos e os resultados de cada algoritmo.

# 🧪 Testes com Pytest
Para rodar os testes comm pytest execute: <br/>
```pytest``` 

Caso prefira, instale a extensão de testes do Pytest correspondente na sua IDE e utilize a interface disponibilizada.

# 🧪 Testes Locais (in-code)
Também foi colocado alguns testes dentro do código "Graph.py" que utilizam funções que iniciam com "graph" e retornam um grafo.<br/>
Exemplo: "graph1()", "graphTestTime()"

## Os testes incluem:
* Verificação das distâncias retornadas.
* Reconstrução de caminhos.
* Erros causados por pesos negativos e ciclos negativos.
* Verificação de desempenho (tempo).
