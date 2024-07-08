unit MergeSort;

interface

uses
  SysUtils, Classes, StrUtils;

type
  TMergeSort = object
  private
    dataArray: array of Integer;
    arq: string;
    arq2: string;
    procedure Merge(var v: array of Integer; inicio, meio, fim: Integer);
    procedure MergeSort(var v: array of Integer; inicio, fim: Integer);
    procedure DefinirArray(n: Integer);
    procedure MostrarArray;
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
  aux: Integer;
  line, numStr: string;
  num: Integer;
begin
  SetLength(dataArray, 0);

  Assign(fileIn, arq);
  Reset(fileIn);

  ReadLn(fileIn, line);

  // separar a string por espaços, colocando os numeros no array
  while Pos(' ', line) > 0 do
  begin
    numStr := Copy(line, 1, Pos(' ', line) - 1);
    Delete(line, 1, Pos(' ', line));
    num := StrToInt(numStr);

    aux := Length(dataArray);
    SetLength(dataArray, aux + 1);
    dataArray[aux] := num;
  end;  

  Close(fileIn);

  WriteLn('Tamanho do array após leitura: ', Length(dataArray));

  MostrarArray;
end;

procedure TMergeSort.MostrarArray;
var
  i: Integer;
begin
  WriteLn('Array: ');
  for i := 0 to High(dataArray) do
    Write(dataArray[i], ' ');
  WriteLn;
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

  WriteLn('Tempo de execução: ', timeTaken:10:10);
end;

procedure TMergeSort.Run(n: Integer);
var
  t1, t2: QWord;
  time_span: Double;
begin
  DefinirArray(n);

  t1 := GetTickCount64;
  MergeSort(dataArray, 0, Length(dataArray) - 1);
  t2 := GetTickCount64;

  time_span := (t2 - t1) / 1000;
  SalvarTempo(n, time_span);
end;

end.
