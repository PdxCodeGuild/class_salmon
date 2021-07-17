const vm = new Vue({
    el: '#app',
    data: {
        unitsIn: '',
        amount: '',
        unitsOut: '',
        conversion: '',
        result: '',
        message: ''
    },
    methods: {
        getCurrency() {
            axios({
                method: 'get',
                url: 'https://api.exchangerate.host/convert',
                params: {
                    amount: this.amount,
                    from: this.unitsIn,
                    to: this.unitsOut
                }
            }).then((response) => {
                this.conversion = response.data.info.rate
                this.result = response.data.result
                this.message = `${this.amount} ${this.unitsIn.toUpperCase()} = ${this.result} ${this.unitsOut.toUpperCase()}`
                this.amount = ''
                this.unitsOut = ''
                this.unitsIn = ''
            })
        },
        clear() {
          this.message = ''
        }
    }
})

