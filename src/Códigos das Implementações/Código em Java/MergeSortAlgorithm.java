// IMPLEMENTAÇÃO MERGE SORT EM JAVA
import java.io.*;
import java.util.*;

public class MergeSortAlgorithm {
    private List<Integer> array = new ArrayList<>();
    private String arq;
    private String arq2;

    public MergeSortAlgorithm(String arqE, String arqS) {
        this.arq = arqE;
        this.arq2 = arqS;
    }

    private void merge(List<Integer> v, int inicio, int meio, int fim) {
        List<Integer> temp = new ArrayList<>();
        int p1 = inicio, p2 = meio + 1;

        while (p1 <= meio && p2 <= fim) {
            if (v.get(p1) <= v.get(p2)) {
                temp.add(v.get(p1++));
            } else {
                temp.add(v.get(p2++));
            }
        }

        while (p1 <= meio) {
            temp.add(v.get(p1++));
        }

        while (p2 <= fim) {
            temp.add(v.get(p2++));
        }

        for (int i = 0; i < temp.size(); i++) {
            v.set(inicio + i, temp.get(i));
        }
    }

    private void mergeSort(List<Integer> v, int inicio, int fim) {
        int meio;
        if (inicio < fim) {
            meio = (inicio + fim) / 2;
            mergeSort(v, inicio, meio);
            mergeSort(v, meio + 1, fim);
            merge(v, inicio, meio, fim);
        }
    }

    private void definirArray(int n) {
        try (Scanner scanner = new Scanner(new File(arq))) {
            array.clear(); 
            while (scanner.hasNextInt()) {
                array.add(scanner.nextInt());
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        if (array.size() > n) {
            array = array.subList(0, n);
        }
    }

    private void salvarTempo(int n, double timeTaken) {
    try (PrintWriter writer = new PrintWriter(new FileWriter(arq2, true))) {
        writer.print("\nJava," + n + "," + String.format(Locale.US, "%.10f", timeTaken) + "," + arq);
    } catch (IOException e) {
        e.printStackTrace();
    }
}

public void run(int n) {
    definirArray(n);

    long startTime = System.nanoTime();
    mergeSort(array, 0, array.size() - 1);
    long endTime = System.nanoTime();
    double timeTaken = (endTime - startTime) / 1e9;

    salvarTempo(n, timeTaken);
}

}
