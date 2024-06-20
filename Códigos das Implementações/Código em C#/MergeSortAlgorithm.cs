// IMPLEMENTAÇÃO MERGE SORT EM C#
using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;

public class MergeSortAlgorithm
{
    private List<int> array = new List<int>();
    private string arq;
    private string arq2;

    public MergeSortAlgorithm(string arqE, string arqS)
    {
        this.arq = arqE;
        this.arq2 = arqS;
    }

    private void Merge(List<int> v, int inicio, int meio, int fim)
    {
        List<int> temp = new List<int>();
        int p1 = inicio, p2 = meio + 1;

        while (p1 <= meio && p2 <= fim)
        {
            if (v[p1] <= v[p2])
            {
                temp.Add(v[p1++]);
            }
            else
            {
                temp.Add(v[p2++]);
            }
        }

        while (p1 <= meio)
        {
            temp.Add(v[p1++]);
        }

        while (p2 <= fim)
        {
            temp.Add(v[p2++]);
        }

        for (int i = 0; i < temp.Count; i++)
        {
            v[inicio + i] = temp[i];
        }
    }

    private void MergeSort(List<int> v, int inicio, int fim)
    {
        int meio;
        if (inicio < fim)
        {
            meio = (inicio + fim) / 2;
            MergeSort(v, inicio, meio);
            MergeSort(v, meio + 1, fim);
            Merge(v, inicio, meio, fim);
        }
    }

    private void DefinirArray(int n)
    {
        try
        {
            using (StreamReader sr = new StreamReader(arq))
            {
                array.Clear(); 
                string linha = sr.ReadLine();
                string[] numeros = linha.Split(new char[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);
                foreach (var num in numeros)
                {
                    if (int.TryParse(num, out int num1))
                    {
                        array.Add(num1);
                    }
                }
            }
        }
        catch (Exception e)
        {
            Console.WriteLine($"Erro ao ler o arquivo de entrada: {e.Message}");
        }

        if (array.Count > n)
        {
            array = array.GetRange(0, n);
        }
    }

    private void SalvarTempo(int n, double timeTaken)
    {
        try
        {
            using (StreamWriter sw = new StreamWriter(arq2, true))
            {
                string formattedTimeTaken = timeTaken.ToString("F10", CultureInfo.InvariantCulture);
                sw.Write($"\nC#,{n},{formattedTimeTaken.Replace(',', '.')},{arq}");
            }
        }
        catch (Exception e)
        {
            Console.WriteLine($"Erro ao salvar o tempo de execução: {e.Message}");
        }
    }


    public void Run(int n)
    {
        DefinirArray(n);

        DateTime startTime = DateTime.Now;
        MergeSort(array, 0, array.Count - 1);
        DateTime endTime = DateTime.Now;
        double timeTaken = (endTime - startTime).TotalSeconds;

        SalvarTempo(n, timeTaken);
    }
}
