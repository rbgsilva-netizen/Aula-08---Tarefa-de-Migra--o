# Sistema de Funcionários (C para Python)
limite = 100
funcionarios = []

def adicionarFuncionario():
    if len(funcionarios) >= limite:
        print("Limite atingido!")
        return

    nome = input("Nome: ").strip().title()
    cargo = input("Cargo: ").strip().title()
    while True:
        try:
            salario = float(input("Salário: ").strip().replace(',','.'))
        except ValueError:
            print('Entrada inválida!')
        else:
            if salario < 0:
                print("O salário não pode ser negativo!")
                continue
            break

    funcionario = {"Nome":nome,
                   "Cargo":cargo,
                   "Salario":salario
                   }
    funcionarios.append(funcionario)
    print("Funcionário cadastrado!")


def listarFuncionarios():
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
        return

    print("\nLista de funcionários:")
    for n, i in enumerate(funcionarios, start=1):
        print(f"{n}) {i['Nome']} - {i['Cargo']} - R$ {i['Salario']:.2f}")


def buscarFuncionario():
    nomeBusca = input("Nome do funcionário: ").strip().title()
    for i in funcionarios:
        if nomeBusca == i['Nome']:
            print(f"Cargo: {i['Cargo']} | Salário: R$ {i['Salario']:.2f}")
            return
    print("Funcionário não encontrado.")

def main():
    print("\n=== SISTEMA DE FUNCIONÁRIOS ===")
    print("1 - Adicionar funcionário")
    print("2 - Listar funcionários")
    print("3 - Buscar funcionário")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            adicionarFuncionario()
        case "2":
            listarFuncionarios()
        case "3":
            buscarFuncionario()
        case "0":
            print('Fechando...')
            return False
        case _:
            print('Opção Inválida!')
    return True

while main():
    pass