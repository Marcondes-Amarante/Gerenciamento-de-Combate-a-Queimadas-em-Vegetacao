## Descrição

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

# Relatório:

## Descrição das decisões de implementação

## Análise dos resultados obtidos

## Desafios encontrados

Encontramos diversos desafios ao longo

## Possíveis melhorias

- implementação de instruções utilizando a biblioteca networkx para única e estritamente gerar a exibição do estado final do grafo pra cada simulação, atualmente já temos o arquivo desenhar que utiliza a biblioteca citada para gerar a visualização do grafo construído através do arquivo de entrada, mas não integramos ao escopo do programa principal
- implementação de mecanismos de tratamentos de erro quanto a dados incorretos ou insuficientes passados no arquivo de entrada