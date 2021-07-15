const vm = new Vue({
    el: '#app',
    data: {
        unitsIn: '',
        amount: '',
        unitsOut: '',
        // conversion: ''
    },
    methods: {
        getCurrency() {
            axios({
                method: 'get',
                url: 'https://api.exchangerate.host/latest',
                params: {
                    amount: this.amount,
                    from: this.unitsIn,
                    to: this.unitsOut
                }
            }).then((response) => {
                console.log(response.data.rates[this.unitsOut])
            })
        // },
        // clear() {
        //   conversion = ''  
        }
    }
})

