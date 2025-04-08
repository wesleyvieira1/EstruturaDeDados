# -*- coding: utf-8 -*-
import queue

class Graph:
    # Construtor da classe Graph
    # Inicializa a matriz de adjacência e a lista de adjacência
    def __init__(self, n):
        self.num_vertices = n
        self.M = [[0 for _ in range(n)] for _ in range(n)]
        self.L = [ [] for _ in range(n)]

    
    def print(self):
        print("Número de Vértices: " + str(self.num_vertices))
        print("Matriz de adjacência:")
        print(self.M)
        print("Lista de Adjacência:")
        print(self.L)
    

    def num_comp(self):
        pred = self.dfs()
        num = 0
        for v in range(self.num_vertices):
            if(pred[v] == -1):
                num += 1
        return num
    
    def dfs(self):
        pred = [-1 for _ in range(self.num_vertices)]
        visitados = [False for _ in range(self.num_vertices)]
        for v in range(self.num_vertices):
            if(visitados[v] == False):
                self.dfs_rec(v, visitados, pred)
                
        return pred
        
        
    def dfs_rec(self, v, visitados, pred):
        print("Vertice: " + str(v))
        visitados[v] = True
        for u in self.L[v]:
            if(visitados[u] == False):
                pred[u] = v
                self.dfs_rec(u, visitados, pred)
    
    def bfs(self, source):
        visitados = [False for _ in range(self.num_vertices)]
        pred = [-1 for _ in range(self.num_vertices)]
        D = [-1 for _ in range(self.num_vertices)]
        Q = queue.Queue()
        Q.put(source)
        visitados[source] = True
        D[source] = 0
        
        while(Q.empty() == False):
            v = Q.get()
            print("Vertice:" + str(v))
            for u in self.L[v]:
                if(visitados[u] == False):
                    Q.put(u)
                    visitados[u] = True
                    D[u] = D[v] + 1
                    pred[u] = v
        
        return D, pred

    # Método para encontrar o caminho entre dois vértices usando BFS
    # Se não houver caminho, imprime uma mensagem informando
    # Se houver caminho, imprime o caminho encontrado
    def bfs_path(self, s, t):
        _, pred = self.bfs(s)
        if pred[t] == -1:
            print(f"Não há caminho entre {s} e {t}")
            return
        path = []
        at = t
        while at != -1:
            path.append(at)
            at = pred[at]
        path.reverse()
        print(f"Caminho de {s} até {t}: {' -> '.join(map(str, path))}")

    #  Método para realizar a busca em profundidade (DFS) usando pilha
    # Este método não utiliza recursão, mas sim uma pilha explícita
    def dfs_stack(self):
        pred = [-1 for _ in range(self.num_vertices)]
        visitados = [False for _ in range(self.num_vertices)]

        for v in range(self.num_vertices):
            if not visitados[v]:
                stack = [v]
                while stack:
                    u = stack.pop()
                    if not visitados[u]:
                        print("Vértice:", u)
                        visitados[u] = True
                        for w in reversed(self.L[u]):
                            if not visitados[w]:
                                pred[w] = u
                                stack.append(w)
        return pred
