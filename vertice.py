from math import inf

class vertice: 
    def __init__(self, tipo: chr, nome: str, pos: int): 
        self.tipo = tipo
        self.nome = nome
        self.pos = pos
        self.d = None
        self.pi = None
        self.cor_p = None
        self.explorados = 0

    def dist(self, dist): 
        self.d = dist
    def pai(self, ver): 
        self.pi = ver
    def cor(self, cor):
        self.cor_p = cor

class caminhao:
    def __init__ (self, capacidade: int, nome: chr):
        self.nome = nome 
        self.capacidade = capacidade
        self.a_atual = None
        self.posicao = None
        self.status = "disponivel"
        self.caminhoAoFoco = []
        self.focoAtual = None
        self.equipe = None

    def n_pos(self, v: vertice):
        self.posicao = v

    def alterarStatus(self, status: chr):
        statusDisponiveis = ['disponivel', 'em_missao', 'em_reabastecimento']

        if(status in statusDisponiveis):
            self.status = status

    def abastecer(self): 
        self.a_atual = self.capacidade

    def apagar(self, necessario: int):
        if self.a_atual >= necessario: 
            self.a_atual -= necessario
            return True
        return False

class equipeBrigada:
    def __init__ (self, nome: chr):
        self.nome = nome
        self.caminhao = None
        self.ocupado = False
    
    def atribuirCaminhao(self, cam: caminhao):
        self.caminhao = cam
        self.ocupado = True


class brigada(vertice): 
    def __init__(self,tipo: chr, nome: str, pos: int):
        super().__init__(tipo, nome, pos)
        self.caminhoes = []
        self.equipes = []
        self.qtdEquipes = 0
        self.color = "red"

    def add_caminhoes(self, caminhoes: list):
            
        for veiculo in caminhoes:
            if(isinstance(veiculo, caminhao)):
                self.caminhoes.append(veiculo)
            else:
                print("caminhoes comporta apenas objetos do tipo caminhao")
    
    def add_equipes(self, equipes: list):

        for equipe in equipes:
            if(isinstance(equipe, equipeBrigada)):
                self.equipes.append(equipe)
            else:
                print("equipe comporta apenas objetos do tipo equipeBrigada")


class vegetacao(vertice):
    def __init__(self,tipo: chr, nome: str, pos: int):
        super().__init__(tipo, nome, pos)
        self.fogo = False
        self.tempo = None
        self.color = "green"
        self.qtdMaterialInflamavel = 0
        self.qtdVizinhosIncendiados = 0
        self.qtdVizinhosVegetacao = 0
    
    def queimou(self):
        self.color = "black"

    def contabilizarVegetacao(self, G):
        
        adj_temp = G.listas_adj[self.pos].raiz.next

        while adj_temp is not None:
            if adj_temp.ver.tipo == "v":
                self.qtdVizinhosVegetacao += 1
        
            adj_temp = adj_temp.next
        
        self.qtdVizinhosVegetacao -= 1

class coleta(vertice): 
    def __init__(self,tipo: chr, nome: str, pos: int):
        super().__init__(tipo, nome, pos)
        self.color = "blue"