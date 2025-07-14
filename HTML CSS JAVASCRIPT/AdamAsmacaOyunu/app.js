const wordsection = document.querySelector(".word");
const boardsection = document.querySelector(".board");
const figure = document.querySelector(".figure");
const letters = [
    "A",
    "B",
    "C",
    "Ç",
    "D",
    "E",
    "F",
    "G",
    "Ğ",
    "H",
    "I",
    "İ",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "Ö",
    "P",
    "R",
    "S",
    "Ş",
    "T",
    "U",
    "Ü",
    "V",
    "Y",
    "Z",
];

const human = ["head","body","rightarm","leftarm","rightleg","leftleg"];
let randomword = "";

const createkeyboard = () =>{
    boardsection.innerHTML = "";
    for (let a = 0; a <letters.length; a++){
        let square = document.createElement("div");
        square.classList.add("lettersquare");
        square.textContent = letters[a];
        boardsection.appendChild(square);
    }
}

const createWord = () => {
    wordsection.innerHTML = "";
    randomword = selectWord();
    for (let a = 0; a < 8; a++){
        let square = document.createElement("div");
        square.classList.add("square");
        square.setAttribute("data-value",randomword[a]);
        wordsection.appendChild(square);
    }
}

const selectWord = () => {
    const word = [
        "KİTAPLIK", "ÇALIŞMAK", "GÜZELLİK", "YAZILIMI", "OYUNCULU", "KÜTÜPHANE", "AKŞAMLIK",
        "DUVARLIK", "ARKADAŞIM", "BAŞLAMAK", "DÜŞÜNMEK", "GELİŞMEK", "TASARLAMA", "ÖZGÜRLÜK",
        "ÖĞRENCİ", "ŞİRKETİN", "TANITICI", "TECRÜBELİ", "BAĞIMLIK", "AKADEMİK", "YORUMLAR",
        "KURALLAR", "HARFLERİ", "GEÇİRMEK", "ÖNYARGILI", "ÇEVİRMEK", "EŞLEŞTİR", "ANLATMAK",
        "SONUÇLAR", "DERSLİK", "ÖNGÖRMEK", "KOMUTLAR", "BİRİMLER", "YENİLEME", "YENİLEŞİ",
        "EŞSİZDİR", "TUTARLIK", "BAĞLANTI", "AÇIKLAMA", "YANSIYAN", "YÖNELTEN", "ÇEKİRDEK",
        "DONANIM", "BİLİNÇLİ", "RESİMLER", "ÇÖZÜMLEM", "SİMGELER", "DUYARLIK", "ÇEVRİLME",
        "KAPSAMAK", "İZLENMEK", "İŞLENMEK", "DOĞRUSU", "YÜKLEMEK", "ÇALIŞKAN", "YARATICI",
        "KODLAMAK", "KURALLAR", "GÜNÜMÜZÜ", "ÖĞRETİCİ", "ARAÇLARI", "DETAYLAR", "ÇÖZÜLMEK",
        "İZLEYİCİ", "SEÇİMLER", "ETKİNLİK", "ANLAMAK", "İNCELEME", "TANIMLA", "ÖRNEKLER",
        "GÖRSELLER", "AKTARMAK", "ÇALIŞTAY", "YÖNELTEN", "ANALİZCİ", "ONAYLAMA", "BAŞLAMAK"
    ];
    const randomWord = Math.floor(Math.random()*word.length);
    return keyWord = Array.from(word[randomWord]);
};

const generatebody = (value) => {
    let bodypart = document.createElement("div");
    bodypart.classList.add(human[value]);
    figure.appendChild(bodypart);
};

const startgame = () => {
    createkeyboard();
    createWord();
    let buttons = document.querySelectorAll(".lettersquare");
    let squares = document.querySelectorAll(".square");
    let figuresection = document.querySelectorAll(".figure div");
    let wrongcount = 0;
    let correctcount = 0;
    figuresection.forEach(item => {
        if (!item.getAttribute("data-value")) item.remove()
    })
    buttons.forEach(item => {
        item.addEventListener("click",(e) => {
            let chosenletter = e.target.textContent;
            if (randomword.includes(chosenletter)){
                e.target.classList.add("correct");
                squares.forEach(item=>{
                    if (item.getAttribute("data-value") === chosenletter){
                        item.textContent = item.getAttribute("data-value");
                        item.classList.add("show");
                        correctcount++;
                    }
                })
                if (correctcount === 8){
                    buttons.forEach(item =>{
                        item.classList.add("close");
                    })
                    squares.forEach(item => {
                        item.style.background="green";
                    })
                    setTimeout(()=>{
                        startgame();
                    },3000)
                }
            }
            else {
                e.target.classList.add("wrong")
                wrongcount++;
                generatebody(wrongcount-1);
                if (wrongcount === 6){
                    buttons.forEach(item=>{
                        item.classList.add("close");
                    })
                    squares.forEach(item => {
                        item.classList.add("show");
                        item.style.background = "red";
                    })
                    setTimeout(()=>{
                        startgame();
                    },3000)
                }
            }
        })
    })
}

startgame();

