const app = Vue.createApp({
    data() {
        return {
            btnIsDisabled: false,
            msgDone: '',
            arraySize: 10,
            numExecutions: 5,
            dice: [],
            keyNumber: 0,
            buttonText: 'Merge Sort',
            executionTimes: [],
            arraySizes: []
        }
    },
    methods: {
        async action() {
            if (this.buttonText === "Merge Sort") {
                this.executionTimes = [];
                this.arraySizes = [];
                let sizes = Array.from({ length: this.numExecutions }, (_, i) => Math.floor(this.arraySize / this.numExecutions) * (i + 1));
                for (let size of sizes) {
                    this.updateDiceArray(size);
                    let startTime = performance.now();
                    await this.mergeSort(0, this.dice.length);
                    let endTime = performance.now();
                    this.executionTimes.push(endTime - startTime);
                    this.arraySizes.push(size);
                }
                this.plotGraph(sizes, this.executionTimes);
                this.btnIsDisabled = false;
                this.msgDone = 'DONE!';
                this.buttonText = 'New Values';
            } else {
                this.updateDiceArray(this.arraySize);
            }
        },
        async mergeSort(start, end) {
            if (end - start <= 1) {
                return;
            }
            for (let i = start; i < end; i++) {
                this.dice[i].top += 10;
            }
            this.btnIsDisabled = true;

            const mid = Math.floor((start + end) / 2);
            await new Promise(resolve => setTimeout(resolve, 100));
            await this.mergeSort(start, mid);
            await this.mergeSort(mid, end);

            await this.merge(start, mid, end);

            if (start === 0 && end === this.dice.length) {
                for (let i = 0; i < this.dice.length; i++) {
                    this.dice[i].isActive = false;
                    this.dice[i].isFinished = true;
                }
                this.msgDone = 'DONE!';
                this.buttonText = 'New Values';
            }
        },
        async merge(start, mid, end) {
            let i = start;
            let j = mid;
            let pushIndex = start;
            for (let k = start; k < end; k++) {
                this.dice[k].isActive = true;
            }
            await new Promise(resolve => setTimeout(resolve, 100));

            while (i < mid && j < end) {
                await new Promise(resolve => setTimeout(resolve, 100));
                let diceEl;
                if (this.dice[i].dieNmbr < this.dice[j].dieNmbr) {
                    diceEl = this.dice.splice(i, 1)[0];
                } else {
                    diceEl = this.dice.splice(j, 1)[0];
                    mid++;
                    j++;
                }
                diceEl.isChanging = true;
                this.dice.splice(pushIndex, 0, diceEl);
                await new Promise(resolve => setTimeout(resolve, 100));
                diceEl.isChanging = false;
                diceEl.isActive = false;
                i++;
                pushIndex++;
            }

            while (j < end) {
                let diceEl = this.dice.splice(j, 1)[0];
                diceEl.isChanging = true;
                this.dice.splice(pushIndex, 0, diceEl);
                await new Promise(resolve => setTimeout(resolve, 100));
                diceEl.isChanging = false;
                diceEl.isActive = false;
                pushIndex++;
                j++;
                i++;
                mid++;
            }

            while (i < mid) {
                let diceEl = this.dice.splice(i, 1)[0];
                diceEl.isChanging = true;
                this.dice.splice(pushIndex, 0, diceEl);
                await new Promise(resolve => setTimeout(resolve, 100));
                diceEl.isChanging = false;
                diceEl.isActive = false;
                pushIndex++;
                i++;
            }
            for (let t = start; t < end; t++) {
                this.dice[t].top -= 10;
                this.dice[t].isActive = false;
            }
        },
        addDie() {
            const newDie = {
                dieNmbr: Math.ceil(Math.random() * 190) + 10,
                left: 0,
                isActive: false,
                isChanging: false,
                keyNmbr: this.keyNumber,
                isFinished: false
            };
            this.dice.push(newDie);
            this.keyNumber++;
        },
        updateDiceArray(size) {
            this.dice = [];
            for (let i = 0; i < size; i++) {
                this.addDie();
            }
            this.buttonText = "Merge Sort";
            this.msgDone = '';
        },
        plotGraph(sizes, times) {
            const ctx = document.getElementById('chart').getContext('2d');
            const nLogN = sizes.map(n => 330 * n * Math.log(n));
            new Chart(ctx, {
                type: 'line',
                data: {
                    labels: sizes,
                    datasets: [
                        {
                            label: 'O(n log n)',
                            data: nLogN,
                            borderColor: 'rgba(255, 99, 132, 1)',
                            fill: false
                        },
                        {
                            label: 'Execution Times',
                            data: times.map((time, index) => ({ x: sizes[index], y: time })),
                            backgroundColor: 'rgba(54, 162, 235, 1)',
                            pointRadius: 5,
                            pointHoverRadius: 7,
                            borderWidth: 1
                        }
                    ]
                },
                options: {
                    scales: {
                        x: {
                            title: {
                                display: true,
                                text: 'Tamanho do Array'
                            }
                        },
                        y: {
                            title: {
                                display: true,
                                text: 'Tempo (ms)'
                            }
                        }
                    }
                }
            });
        }
    },
    mounted() {
        this.updateDiceArray(this.arraySize);
    }
});

app.mount('#vueApp');