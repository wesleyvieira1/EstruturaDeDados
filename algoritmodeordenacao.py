import time

#Função Selection Sort
def selectionSort(array):
    n = len(array)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if array[j] < array[min]:
                min = j
        array[i], array[min] = array[min], array[i]
    return array

#Função Insertion Sort
def insertionSort(array):
    n = len(array)
    for i in range(1, n):
        chave = array[i]
        j = i - 1
        while j >= 0 and chave < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = chave
    return array

#Função para ler números de um arquivo
def lerTestes(file_path):
    with open(file_path, "r") as file:
        return [int(line.strip()) for line in file]

# unção para executar os testes
def testeAlgoritmo(input_file):
    numbers = lerTestes(input_file)

    #Teste com Selection Sort
    start_time = time.time()
    selection_sorted = selectionSort(numbers[:])
    selection_time = time.time() - start_time

    #Teste com Insertion Sort
    start_time = time.time()
    insertion_sorted = insertionSort(numbers[:])
    insertion_time = time.time() - start_time


    print(f"Arquivo: {input_file}")
    print(f"Tempo Selection Sort: {selection_time:.6f} segundos")
    print(f"Array ordenado com Selection Sort: {selection_sorted}")
    print(f"Tempo Insertion Sort: {insertion_time:.6f} segundos")
    print(f"Array ordenado com Insertion Sort: {insertion_sorted}")
    print("\n")


testes = [
    './num.1000.1.in',
    './num.1000.2.in',
    './num.1000.3.in',
    './num.1000.4.in',
    './num.10000.1.in',
    './num.10000.2.in',
    './num.10000.3.in',
    './num.10000.4.in',
    './num.100000.1.in',
    './num.100000.2.in',
    './num.100000.3.in',
    './num.100000.4.in'
]

# Executa os testes para cada arquivo
for file in testes:
    testeAlgoritmo(file)


#OBS:
#Os testes estão executados no arquivo .ipynb enviado junto ao link do repositório
