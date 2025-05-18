import grafos as gf
import vertice as ver
import random

def obterDados():

    G = gf.grafo()

    with open('arquivoLeitura.txt', 'r') as arquivo:
        
        #retornando lista de linhas do arquivo
        linhas = arquivo.readlines()
            
        i=0
        
        while(i < len(linhas)):

            #verificando marcador de linha
            if linhas[i].startswith("#"):
             
                parametro = linhas[i]
                i+=1

                #obtendo e adicionando vértices de acordo com os tipos indicados
                if("vertices" in parametro):

                    #obtendo conteúdo entre '[]'
                    inicio = linhas[i].find("[")
                    fim = linhas[i].find("]")

                    #segmentando conteudo da linha usando ',' como separador
                    conteudo = linhas[i][inicio+1:fim].split(",")

                    entrada = []

                    #removendo espaços
                    for item in conteudo:
                        entrada.append(item.strip())
                    
                    #adicionando vértices no grafo de acordo com o seu tipo indicado na entrada
                    for vertice in entrada:

                        if("-b" in vertice):
                            vertice = vertice.replace("-b", "")
                            int(vertice)
                            G.insere_ver("b")

                        elif ("-c" in vertice):
                            vertice = vertice.replace("-c", "")
                            int(vertice)
                            G.insere_ver("c")

                        else:
                            int(vertice)
                            G.insere_ver("v")
                    
                    print("\nvértices carregados")
                
                    i+=1

                #obtendo arestas e atualizando seus valores na matriz de custo
                elif("arestas" in parametro):
                    while(linhas[i].strip() != ""):

                        #obtendo vértice inicial
                        entrada = linhas[i].strip()
                        entrada = entrada.split(",")
                        verticeIncial = int(entrada[0])
                        
                        #obtendo vértice adjacente
                        entrada2 = entrada[1].split("=")
                        verticeAdj = int(entrada2[0])

                        #obtendo peso da aresta
                        peso = int(entrada2[1])
                        G.adc_lista_adj(verticeIncial, verticeAdj, peso)


                        i+=1
                    
                    print("\narestas carregadas \n")
                    i+=1

                #obtendo caminhões
                elif("caminhoes" in parametro):
                    
                    #removendo espaços e \n, e segmentando dados por ","
                    conteudo = linhas[i].strip()
                    conteudo = conteudo.split(",")

                    qtd_caminhoes = int(conteudo[0])
                    capacidade_caminhao = int(conteudo[1])

                    G.capacidadeCaminhoes = capacidade_caminhao

                    for v in G.vertices:
                        if(v.tipo=="b"):

                            caminhoes = []

                            for j in range(qtd_caminhoes):
                                cam = ver.caminhao(capacidade_caminhao, nome = f"B{v.pos}-CAM{j}")
                                cam.abastecer()
                                cam.n_pos(v)

                                caminhoes.append(cam)
                            
                            v.add_caminhoes(caminhoes)

                            print(v.nome)
                            for c in v.caminhoes:
                                print(f"vertice {c.posicao.nome}: caminhao {c.nome}")
                                print(f"    capacidade: {c.capacidade}")
                                print(f"    água atual: {c.a_atual}")
                    
                    print("\ncaminhões carregados para brigadas \n")
                    i+=1

                #obtendo qtd de equipes por posto de brigada
                elif("equipes" in parametro):
                    
                    quantidadeEquipes = int(linhas[i].strip())

                    for vertice in G.vertices:
                        if(vertice.tipo =="b"):
                            
                            equipes = []

                            
                            for j in range(quantidadeEquipes):
                                equipe = ver.equipeBrigada(nome = f"B{vertice.pos}-Equipe{j}")

                                equipes.append(equipe)

                            vertice.add_equipes(equipes)
                            
                            #atribuindo sequencialmente equipes aos seus respectivos caminhões
                            for equipe, caminhao in zip(vertice.equipes, vertice.caminhoes):
                                equipe.ocupado = True
                                equipe.caminhao = caminhao
                                caminhao.equipe = equipe
                            
                            print(vertice.nome)
                            for e in vertice.equipes:

                                print(e.nome)
                                print(e.ocupado)
                                print(f"{e.caminhao.nome} \n")
                    
                    print("equipes de brigadas inicializadas \n")
                    
                    i+=1

                else:
                    i+=1
            
            else:
                i+=1
    
    return G

def inicializandoFoco(G, foco: int, capacidade_caminhao: int):

    print("\nfoco inicial atribuído")

    print("iniciando alocação de material inflamável\n")

    G.focos.append(foco)

    #gerando material inflamável para os vértices de vegetação criados

    #qtdMaterial inflamável atribuida aleatoriamente com base em limites
    #superior e inferior projetados com base no min e max de turnos desejados
    minTurnos = 1
    maxTurnos = 3

    limiteSuperior = capacidade_caminhao // minTurnos
    limiteInferior = capacidade_caminhao // maxTurnos

    print(f"vegetação {G.vertices[foco].nome}: \n")

    for vertice in G.vertices:
        if(vertice.tipo == "v"):
            vertice.qtdMaterialInflamavel = random.randint(limiteInferior, limiteSuperior)
            print(f"{vertice.nome} -> qtdMaterial: {vertice.qtdMaterialInflamavel}")
    
    print("\nqtd de material inflamável atribuídas as vegetações\n")

    #contabilizando vertices de vegetação
    for vertice in G.vertices:
        if vertice.tipo == "v":
            G.vertices[vertice.pos].contabilizarVegetacao(G)