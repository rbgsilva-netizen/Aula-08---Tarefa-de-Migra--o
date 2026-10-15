# Sistema de cadastro de alunos (COBOL para Python)
alunos = []
num_alunos = 5

def calcula_Media(lista):
    return  sum(lista) / len(lista)


def main():
    print("=== SISTEMA DE CADASTRO DE ALUNOS ===")
    for i in range(1,num_alunos + 1):
        nome = input(f"Digite o nome do aluno {i}: ")
        nota = float(input(f"Digite a nota de {nome}: "))
        alunos.append((nome,nota))

    print("=== LISTA DE ALUNOS ===")
    for k,v in alunos:
        print(f"{k:<20} | Nota: {v:.2f}")

    notas = [nota for nome, nota in alunos]
    media = calcula_Media(notas)

    print(f"Média da turma: {media:.2f}")


main()