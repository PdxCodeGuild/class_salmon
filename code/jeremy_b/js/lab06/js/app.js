/* declare API URLs here */
const NASA_API = "https://api.nasa.gov/planetary/apod?api_key=" + NASA_KEY;
const N2OY_TLE = "https://api.n2yo.com/rest/v1/satellite/tle/";

/* Vue stuff*/
/* components */
/* load banner image */
Vue.component('apod', {
    //template: "<div></div>",
    template:'<div><img v-bind:src="bannerUrl" alt="NASA APOD"></div>',
    data: function(){
        return{
            "bannerUrl": ""
        }
    },
    created: function(){
        axios.get(NASA_API).then(response => this.bannerUrl = response.data.url);
    }
});

/* Satellite search by ID */
Vue.component('sat-search', {
    template:`<div><input type="text" v-model="satId"><button type="submit" @click="getSatInfo">Get Sat Info</button></div>`,
    data: function(){
        return{
            "satId": ""
        }
    },
    methods:{
        updateSatId: function(satId) {
            this.$emit('search-input', satId);
        },
        getSatInfo: function() {
            this.$emit('get-sat-info', this.satId);
        }
    }
});

/* main app */
const vm = new Vue({
    el: "#app",
    data: {
        "id": "",
        "satInfo": []
    },
    methods: {
        showSatInfo: function(satId){
            console.log(satId);
            this.id = satId;
            console.log(this.id);
            url = N2OY_TLE + this.id + "&apiKey=" + N2OY_KEY;
            console.log(url);
            axios.get(url).then(response =>  this.satInfo = response.data);
            console.log(this.satInfo);
        }
    }
});


/* Tabby.js stuff*/
var tabs = new Tabby(
    '[data-tabs]',
    {
        idPrefix: "tabby-toggle_",
    });

/* Other JS */