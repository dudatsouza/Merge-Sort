// IMPLEMENTAÇÃO MERGE SORT EM C#
using System;

public class Program
{
    public static void Main(string[] args)
    {
        Console.Write("Digite o tamanho do vetor: ");
        int n = int.Parse(Console.ReadLine());

        Console.Write("Digite o nome do arquivo de entrada: ");
        string arqE = Console.ReadLine();

        Console.Write("Digite o nome do arquivo de saída: ");
        string arqS = Console.ReadLine();

        MergeSortAlgorithm sorter = new MergeSortAlgorithm(arqE, arqS);
        sorter.Run(n);

        Console.Write("Execução em C# finalizada\n");
    }
}

