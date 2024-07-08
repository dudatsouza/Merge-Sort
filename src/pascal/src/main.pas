program Main;

uses
  SysUtils, MergeSort;

var
  n: Integer;
  arqE, arqS: string;
  sorter: TMergeSort;

begin
  Write('Digite o tamanho do vetor: ');
  ReadLn(n);

  Write('Digite o nome do arquivo de entrada: ');
  ReadLn(arqE);

  Write('Digite o nome do arquivo de saída: ');
  ReadLn(arqS);

  arqE := '../../../datasets/inputs/random.txt';
  arqS := '../../../datasets/outputs/output.csv';

  sorter.Init(arqE, arqS);
  sorter.Run(n);

  WriteLn('Execução em Pascal finalizada.');
end.
