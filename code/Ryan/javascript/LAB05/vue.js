const vm = new Vue({
    el: "#app",
    data: {
        results: [],
        qotd: {},
    },
    methods: {
        loadQotd: function(){
        axios({
            method: "get",
            url: "https://favqs.com/api/qotd/"
        }).then(response => console.log(response.data))
        },
    }
})





// const vm = new Vue({
//     el: '#app',
//     data: {
//         results: [],
//         qotd: {}
//     },
//     methods: {
//         loadQotd: function() {
//             axios({
//                 method: 'get',
//                 url: 'https://favqs.com/api/qotd/'
//             }).then(response => this.qotd = response.data).catch(console.log("error!"))
//         },
//         loadQuotes: function() {
//             axios({
//                 method: 'get',
//                 url: 'https://favqs.com/api/quotes/',
//                 headers: {
//                     "Authorization": `Token token="${apiKey}"`
//                 },
//                 params: {
//                     type: 'author',
//                     filter: 'abraham lincoln'
//                 }
//             }).then(response => this.results = response.data)
//         }
//     },
//     created: function() {
//         this.loadQotd()
//     }
// })

document.querySelector("#r0c0").innerHTML = vm.loadQotd.response.body.quote;
document.querySelector("#r0c1").innerHTML = vm.loadQotd;
document.querySelector("#r0c2").innerHTML = vm.loadQotd;
document.querySelector("#r0c3").innerHTML = vm.loadQotd;
document.querySelector("#r0c4").innerHTML = vm.loadQotd;
document.querySelector("#r1c0").innerHTML = vm.loadQotd;
document.querySelector("#r1c1").innerHTML = vm.loadQotd;
document.querySelector("#r1c2").innerHTML = vm.loadQotd;
document.querySelector("#r1c3").innerHTML = vm.loadQotd;
document.querySelector("#r1c4").innerHTML = vm.loadQotd;
document.querySelector("#r2c0").innerHTML = vm.loadQotd;
document.querySelector("#r2c1").innerHTML = vm.loadQotd;
document.querySelector("#r2c2").innerHTML = vm.loadQotd;
document.querySelector("#r2c3").innerHTML = vm.loadQotd;
document.querySelector("#r2c4").innerHTML = vm.loadQotd;
document.querySelector("#r3c0").innerHTML = vm.loadQotd;
document.querySelector("#r3c1").innerHTML = vm.loadQotd;
document.querySelector("#r3c2").innerHTML = vm.loadQotd;
document.querySelector("#r3c3").innerHTML = vm.loadQotd;
document.querySelector("#r3c4").innerHTML = vm.loadQotd;
document.querySelector("#r4c0").innerHTML = vm.loadQotd;
document.querySelector("#r4c1").innerHTML = vm.loadQotd;
document.querySelector("#r4c2").innerHTML = vm.loadQotd;
document.querySelector("#r4c3").innerHTML = vm.loadQotd;
document.querySelector("#r4c4").innerHTML = vm.loadQotd;

