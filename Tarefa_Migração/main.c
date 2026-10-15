#include <stdio.h>
#include <string.h>

#define MAX 100

typedef struct {
    char nome[50];
    char cargo[30];
    float salario;
} Funcionario;

Funcionario funcionarios[MAX];
int total = 0;

void adicionarFuncionario();
void listarFuncionarios();
void buscarFuncionario();

int main() {
    int opcao;

    do {
        printf("\n=== SISTEMA DE FUNCIONÁRIOS ===\n");
        printf("1 - Adicionar funcionário\n");
        printf("2 - Listar funcionários\n");
        printf("3 - Buscar funcionário\n");
        printf("0 - Sair\n");
        printf("Escolha uma opção: ");
        scanf("%d", &opcao);
        getchar(); // limpar buffer

        switch (opcao) {
            case 1: adicionarFuncionario(); break;
            case 2: listarFuncionarios(); break;
            case 3: buscarFuncionario(); break;
            case 0: printf("Encerrando...\n"); break;
            default: printf("Opção inválida!\n");
        }
    } while (opcao != 0);

    return 0;
}

void adicionarFuncionario() {
    if (total >= MAX) {
        printf("Limite atingido!\n");
        return;
    }
    printf("Nome: ");
    fgets(funcionarios[total].nome, 50, stdin);
    funcionarios[total].nome[strcspn(funcionarios[total].nome, "\n")] = '\0';

    printf("Cargo: ");
    fgets(funcionarios[total].cargo, 30, stdin);
    funcionarios[total].cargo[strcspn(funcionarios[total].cargo, "\n")] = '\0';

    printf("Salário: ");
    scanf("%f", &funcionarios[total].salario);
    getchar();

    total++;
    printf("Funcionário cadastrado!\n");
}

void listarFuncionarios() {
    if (total == 0) {
        printf("Nenhum funcionário cadastrado.\n");
        return;
    }
    printf("\nLista de funcionários:\n");
    for (int i = 0; i < total; i++) {
        printf("%d) %s - %s - R$ %.2f\n", i + 1,
               funcionarios[i].nome,
               funcionarios[i].cargo,
               funcionarios[i].salario);
    }
}

void buscarFuncionario() {
    char nomeBusca[50];
    printf("Nome do funcionário: ");
    fgets(nomeBusca, 50, stdin);
    nomeBusca[strcspn(nomeBusca, "\n")] = '\0';

    for (int i = 0; i < total; i++) {
        if (strcmp(funcionarios[i].nome, nomeBusca) == 0) {
            printf("Cargo: %s | Salário: R$ %.2f\n",
                   funcionarios[i].cargo, funcionarios[i].salario);
            return;
        }
    }
    printf("Funcionário não encontrado.\n");
}
