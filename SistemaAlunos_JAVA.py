
alunos = {}

def adicionar_aluno():
    nome = input("Nome do aluno: ").strip().title()
    while True:
        try:
            nota = float(input("Nota final: "))
        except ValueError:
            print('Entrada inválida')
        else:
            if not 0 <= nota <= 10:
                print('A nota precisa estar entre 0 e 10.')
                continue
            break

    alunos[nome] = nota
    print("Aluno cadastrado com sucesso!")


def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    print("\nLista de alunos")
    for nome, nota in alunos.items():
        print(f"- {nome} | Nota: {nota:.2f}")


def buscar_nota():
    busca_nome = input("Nome do aluno: ").strip().title()

    if busca_nome in alunos:
        print(f"Nota de {busca_nome}: {alunos[busca_nome]:.2f}")
    else:
        print("Aluno não encontrado.")


def main():
    print("\n=== SISTEMA DE ALUNOS ===")
    print("1 - Adicionar aluno")
    print("2 - Listar alunos")
    print("3 - Buscar nota")
    print("0 - Sair")

    opcao = input("Opção: ")
    match opcao:
        case "1":
            adicionar_aluno()
        case "2":
            listar_alunos()
        case "3":
            buscar_nota()
        case "0":
            print("Encerrando...")
            return False
        case _:
            print("Opção Inválida!")

    return True

while main():
    pass