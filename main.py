import parse
import BFS
import Dijkstra

import os

#inicializando grafo
Grafo = parse.obterDados()
Grafo.listar_Prop()

#criando pasta para armazenar logs da simulaçao executada para cada vértice (caso ainda não exista)
pasta = "logs"
os.makedirs(pasta, exist_ok=True)

#filtrando lista de vértices do grafo para conter apenas vértices de vegetação
vegetacoes = [v.pos for v in Grafo.vertices if v.tipo == 'v']


#programa executa simulação enquanto houver focos ativos no grafo
for vegetacao in vegetacoes:
    
    tempo = 0

    parse.inicializandoFoco(Grafo, vegetacao, Grafo.capacidadeCaminhoes)

    #criando arquivo de log para o vértice de vegetação iterado
    caminho =  os.path.join(pasta, f"log_{vegetacao}.txt")

    with open(caminho, "w") as arquivo_log:
    
        arquivo_log.write(f"\nsimulação do incêndio a partir de {Grafo.vertices[vegetacao].nome} \n")

        while Grafo.focos:

            arquivo_log.write(f"\nTempo {tempo}:\n")

            arquivo_log.write("\nAção do fogo: \n")
            BFS.bfsMod(Grafo, arquivo_log)

            arquivo_log.write("\nAção dos brigadistas \n")
            Dijkstra.acaoBrigadistas(Grafo, arquivo_log)
            
            tempo += 1

        if(not Grafo.focos):
            arquivo_log.write("incêndio conclúido \n")

            arquivo_log.write("\nRelatório final da simulação: \n")

            if(len(Grafo.focosQueimados) > 0):
                arquivo_log.write(f"tempo total da simualação: {tempo} \n")
            else:
                arquivo_log.write(f"tempo necessário para conter fogo: {tempo} unidades de tempo \n") #[OK]

            arquivo_log.write(f"quantidade de vértices totalmente queimados: {len(Grafo.focosQueimados)} \n") #[OK]
            arquivo_log.write(f"quantidade de vértices salvos: {Grafo.qtdFocosSalvos} \n") #[OK]
            arquivo_log.write(f"quantidade de equipes mobilizadas: {len(Grafo.equipesMobilizadas)} \n") #[OK]
            arquivo_log.write(f"quantidade de reabastecimentos efetuados: {Grafo.reabastecimentos} \n") #[OK] 
            arquivo_log.write(f"quantidade de água gasta: {Grafo.qtdAguaUtilizada}L\n") #[OK]

    #resetando atributos do grafo de acompanhamento e registro da simulação
    Grafo.resetarAtributos(Grafo.capacidadeCaminhoes)



    