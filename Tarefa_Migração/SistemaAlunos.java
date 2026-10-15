import java.util.*;

public class SistemaAlunos {

    static HashMap<String, Double> notas = new HashMap<>();
    static ArrayList<String> listaNomes = new ArrayList<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int opcao;

        do {
            System.out.println("\n=== SISTEMA DE ALUNOS ===");
            System.out.println("1 - Adicionar aluno");
            System.out.println("2 - Listar alunos");
            System.out.println("3 - Buscar nota");
            System.out.println("0 - Sair");
            System.out.print("Opção: ");
            opcao = sc.nextInt();
            sc.nextLine();

            switch (opcao) {
                case 1:
                    adicionarAluno(sc);
                    break;
                case 2:
                    listarAlunos();
                    break;
                case 3:
                    buscarNota(sc);
                    break;
                case 0:
                    System.out.println("Encerrando...");
                    break;
                default:
                    System.out.println("Opção inválida!");
                    break;
            }

        } while (opcao != 0);
        sc.close();
    }

    public static void adicionarAluno(Scanner sc) {
        System.out.print("Nome do aluno: ");
        String nome = sc.nextLine();
        System.out.print("Nota final: ");
        double nota = sc.nextDouble();

        notas.put(nome, nota);
        listaNomes.add(nome);
        System.out.println("Aluno cadastrado com sucesso!");
    }

    public static void listarAlunos() {
        if (listaNomes.isEmpty()) {
            System.out.println("Nenhum aluno cadastrado.");
            return;
        }
        System.out.println("\nLista de alunos:");
        for (String nome : listaNomes) {
            System.out.println("- " + nome + " | Nota: " + notas.get(nome));
        }
    }

    public static void buscarNota(Scanner sc) {
        System.out.print("Nome do aluno: ");
        String nome = sc.nextLine();
        if (notas.containsKey(nome)) {
            System.out.println("Nota de " + nome + ": " + notas.get(nome));
        } else {
            System.out.println("Aluno não encontrado.");
        }
    }
}
