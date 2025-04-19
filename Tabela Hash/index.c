#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//Tamanhos fixos
#define TAM_PRIMEIRO_NIVEL 10
#define TAM_SEGUNDO_NIVEL 5
#define TAM_NOME 50

//Estrutura Objeto
struct Objeto {
    int chave;
    char nome[TAM_NOME];
    struct Objeto* prox;
};

//Estrutura Segundo Nível 
struct SegundoNivel {
    struct Objeto* listas[TAM_SEGUNDO_NIVEL];
};

//Estrutura Tabela Hash
struct SegundoNivel* tabelaHash[TAM_PRIMEIRO_NIVEL];


//Funções de Hash
int hashPrimeiroNivel(int chave) {
    return chave % TAM_PRIMEIRO_NIVEL;
}

//Função de Hash para o segundo nível
int hashSegundoNivel(int chave) {
    return (chave / TAM_PRIMEIRO_NIVEL) % TAM_SEGUNDO_NIVEL;
}

int main() {
    int i, j;

    //Inicializando a tabela com NULL
    for (i = 0; i < TAM_PRIMEIRO_NIVEL; i++) {
        tabelaHash[i] = NULL;
    }

    int chaves[] = {15, 25, 35, 45, 55, 65};
    char nomes[][TAM_NOME] = {"João", "Marina", "Julia", "Marco", "Antônio", "José"};

    for (i = 0; i < 6; i++) {
        int chave = chaves[i];
        char* nome = nomes[i];

        int pos1 = hashPrimeiroNivel(chave);
        int pos2 = hashSegundoNivel(chave);

        if (tabelaHash[pos1] == NULL) {
            tabelaHash[pos1] = (struct SegundoNivel*) malloc(sizeof(struct SegundoNivel));
            for (j = 0; j < TAM_SEGUNDO_NIVEL; j++) {
                tabelaHash[pos1]->listas[j] = NULL;
            }
        }

        //Novo Objeto
        struct Objeto* novo = (struct Objeto*) malloc(sizeof(struct Objeto));
        novo->chave = chave;
        strcpy(novo->nome, nome);
        novo->prox = NULL;

        novo->prox = tabelaHash[pos1]->listas[pos2];
        tabelaHash[pos1]->listas[pos2] = novo;

        printf("%s: %d\n", nome, chave);
    }

    //Buscando um objeto
    int chaveBusca;
    printf("\nDigite a chave para buscar: ");
    scanf("%d", &chaveBusca);

    int pos1 = hashPrimeiroNivel(chaveBusca);
    int pos2 = hashSegundoNivel(chaveBusca);

    if (tabelaHash[pos1] != NULL) {
        struct Objeto* atual = tabelaHash[pos1]->listas[pos2];
        while (atual != NULL) {
            if (atual->chave == chaveBusca) {
                printf("Encontrado! %s (Chave: %d)\n", atual->nome, atual->chave);
                break;
            }
            atual = atual->prox;
        }
        if (atual == NULL) {
            printf("Objeto com chave %d não encontrado\n", chaveBusca);
        }
    } else {
        printf("Objeto com chave %d não encontrado\n", chaveBusca);
    }

    //Limpando Mémoria
    for (i = 0; i < TAM_PRIMEIRO_NIVEL; i++) {
        if (tabelaHash[i] != NULL) {
            for (j = 0; j < TAM_SEGUNDO_NIVEL; j++) {
                struct Objeto* atual = tabelaHash[i]->listas[j];
                while (atual != NULL) {
                    struct Objeto* temp = atual;
                    atual = atual->prox;
                    free(temp);
                }
            }
            free(tabelaHash[i]);
        }
    }

    return 0;
}
