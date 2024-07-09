unit MergeSort;

interface

{$IFDEF UNIX}
uses
  SysUtils, BaseUnix;
{$ENDIF}

type
  TMergeSort = object
  private
    dataArray: array of Integer;
    arq: string;
    arq2: string;
    procedure Merge(var v: array of Integer; inicio, meio, fim: Integer);
    procedure MergeSort(var v: array of Integer; inicio, fim: Integer);
    procedure DefinirArray(n: Integer);
    procedure SalvarTempo(n: Integer; timeTaken: Double);
  public
    constructor Init(const arqE, arqS: string);
    procedure Run(n: Integer);
  end;

implementation

constructor TMergeSort.Init(const arqE, arqS: string);
begin
  arq := arqE;
  arq2 := arqS;
end;

procedure TMergeSort.Merge(var v: array of Integer; inicio, meio, fim: Integer);
var
  tamanho, p1, p2, idx, i: Integer;
  temp: array of Integer;
begin
  tamanho := fim - inicio + 1;
  SetLength(temp, tamanho);
  p1 := inicio;
  p2 := meio + 1;
  idx := 0;

  while (p1 <= meio) and (p2 <= fim) do
  begin
    if v[p1] <= v[p2] then
    begin
      temp[idx] := v[p1];
      Inc(p1);
    end
    else
    begin
      temp[idx] := v[p2];
      Inc(p2);
    end;
    Inc(idx);
  end;

  while p1 <= meio do
  begin
    temp[idx] := v[p1];
    Inc(p1);
    Inc(idx);
  end;

  while p2 <= fim do
  begin
    temp[idx] := v[p2];
    Inc(p2);
    Inc(idx);
  end;

  for i := 0 to tamanho - 1 do
    v[inicio + i] := temp[i];
end;

procedure TMergeSort.MergeSort(var v: array of Integer; inicio, fim: Integer);
var
  meio: Integer;
begin
  if inicio < fim then
  begin
    meio := (inicio + fim) div 2;
    MergeSort(v, inicio, meio);
    MergeSort(v, meio + 1, fim);
    Merge(v, inicio, meio, fim);
  end;
end;

procedure TMergeSort.DefinirArray(n: Integer);
var
  fileIn: TextFile;
  linha: string;
  substrings: array of string;
  i, count: Integer;
begin
  SetLength(dataArray, n);

  Assign(fileIn, arq);
  Reset(fileIn);

  // Lê a linha inteira do arquivo
  ReadLn(fileIn, linha);
  Close(fileIn);

  // Divide a linha em substrings com base no espaço
  substrings := linha.Split([' ']);

  // Preenche dataArray com os primeiros n elementos
  count := 0;
  for i := 0 to High(substrings) do
  begin
    if count < n then
    begin
      dataArray[count] := StrToInt(substrings[i]);
      Inc(count);
    end
    else
      Break;
  end;
end;

procedure TMergeSort.SalvarTempo(n: Integer; timeTaken: Double);
var
  fileOut: TextFile;
begin
  Assign(fileOut, arq2);
  if FileExists(arq2) then
    Append(fileOut)
  else
    Rewrite(fileOut);

  WriteLn(fileOut, Format('Pascal,%d,%.10f,%s', [n, timeTaken, arq]));
  Close(fileOut);

  WriteLn('Tempo de execução: ', FormatFloat('0.0000000000', timeTaken));
end;

procedure TMergeSort.Run(n: Integer);
var
  TempoInicial, TempoFinal: timeval;
  TempoExecucao: Double;
begin
  WriteLn('Definindo array...');
  DefinirArray(n);

  {$IFDEF UNIX}
  // Capturar o tempo inicial
  fpGetTimeOfDay(@TempoInicial, nil);

  MergeSort(dataArray, 0, Length(dataArray) - 1);
  
  // Capturar o tempo final após a execução da função
  fpGetTimeOfDay(@TempoFinal, nil);

  // Calcular o tempo de execução em segundos
  TempoExecucao := (TempoFinal.tv_sec - TempoInicial.tv_sec) + 
                   (TempoFinal.tv_usec - TempoInicial.tv_usec) / 1000000.0;

  // Exibir o tempo de execução
  WriteLn('Tempo de execução da função: ', TempoExecucao:0:6, ' segundos');
  {$ENDIF}

  SalvarTempo(n, TempoExecucao);
  WriteLn('Tempo salvo com sucesso.');
end;

end.
