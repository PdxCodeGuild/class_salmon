const app = Vue.createApp({
    // data, functions
    // template: "<h2>I am a h2</h2>"

    data(){
        return{
            title: "i am the title",
            another: "here's another",
            number: 45,

        }
    },

    methods: {
        changeTitle(){
            this.another = "Change from line 16"
            console.log("line 16")
        }
    }
})

app.mount("#app") 

cll