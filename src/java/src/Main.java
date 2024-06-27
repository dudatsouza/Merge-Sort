// IMPLEMENTAÇÃO MERGE SORT EM JAVA
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o tamanho do vetor: ");
        int n = scanner.nextInt();

        System.out.print("Digite o nome do arquivo de entrada: ");
        String arqE = scanner.next();

        System.out.print("Digite o nome do arquivo de saída: ");
        String arqS = scanner.next();

        MergeSort sorter = new MergeSort(arqE, arqS);
        sorter.run(n);

        System.out.println("Execução em Java finalizada");
        scanner.close();
    }
}