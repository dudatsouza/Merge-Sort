<?php

require 'MergeSortAlgorithm.php';

function prompt($prompt) {
    echo $prompt;
    return rtrim(fgets(STDIN));
}

function main() {
    $n = (int) prompt("Digite o tamanho do vetor: ");
    $arqE = prompt("Digite o nome do arquivo de entrada: ");
    $arqS = prompt("Digite o nome do arquivo de saída: ");

    $sorter = new MergeSortAlgorithm($arqE, $arqS);
    $sorter->run($n);

    echo "Execução em PHP finalizada\n";
}

main();
?>
