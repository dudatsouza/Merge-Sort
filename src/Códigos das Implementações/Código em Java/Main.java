// IMPLEMENTAÇÃO MERGE SORT EM JAVA
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        System.out.print("Digite o tamanho do vetor: ");
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        System.out.print("Digite o nome do arquivo de entrada: ");
        String arqE = scanner.next();

        System.out.print("Digite o nome do arquivo de saída: ");
        String arqS = scanner.next();

        MergeSortAlgorithm sorter = new MergeSortAlgorithm(arqE, arqS);
        sorter.run(n);

        System.out.println("Execução em Java finalizada");
    }
}