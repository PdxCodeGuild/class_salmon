const vm = new Vue({
    el: '#app',
    data: {
        unitsIn: '',
        amount: '',
        unitsOut: '',
        conversion: '',
        result: '',
        message: `${this.amount} ${this.unitsIn} = ${this.result} ${this.unitsOut}`
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
            })
        },
        clear() {
          this.result = ''
        }
    }
})

