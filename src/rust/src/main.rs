mod merge_sort;

use std::io;
use std::io::Write;

fn main() {
    let mut input = String::new();

    print!("Digite o tamanho do vetor: ");
    io::stdout().flush().unwrap();
    io::stdin().read_line(&mut input).expect("Falha ao ler linha");
    let n: usize = input.trim().parse().expect("Digite um número válido");

    input.clear();

    print!("Digite o nome do arquivo de entrada: ");
    io::stdout().flush().unwrap();
    io::stdin().read_line(&mut input).expect("Falha ao ler linha");
    let arq_e = input.trim().to_string();

    input.clear();

    print!("Digite o nome do arquivo de saída: ");
    io::stdout().flush().unwrap();
    io::stdin().read_line(&mut input).expect("Falha ao ler linha");
    let arq_s = input.trim().to_string();

    let mut sorter = merge_sort::MergeSort::new(arq_e, arq_s);
    sorter.run(n);

    println!("Execução em Rust finalizada.");
}
