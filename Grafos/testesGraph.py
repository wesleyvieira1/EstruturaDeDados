from graph import Graph

def load_from(fileName):
    with open(fileName, 'r') as f:
        n = int(f.readline())
        g = Graph(n)

        l = 0
        for line in f:
            line = line.strip()
            numeros = line.split("\t")
            for c in range(min(n, len(numeros))):
                g.M[l][c] = int(numeros[c])
                if int(numeros[c]) != 0:
                    g.L[l].append(c)
            l += 1

    return g

def testar_bfs_path(file, s, t):
    print(f"\nArquivo: {file} | Caminho de {s} até {t} com BFS:")
    g = load_from(file)
    g.bfs_path(s, t)

def testar_dfs_stack(file):
    print(f"\nArquivo: {file} | DFS com pilha:")
    g = load_from(file)
    g.dfs_stack()

if __name__ == "__main__":
    arquivos = [
        ("Grafos/pcv4.txt", 0, 3),
        ("Grafos/pcv10.txt", 0, 9),
        ("Grafos/pcv50.txt", 0, 49),
        ("Grafos/pcv177.txt", 0, 176)
    ]

    for arq, s, t in arquivos:
        testar_bfs_path(arq, s, t)
        testar_dfs_stack(arq)
