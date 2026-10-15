import java.util.*;

public class SistemaDeVotacao {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String[] opcoes = {"Opção 1", "Opção 2", "Opção 3"};
        int[] votos = new int[opcoes.length];
        boolean votacaoAtiva = true;

        System.out.println("=== SISTEMA DE VOTAÇÃO ===");
        System.out.println("As opções são:");
        for (int i = 0; i < opcoes.length; i++) {
            System.out.println((i + 1) + " - " + opcoes[i]);
        }

        while (votacaoAtiva) {
            System.out.print("\nEscolha uma opção (1-" + opcoes.length + ") ou 0 para encerrar: ");

            if (scanner.hasNextInt()) {
                int escolha = scanner.nextInt();

                if (escolha == 0) {
                    votacaoAtiva = false;
                } else if (escolha >= 1 && escolha <= opcoes.length) {
                    votos[escolha - 1]++;
                    System.out.println("Você votou na " + opcoes[escolha - 1]);
                } else {
                    System.out.println("Opção inválida. Tente novamente.");
                }
            } else {
                System.out.println("Entrada inválida. Digite apenas números.");
                scanner.next(); // descarta entrada inválida
            }
        }

        System.out.println("\n=== RESULTADOS FINAIS ===");
        for (int i = 0; i < opcoes.length; i++) {
            System.out.println(opcoes[i] + ": " + votos[i] + " voto(s)");
        }

        scanner.close();
    }
}
