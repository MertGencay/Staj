const {createApp} = Vue
    createApp({
        data(){
            return {
                name: "Mert", //String
                job: "Öğrenci",
                age: 21, //Integer
                giyim: {
                    sapka: true, //Boolean
                    pantolon: "kot",
                    tshirt: false //Boolean
                },
                yetenek: ["Sürücü","Yazılımcı","Boksör","Yüzücü"]
            }
        },
        methods: {
            hesapla: function(isim){
                return "İyi Günler " + isim;
            },            
            topla: function(){
                return 2 + 5;
            }
        }
    }).mount("#ilk-uygulama");