const app = Vue.createApp({
    data() {
        return {
            btnIsDisabled: false,
            msgDone: '',
            inpVal: 500,
            arraySize: 500, 
            dice: [],
            keyNumber: 0,
            buttonText: 'Merge Sort'
        }
    },
    computed: {
        delay() {
            return 550 - this.inpVal;
        }
    },
    watch: {
        delay: {
            immediate: true,
            handler() {
                this.updateMoveDuration();
            },
        },
        arraySize: {
            immediate: true,
            handler(newSize) {
                this.updateDiceArray(newSize);
            }
        }
    },
    methods: {
        action() {
            if (this.buttonText === "Merge Sort") {
                this.mergeSort(0, this.dice.length);
            } else {
                this.updateDiceArray(this.arraySize);
            }
        },
        updateMoveDuration() {
            const stylesheet = document.styleSheets[0];
            const rules = Array.from(stylesheet.cssRules);
            const moveRule = rules.find(rule => rule.selectorText === '.v-move');
            if (moveRule) {
                moveRule.style.transitionDuration = `${this.delay}ms`;
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
            await new Promise(resolve => setTimeout(resolve, this.delay));
            await this.mergeSort(start, mid);
            await this.mergeSort(mid, end);

            await this.merge(start, mid, end);

            if (start === 0 && end === this.dice.length) {
                for (let i = 0; i < this.dice.length; i++) {
                    this.dice[i].isActive = false;
                    this.dice[i].isFinished = true;
                }
                this.btnIsDisabled = false;
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
            await new Promise(resolve => setTimeout(resolve, this.delay));

            while (i < mid && j < end) {
                await new Promise(resolve => setTimeout(resolve, this.delay));
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
                await new Promise(resolve => setTimeout(resolve, this.delay));
                diceEl.isChanging = false;
                diceEl.isActive = false;
                i++;
                pushIndex++;
            }

            while (j < end) {
                let diceEl = this.dice.splice(j, 1)[0];
                diceEl.isChanging = true;
                this.dice.splice(pushIndex, 0, diceEl);
                await new Promise(resolve => setTimeout(resolve, this.delay));
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
                await new Promise(resolve => setTimeout(resolve, this.delay));
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
                dieNmbr: Math.ceil(Math.random() * 290) + 10,
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
        }
    },
    mounted() {
        this.updateDiceArray(this.arraySize);
        this.updateMoveDuration();
    }
})
app.mount('#vueApp')
