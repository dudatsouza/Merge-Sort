const readline = require('readline');
const MergeSortAlgorithm = require('./MergeSortAlgorithm');

async function main() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    const question = (query) => new Promise((resolve) => rl.question(query, resolve));

    try {
        let n, arqE, arqS;

        const inputs = process.argv.slice(2);
        if (inputs.length === 3) {
            n = parseInt(inputs[0], 10);
            arqE = inputs[1];
            arqS = inputs[2];

            if (isNaN(n) || n <= 0) {
                console.error('Tamanho do vetor inválido!');
                rl.close();
                return;
            }
        } else {
            n = parseInt(await question('Digite o tamanho do vetor: '), 10);
            arqE = await question('Digite o nome do arquivo de entrada: ');
            arqS = await question('Digite o nome do arquivo de saída: ');

            rl.close();

            if (isNaN(n) || n <= 0) {
                console.error('Tamanho do vetor inválido!');
                return;
            }
        }

        const sorter = new MergeSortAlgorithm(arqE, arqS);
        await sorter.run(n);

        console.log('Execução em JavaScript finalizada');
        process.exit()
    } catch (error) {
        console.error('Erro:', error);
        rl.close();
    }
}

main();
