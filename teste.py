import os
from time import sleep

funcionarios = []
opcoes = ['1 - Cadastrar funcionário',
          '2 - Listar funcionários',
          '3 - Pesquisar funcionário',
          '0 - Sair']


def cadastrar_funcionario():
    os.system('cls')
    print(" Cadastrado de Funcionários ".center(100,"="))
    nome = input("Nome: ").strip().title()
    cargo = input("Cargo: ").strip().title()
    while True:
        try:
            salario = float(input("Salario: "))
        except ValueError:
            print('Entrada inválida.')
        else:
            if salario < 0:
                print('Não é permitido valores negativos.')
                continue
            else:
                break

    funcionario = {'Nome':nome,
                   'Cargo':cargo,
                   'Salário':salario}
    funcionarios.append(funcionario)
    print("Funcionário cadastrado com sucesso!")

    novoCadastro = input("Deseja cadastrar outro funcionário? [s/n]").strip().lower()
    if novoCadastro == "s":
        return True
    elif novoCadastro == "n":
        return False
    else:
        print("Entrada inválida.")
        input('[Pressione ENTER para voltar ao menu inicial]')
        return False


def listar_funcionario():
    os.system('cls')
    print(" Funcionarios Cadastrados ".center(100,"="))
    for indice, func in enumerate(funcionarios):
        print(f'[{indice}] Nome: {func['Nome']:<25} | Cargo: {func['Cargo']:<25} | Salário: R$ {func['Salário']:.2f}')


def pesquisar_funcionario():
    os.system('cls')
    print(" Pesquisar Funcionário ".center(100,"="))
    print()
    contador = 0
    busca_nome = input("Nome: ").strip().title()
    for i in funcionarios:
        if busca_nome in list(i["Nome"].split()):
            print("-"*30)
            print(f"Nome: {i["Nome"]}")
            print(f"Cargo: {i['Cargo']}")
            print(f"Salário: R$ {i['Salário']}")
            contador += 1

    if contador == 0:
        print('\nFuncionário não cadastrado.')


def main():
    os.system('cls')
    print(' Sistema de Funcionários '.center(70,"="))
    for i in opcoes:
        print(i)


    escolha = input('Escolha uma opção: ').strip()
    match escolha:
        case '1':
            while cadastrar_funcionario():
                pass

        case '2':
            listar_funcionario()
            input('\n[Pressione ENTER para voltar ao menu inicial]')
        case '3':
            pesquisar_funcionario()
            input('\n[Pressione ENTER para voltar ao menu inicial]')
        case '0':
            print("Encerrando...")
            return False
        case _:
            print(f"Entrada inválida. Escolha entre 0 e {len(opcoes)-1}")
    

    # input('[Pressione ENTER para voltar ao menu inicial]')
    return True


while main():
    pass