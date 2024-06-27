<?php

// IMPLEMENTAÇÃO MERGE SORT EM PHP
class MergeSort {
    private $array = [];
    private $arqE;
    private $arqS;

    public function __construct($arqE, $arqS) {
        $this->arq = $arqE;
        $this->arq2 = $arqS;
    }

    private function merge(&$v, $inicio, $meio, $fim) {
        $temp = [];
        $p1 = $inicio;
        $p2 = $meio + 1;
        $i = 0;

        while ($p1 <= $meio && $p2 <= $fim) {
            if ($v[$p1] < $v[$p2]) {
                $temp[$i++] = $v[$p1++];
            } else {
                $temp[$i++] = $v[$p2++];
            }
        }

        while ($p1 <= $meio) {
            $temp[$i++] = $v[$p1++];
        }

        while ($p2 <= $fim) {
            $temp[$i++] = $v[$p2++];
        }

        for ($j = 0, $k = $inicio; $j < count($temp); $j++, $k++) {
            $v[$k] = $temp[$j];
        }
    }

    private function mergeSort(&$v, $inicio, $fim) {
        if ($inicio < $fim) {
            $meio = (int) ($inicio + ($fim - $inicio) / 2);
            $this->mergeSort($v, $inicio, $meio);
            $this->mergeSort($v, $meio + 1, $fim);
            $this->merge($v, $inicio, $meio, $fim);
        }
    }

    private function definirArray($n) {
        $content = file_get_contents($this->arq);
        $numbers = explode(' ', $content);

        $this->array = [];

        foreach ($numbers as $num) {
            $num = trim($num);
            if ($num !== '') {
                $this->array[] = (int) $num;
            }
        }

        $this->array = array_slice($this->array, 0, $n);
    }

    private function salvarTempo($n, $time_taken) {
        $data = "\nPHP,$n," . number_format($time_taken, 10) . ",$this->arq";
        file_put_contents($this->arq2, $data, FILE_APPEND);
        echo "Tempo de execução:" . number_format($time_taken, 10);
    }

    public function run($n) {
        $this->definirArray($n);

        $start = microtime(true);
        $this->mergeSort($this->array, 0, count($this->array) - 1);
        $end = microtime(true);
        $time_taken = ($end - $start);

        $this->salvarTempo($n, $time_taken);
    }
}
?>
