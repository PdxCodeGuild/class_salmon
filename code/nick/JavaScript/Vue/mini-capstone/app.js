
// Vue.component('qotd', {
//     data: function() {
//         return {quoteResponse:{}}
//     },
//     template: `
//         <div>
//         <button v-on:click="loadQuote">Quote of the Day</button>
//         <p v-if="quoteResponse.quote">{{ quoteResponse.quote.body }}</p>
//         <p v-if="quoteResponse.quote"><i><a v-bind:href="quoteResponse.quote.url">{{ quoteResponse.quote.author }}</a></i></p>
//         </div>
//     `,
//     methods: {
//         loadQuote: function() {
//             axios({
//                 method: "get",
//                 url: "https://favqs.com/api/qotd",
//             }).then(response => {
//                 this.quoteResponse = response.data;
//                 console.log(response.data)
//             })
//         },
//     },
// })
let vm = new Vue({
    el: '#app',
    data: {
        latlonResponse: {},
        rateResponse: {},
        addressInput: "",
        limitInput: "",
        format: "json",
        utilityInfo: [],
        cityName: "",
        commercialRate: [],
        residentialRate: [],
        industrialRate: [],
        // pageInput: 1,
    },
    methods: {
        loadLatlong: function () {
            axios({
                method: "get",
                url: "https://geocode.xyz/",
                params: {
                    region: "US",
                    locate: this.addressInput,
                    geoit: "json",
                    auth: apiKey2
                },
            }).then(response => {
                this.latlonResponse = response.data
                this.cityName = response.data.standard.city
                console.log(response.data.standard.city)
                this.loadRates()
            }
            ),
            loadRates()
        },
        loadRates: function() {
            axios({
                method: "get",
                // url: `https://developer.nrel.gov/api/alt-fuel-stations/v1.${this.format}`, //This works without a CROS
                url: `https://developer.nrel.gov/api/utility_rates/v3.${this.format}`, 
                // headers: {
                //     "X-Api-Key": `${apiKey}`,
                // },
                params: {
                    api_key: apiKey,
                    lat: this.latlonResponse.latt,
                    lon: this.latlonResponse.longt,
                    limit: this.limitInput,
                    // address: addressInput
                },
                // url: `https://favqs.com/api/quotes/?filter=${filter}&type=${type}`,
            }).then(response => {this.rateResponse = response.data,
                this.utilityInfo = response.data.outputs.utility_info,
                this.commercialRate = response.data.outputs.commericial,
                this.residentialRate = response.data.outputs.residential,
                this.industrialRate = response.data.outputs.industrial,
                console.log(response.data.outputs.utility_info)
                console.log(response.data.outputs),
                console.log(this.latlonResponse)}
            )
        },
    },
});