//https://javascript.info/localstorage
//https://www.freecodecamp.org/news/how-to-use-javascript-collections-map-and-set/
//https://www.youtube.com/watch?v=U693xrQKFy4

//let billista = JSON.parse(localStorage.getItem("bilarlistan"));

class Bil {

    constructor(brand, color, bid){
        this.brand = brand;
        this.color = color;
        this.bid = bid;
    }
}

let billista = [];

/**getDataFromLocalStorage() Hämtar data localstorage */ 
async function getDataFromLocalStorage(){
    try {
          
        billista = await JSON.parse(localStorage.getItem("bilarlistan") );

        //Om billistan  är tom Null från localStorage
        if (billista == null)
            billista = []
        
        lista_bilar_div.innerHTML = "";
        
        //if (billista != null)
        billista.forEach(createHtmlBilLista);
    }
    catch (e){
        
        console.log(`Fel: ${e}`)
    }
}

getDataFromLocalStorage();

const addbutton = document.getElementById("addbutton");
const brand = document.getElementById("brand");
const color = document.getElementById("color");
const lista_bilar_div = document.getElementById("listabilarDiv");

addbutton.addEventListener("click", addButtonClick);
//console.log(`minusknapp type off= ${typeof(minusknapp)}`)

/**createHtmlBilLista Skapar Elementen i div för billistan-----*/
const createHtmlBilLista = (bil) => {
    //skapar element
    const bildiv = document.createElement('div');
    bildiv.className = "bil_div_element"
    const bilH2 = document.createElement('h3');
    const bilPcolor = document.createElement('p');
    const bilDelButt = document.createElement('button');
    //Fyller innehåll
    bilH2.innerText = `${bil.brand}`
    bilPcolor.innerText = `Färg: ${bil.color}`
    bilDelButt.innerText = "Delete"
    bilDelButt.id = bil.bid;
    //bilDelButt.addEventListener("click", deleteBil);
    //Lägger till till DOM
    bildiv.append(bilH2, bilPcolor, bilDelButt);
    lista_bilar_div.appendChild(bildiv);

};

/**addButtonClick() Lägger till bill till listan ---------*/
function addButtonClick(){
    
    console.log(`color= ${brand.value}`)
    const now = Date.now(); 
    const id = now.toString()
    let brandname = brand.value;

    if (brandname != ""){
        let car = new Bil(brand.value, color.value, id);
        billista.push(car);
        
        localStorage.setItem("bilarlistan" , JSON.stringify(billista));
        brand.value = "";
        color.value = "";

        lista_bilar_div.innerHTML = "";

        billista.forEach(createHtmlBilLista);
    }
    else
        alert("Måste fylla i fabrikat")

    brand.focus();
}

/**deletBil() tarbort bil--------------- */
let deleteBil = (e) => {

        const ny_billista = billista.filter((o, i) => o.bid !== e.target.id)
        //console.log(`ny_billista= ${JSON.stringify(ny_billista)}`)

        //Tilldelar ny_billista till gamla billistan
        billista = ny_billista;
        //Skriver till localstorage
        localStorage.setItem("bilarlistan" , JSON.stringify(billista));
        //läser från localstorage och skriver html elementen
        getDataFromLocalStorage();    
}

window.addEventListener("click", deleteBil);















