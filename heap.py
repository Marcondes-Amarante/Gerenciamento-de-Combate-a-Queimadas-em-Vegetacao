import grafos as gr
import vertice as v
import linkedlist as list
import math as mt

##Preciso modificar...
##E se mantiver 2 vetores? -> Um mantém as prioridades e outro mantem os elementos.

class no: 
    def __init__(self, ver):
        self.ver = ver
        self.prio = None

    def set_prio(self, val):
        self.prio = val

class heap: 
    def __init__(self):
        self.ordem = []
        self.vetores = dict()
    

    def posicao(self, ver, index):
        self.vetores[ver.nome] = index

    def inserir(self, ver, prio):
        x = no(ver)
        x.set_prio(prio)
        self.ordem.append(x)
        self.vetores[ver.nome] = self.ultima()
        subir(self, self.ultima())

    def corrigir(self, ver, antiga, nova):
        i = self.vetores[ver.nome]
        self.ordem[i].prio = nova
        if antiga > nova:
            subir(self, i)
        else: 
            descer(self, i)
        

    def remover(self):
        if (len(self.ordem) > 0):
            self.ordem[0], self.ordem[self.ultima()] = self.ordem[self.ultima()],self.ordem[0]
            self.posicao(self.ordem[0].ver, 0)
            del self.vetores[self.ordem[self.ultima()].ver.nome]
            x = self.ordem[self.ultima()].ver
            self.ordem.pop(self.ultima())
            descer(self, 0)
            return x



    def ultima(self): 
        return (len(self.ordem) - 1)

        
def subir(H,i):
    j = mt.floor(i/2)
    if j >= 0:
        if H.ordem[i].prio < H.ordem[j].prio:
            temp = H.ordem[i]
            H.ordem[i] = H.ordem[j]
            H.ordem[j] = temp

            H.posicao(H.ordem[j].ver, j)
            H.posicao(H.ordem[i].ver, i)

            subir(H, j)

def descer(H, i):
    n = len(H.ordem)-1
    j = 2*i
    if j <= n: 
        if j < n: 
            if (H.ordem[j + 1].prio < H.ordem[j].prio):
                j = j+1
            if( H.ordem[i].prio > H.ordem[j].prio):
                H.ordem[i], H.ordem[j] = H.ordem[j], H.ordem[i]

                H.posicao(H.ordem[j].ver, j)
                H.posicao(H.ordem[i].ver, i)

                descer(H, j)
