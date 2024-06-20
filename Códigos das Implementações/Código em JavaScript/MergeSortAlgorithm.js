const fs = require('fs');
const readline = require('readline');

class MergeSortAlgorithm {
    constructor(arqE, arqS) {
        this.array = [];
        this.arq = arqE;
        this.arq2 = arqS;
    }

    merge(v, inicio, meio, fim) {
        let temp = [];
        let p1 = inicio, p2 = meio + 1;

        while (p1 <= meio && p2 <= fim) {
            if (v[p1] <= v[p2]) {
                temp.push(v[p1++]);
            } else {
                temp.push(v[p2++]);
            }
        }

        while (p1 <= meio) {
            temp.push(v[p1++]);
        }

        while (p2 <= fim) {
            temp.push(v[p2++]);
        }

        for (let i = 0; i < temp.length; i++) {
            v[inicio + i] = temp[i];
        }
    }

    mergeSort(v, inicio, fim) {
        let meio;
        if (inicio < fim) {
            meio = Math.floor((inicio + fim) / 2);
            this.mergeSort(v, inicio, meio);
            this.mergeSort(v, meio + 1, fim);
            this.merge(v, inicio, meio, fim);
        }
    }

    definirArray(n) {
        return new Promise((resolve, reject) => {
            fs.readFile(this.arq, 'utf8', (err, data) => {
                if (err) {
                    return reject(err);
                }

                this.array = data.split(/\s+/).map(Number);
                if (this.array.length > n) {
                    this.array = this.array.slice(0, n);
                }
                resolve();
            });
        });
    }

    salvarTempo(n, timeTaken) {
        const data = `\nJavaScript,${n},${timeTaken},${this.arq}`;
        fs.writeFileSync(this.arq2, data, { flag: 'a' });
    }

    printArray() {
        console.log(this.array);
    }

    async run(n) {
        await this.definirArray(n);

        const startTime = process.hrtime();
        this.mergeSort(this.array, 0, this.array.length - 1);
        const endTime = process.hrtime(startTime);
        const timeTaken = endTime[0] + endTime[1] / 1e9;

        this.salvarTempo(n, timeTaken);
    }
}

module.exports = MergeSortAlgorithm;
