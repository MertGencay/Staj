const {createApp} = Vue

createApp({
    data(){
        return{
            age: 20,
            a: 0,
            b: 0,
        }
    },
    methods: {
        
    },
    computed: {
        aYaEkle(){
            return this.a + this.age;
        },
        bYeEkle(){
            return this.b + this.age;
        }
    }
}).mount("#app");