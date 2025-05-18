import vertice as v
import linkedlist as ar
import random as r
from math import inf

class grafo:
    def __init__(self):
        self.vertices = []
        self.arestas = []
        self.listas_adj = []
        self.focos = []
        self.mat_custos = []
        self.qtd_brigadas = 0
        self.capacidadeCaminhoes = 0
        self.focosAtendidos = []
        self.qtdFocosSalvos = 0
        self.focosQueimados = []
        self.equipesMobilizadas = []
        self.qtdAguaUtilizada = 0
        self.reabastecimentos = 0
    
    def pos_ver(self, ver):
        return self.vertices[ver]
    
    def cria_ver(self, tipo: chr):
         match tipo: 
            case 'b':
                if(self.qtd_brigadas < 3):
                    V = v.brigada(tipo = "b", nome = f"B: {len(self.vertices)}", pos = len(self.vertices))
                    self.qtd_brigadas += 1
                    return V
                else: 
                    print("Já existem brigadas demais - Uma delas foi removida!")
                    return None
            case 'v':
                V = v.vegetacao(tipo = 'v', nome = f"V: {len(self.vertices)}", pos = len(self.vertices))
                return V
            case 'c': 
                V = v.coleta(tipo = 'c', nome = f"C: {len(self.vertices)}", pos = len(self.vertices))
                return V
            
            case _: 
                print("Tipo não reconhecido")
                return None
    
    def insere_ver(self, tipo: chr):
        
        V = self.cria_ver(tipo)
        
        if (V != None):

            def compara(K): 
                if (type(K) == type(V)): return True
                else: return False
            
            for i in filter(compara, self.vertices):
                if i.nome == V.nome: 
                    print("Nome já existe")
                    V = None
            
            if (V != None):
                ##Agora para eliminar ocorrêcias repetidas!!!
                self.listas_adj.append(ar.lista(V))
                self.vertices.append(V)
                self.ajusta_matP()

    def ajusta_matP(self): 
        n = len(self.vertices)

        while (len(self.mat_custos) < n):
            ref = []
            self.mat_custos.append(ref)
            for i in self.mat_custos:
                while (len(i) < n):
                    i.append(0)

    def deleta(self, vertice: v.vertice):
        x = self.vertices.index(vertice)
        self.vertices.pop(x)
        self.listas_adj.pop(x)
        self.mat_custos.pop(x)

        for x in self.mat_custos: 
            x.pop(x)

    def adc_lista_adj(self, ind_v: int , ind_adj: int, peso: int):
        self.listas_adj[ind_v].inserir(self.vertices[ind_adj], peso)
        self.listas_adj[ind_adj].inserir(self.vertices[ind_v], peso)
        self.mat_custos[ind_v] [ind_adj] = peso
        self.mat_custos[ind_adj] [ind_v] = peso
        self.arestas.append((ind_v, ind_adj))

    def listar_Prop(self):
        count = 0
        for i in self.vertices: 
            print(f"{count+1} - {i.nome} -> {type(i)}")
            count += 1
        
        for i in self.listas_adj: 
            i.Exibir_adj()
    
    def resetarAtributos(self, capacidadeCaminhao: int):
        self.focos = []
        self.focosAtendidos = []
        self.qtdFocosSalvos = 0
        self.focosQueimados = []
        self.equipesMobilizadas = []
        self.qtdAguaUtilizada = 0
        self.reabastecimentos = 0

        #resetar atributos dos caminhões das brigadas
        for vertice in self.vertices:

            #resetar atributos dos vértices de vegetacao
            if(vertice.tipo == "v"):
                vertice.fogo = False
                vertice.color = "green"
                vertice.qtdVizinhosIncendiados = 0
                vertice.explorados = 0

            if(vertice.tipo == "b"):
                for caminhao in vertice.caminhoes:
                    caminhao.a_atual = capacidadeCaminhao
                    caminhao.n_pos(vertice)
                    caminhao.status = "disponivel"
                    caminhao.caminhoAoFoco = []
                    caminhao.focoAtual = None


