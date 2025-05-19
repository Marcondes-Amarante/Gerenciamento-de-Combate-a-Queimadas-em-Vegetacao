# Sistema de simulação e gerenciamento de combate a incêndios

O presente projeto consiste em uma algoritmo de simulação de incêndio representado como grafo que utiliza algoritmos clássicos de busca e caminho mínimo (BFS e dijkstra) para representação dos comportamentos de propagação do fogo e ação de brigadistas.

# Instruções de execução

### Como executar o programa:

1. Clone ou baixe o repositório.

2. Abra a pasta do projeto com sua IDE ou terminal.

3. Execute o arquivo main.py.
O programa criará uma pasta chamada logs, onde serão salvos:
- Arquivos .txt contendo detalhes das ações da simulação a partir de cada vértice de vegetação, e um relatório final com métricas como:
    - Vértices salvos/queimados
    - Tempo total da simulação, entre outros.

### Sobre o arquivo de entrada (grafo):
Já existe um arquivo de entrada com:
- Vértices (brigada, coleta, vegetação),
- Arestas com pesos,
- Caminhões e suas capacidades,
- Equipes por brigada.
O programa será executado normalmente sem modificações, contudo, não impede que vocês possa modificá-lo seguindo as instruções abaixo:

### Como editar o grafo:
- Vértices:
    - Localize a linha #vertices.
    - Na linha seguinte, liste os vértices em [ ] separados por vírgulas.
    - Adicione -b (brigada) ou -c (coleta) após o número do vértice, se aplicável.
    - Se não houver especificação de tipo o vértice será considerado como vegetação.

- Arestas:
    - Localize #arestas e pesos.
    - Adicione uma linha com os dois vértices separados por vírgula e o peso após =.
    Ex: 1,2=10.

- Caminhões por brigada:
    - Localize #quantidade de caminhoes por posto de brigada e suas capacidades.
    - na linha seguinte informe quantidade e capacidade separados por vírgula.

- Equipes por brigada:
    - Localize #quantidade de equipes por posto de brigada.
    - Na linha seguinte adicione apenas a quantidade de equipes.

### Saída esperada:
Arquivos txt. para cada vértice de vegetação, armazenados na pasta "logs", contendo o detalhamento e relatório final da simulação gerada a partir de cada um desse vértices, de modo que para acessar o que ocorreu na simulação dos mesmos basta apenas acessar o arquivo txt da pasta "logs" correspondente ao vértice desejado. 

Ex: para ver o detalhamento da simulação gerada a partir do vértice 10 basta apenas abrir o arquivo txt "log_10", lá encontra-se listada todas as ações assumidas pelo fogo e brigadistas a cada turno da simulação iniciada a partir do mesmo.