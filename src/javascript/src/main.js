// IMPLEMENTAÇÃO MERGE SORT EM JAVASCRIPT
const readline = require('readline');
const MergeSort = require('./MergeSort');

async function getInputs() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    const question = (query) => new Promise((resolve) => rl.question(query, resolve));

    const n = parseInt(await question('Digite o tamanho do vetor: '), 10);
    const arqE = await question('Digite o nome do arquivo de entrada: ');
    const arqS = await question('Digite o nome do arquivo de saída: ');

    rl.close();

    return { n, arqE, arqS };
}

async function main() {
    try {
        const inputs = process.argv.slice(2);
        let n, arqE, arqS;

        if (inputs.length === 3) {
            n = parseInt(inputs[0], 10);
            arqE = inputs[1];
            arqS = inputs[2];

            if (isNaN(n) || n <= 0) {
                console.error('Tamanho do vetor inválido!');
                return;
            }
        } else {
            const userInput = await getInputs();
            n = userInput.n;
            arqE = userInput.arqE;
            arqS = userInput.arqS;

            if (isNaN(n) || n <= 0) {
                console.error('Tamanho do vetor inválido!');
                return;
            }
        }

        const sorter = new MergeSort(arqE, arqS);
        await sorter.run(n);

        console.log('Execução em JavaScript finalizada');
        process.exit(0);
    } catch (error) {
        console.error('Erro:', error);
    }
}

main();
