const {createApp} = Vue

createApp({
    data(){
        return{

        }
    },
    methods: {
        isimYakala: function(){
            console.log("İsim alanına birşey yazdınız.");
        },
        yasYakala: function(){
            console.log("Yaş alanına birşey yazdınız.");
        }
    }
}).mount("#app");