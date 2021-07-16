
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
// Vue.component('rates-layout', , {
//     // data: function() {
//     //     return {quoteResponse:{}}
//     // },
//     template: '\
//       <li>\
//         The residential rate in {{ cityName }}is ${{ residentialRate }} per kWh.\
//       </li>\
//     ',
//     props: ['cityName', 'residentialRate'],
//   })
// Vue.component('rate-items', {
//     template: '\
//     <template>\
//       <ul>\
//         <p>The residential rate for electricity is ${{ residentialRate }} per kWh</p>\
//         <p>The commercial rate for electricity is ${{ commercialRate }} per kWh</p>\
//         <p>The industrial rate for electricity is ${{ industrialRate }} per kWh</p>\
//         <h3 class="subtitle">Operating companies in this service area include:</h3>\
//         <li \
//         v-for="index in utilityInfo"\
//         v-bind:key="index.id"\
//         >{{ index.utility_name }}</li>\
//       </ul>\
//       <img src"https://api.mapbox.com/styles/v1/mapbox/streets-v11/statichttps://api.mapbox.com/styles/v1/mapbox/dark-v10/static/{{ latlonResponse.latt }},{{ latlonResponse.longt }},10,0/275x200?access_token=pk.eyJ1IjoiYXplcm1hbiIsImEiOiJja3I1YXgzYmszM2o2Mm9xcGd6NThkZTZjIn0.O3OKKsfIG0ZyyF-LvNdu_g"></img>\
//     </template>\
//     ',
//     props: ['residentialRate', 'commercialRate', 'industrialRate', 'utilityInfo', 'latlonResponse.latt', 'latlonResponse.longt']
//   })
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
        variableCheck: false,
        mapUrl: ""
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
                this.variableCheck = true
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
                this.commercialRate = response.data.outputs.commercial,
                this.residentialRate = response.data.outputs.residential,
                this.industrialRate = response.data.outputs.industrial,
                this.mapUrl = `https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v11/static/${this.latlonResponse.longt},${this.latlonResponse.latt},8.75,0/350x240?access_token=pk.eyJ1IjoiYXplcm1hbiIsImEiOiJja3I1YXgzYmszM2o2Mm9xcGd6NThkZTZjIn0.O3OKKsfIG0ZyyF-LvNdu_g`,
                console.log(String(this.mapUrl))
                console.log(response.data.outputs.utility_info),
                console.log(response.data.outputs),
                console.log(this.latlonResponse)}
            )
        },
    },
});
vm.use(VueMaterial.default)

      new Vue({
        el: '#app'
      })