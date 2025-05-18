import vertice as ver

class no: 
    def __init__(self, vertice: ver.vertice , peso: int): 
        self.ver = vertice
        self.next = None
        self.peso = peso
    
    def prox(self, prox): 
        self.next = prox
        
##Posso incrementar lista ordenada por peso...
##Isso seria bom? Eu preciso sempre chegar no de menor peso. Mas não importa muito.
##Quem vai ler por peso não o algoritmo de busca mais tarde. Por enquanto é só ordenar.

class lista:
    def __init__(self, vertice: ver.vertice): 
        self.raiz = no(vertice, 0)
        self.tam = 0

    @property
    def tamanho(self): 
        return self.tam
    
    def __len__(self):
        tam = 0
        atual = self.raiz

        while atual != None:
            tam += 1
            atual = atual.next

        return tam 

    def busca(self, x: ver.vertice):
        atual = self.raiz
        while atual != None: 
            if atual.ver == x:
                return atual
            else:
                atual = atual.next
        return None
    
    
    def inserir(self, x: ver.vertice, peso):
        novo = no(x, peso)
        if self.busca(x) != None:
            print(f"Elemento {x.nome} já está na lista de {self.raiz.ver.nome}")
            return None
        
        else: 
            atual = self.raiz
            while atual.next != None: 
                atual = atual.next
            atual.next = novo
            self.tam += 1
            atual = atual.next
        return atual
    
    def Exibir_adj(self):
        atual = self.raiz 
        while atual != None: 
            print(f"|{atual.ver.nome}| -> ", end = "")
            atual = atual.next
        print("None")

    def remover(self, x: ver.vertice):
        atual = self.raiz
        buscado = self.busca(x)
        if buscado == self.raiz: 
            self.raiz = buscado.next
            self.tam -= 1
            print("Elemento removido era a raiz")
            return True
        elif buscado != None: 
            while atual.next != buscado: 
                atual = atual.next
            atual.next = buscado.next
            self.tam -= 1
            print("Removido. \n")
            return True
        else:
            print("Elemento não está na lista! \n")
            return False