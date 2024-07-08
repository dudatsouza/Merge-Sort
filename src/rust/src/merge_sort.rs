use std::fs::{File, OpenOptions};
use std::io::{BufRead, BufReader, Write};
use std::time::Instant;

pub struct MergeSort {
    array: Vec<i32>,
    arq: String,
    arq2: String,
}

impl MergeSort {
    pub fn new(arq: String, arq2: String) -> MergeSort {
        MergeSort {
            array: Vec::new(),
            arq,
            arq2,
        }
    }

    fn merge(&mut self, v: &mut [i32], inicio: usize, meio: usize, fim: usize) {
        let mut temp = Vec::with_capacity(fim - inicio + 1);
        let (mut p1, mut p2) = (inicio, meio + 1);

        while p1 <= meio && p2 <= fim {
            if v[p1] <= v[p2] {
                temp.push(v[p1]);
                p1 += 1;
            } else {
                temp.push(v[p2]);
                p2 += 1;
            }
        }

        while p1 <= meio {
            temp.push(v[p1]);
            p1 += 1;
        }

        while p2 <= fim {
            temp.push(v[p2]);
            p2 += 1;
        }

        for (i, val) in temp.iter().enumerate() {
            v[inicio + i] = *val;
        }
    }

    fn merge_sort_helper(&mut self, v: &mut [i32], inicio: usize, fim: usize) {
        if inicio < fim {
            let meio = (inicio + fim) / 2;
            let (left, right) = v.split_at_mut(meio + 1);
            self.merge_sort_helper(left, inicio, meio);
            self.merge_sort_helper(right, 0, fim - meio - 1);
            self.merge(v, inicio, meio, fim);
        }
    }

    pub fn run(&mut self, n: usize) {
        self.definir_array(n);

        let start = Instant::now();
        let len = self.array.len();
        let mut array_copy = self.array.clone(); // Clonar o vetor para evitar mutabilidade simultânea
        self.merge_sort_helper(&mut array_copy, 0, len - 1);
        let duration = start.elapsed();

        self.salvar_tempo(n, duration.as_secs_f64());
    }

    fn definir_array(&mut self, n: usize) {
        let file = File::open(&self.arq).expect("Erro ao abrir o arquivo de entrada");
        let reader = BufReader::new(file);
        
        self.array.clear();
    
        // Lê a primeira linha do arquivo
        if let Some(Ok(line)) = reader.lines().next() {
            // Divide a linha em números separados por espaço
            for num_str in line.split_whitespace() {
                if self.array.len() >= n {
                    break;
                }
                if let Ok(num) = num_str.parse::<i32>() {
                    self.array.push(num);
                } else {
                    println!("Número inválido: {}", num_str);
                }
            }
        }
    }

    fn salvar_tempo(&self, n: usize, time_taken: f64) {
        let mut file = OpenOptions::new()
            .write(true)
            .append(true)
            .open(&self.arq2)
            .expect("Erro ao abrir o arquivo de saída");

        write!(file, "\nRust, {}, {:.10}, {}", n, time_taken, self.arq).expect("Erro ao escrever no arquivo");

        println!("\nTempo de execução: {:.10}", time_taken);
    }
}
