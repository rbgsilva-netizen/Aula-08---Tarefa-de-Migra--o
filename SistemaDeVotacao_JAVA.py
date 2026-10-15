votos = {"Opção 1":0,
         "Opção 2":0,
         "Opção 3":0
         }

def main():
    print("=== SISTEMA DE VOTAÇÃO ===")
    print("As opções são:")
    for indice, opcao in enumerate(votos):
        print(f"{indice + 1} - {opcao}")

    opcoes = list(votos)
    votacaoAtiva = True
    while votacaoAtiva:
        try:
            escolha = int(input(f"\nEscolha uma opção (1-{len(votos)}) ou 0 para encerrar: "))
        except ValueError:
            print("Entrada inválida. Digite apenas números")
            continue
        else:
            if escolha == 0:
                votacaoAtiva = False
            elif 1 <= escolha <= len(votos):
                opcao = opcoes[escolha-1]
                print(f"Você votou na {opcao}")
                votos[opcao] += 1
            else:
                print("Entrada inválida. Tente novamente.")

    print("\n=== RESULTADOS FINAIS ===")
    for opcao, voto in votos.items():
        unidade = "voto" if voto == 1 else "votos"
        print(f"{opcao}: {voto} {unidade}")


main()