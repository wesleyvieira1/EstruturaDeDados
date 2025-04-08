# -*- coding: utf-8 -*-
from graph import Graph

def load_from(fileName):
    f = open(fileName, 'r')
    n = int(f.readline())
    
    g = Graph(n)
    
    
    l = 0
    for line in f:
        line.strip()
        numeros = line.split("\t")
        c = 0
        for i in numeros:
            if(c == n):
                break
            g.M[l][c] = int(i)
            if int(i) != 0:
                g.L[l].append(c)
            
            c += 1
        l += 1
    
    return g

def carregar_teste():
    g = Graph(4)
    g.M = [
        [0, 1, 1, 0],
        [1, 0, 1, 1],
        [1, 1, 0, 0],
        [0, 1, 0, 0]
    ]
    g.L = [
        [1, 2],
        [0, 2, 3],
        [0, 1],
        [1]
    ]
    return g

print("Teste com a classe Graph\n")
g = carregar_teste()
g.print()
g.bfs_path(0, 3)
g.dfs_stack()
print("\n\n")

#Testes com os arquvivos

files = ["Grafos/pcv4.txt", "Grafos/pcv10.txt", 
         "Grafos/pcv50.txt", "Grafos/pcv177.txt"]

print("Teste com os arquivos\n\n")
for file in files:
    g = load_from(file)
    g.print()
    n = g.num_comp()
    print("Número de Componentes: " + str(n))
    
    # Teste do caminho com BFS
    print(f"\nTeste de caminho BFS de 0 até {g.num_vertices - 1}:")
    g.bfs_path(0, g.num_vertices - 1)
    
    # Teste de DFS com pilha
    print("\nDFS com pilha:")
    g.dfs_stack()

    print("\n\n")
