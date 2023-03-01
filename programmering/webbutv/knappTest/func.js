//https://docs.github.com/en/get-started/getting-started-with-git/associating-text-editors-with-git
//$ git config --global core.editor "'C:/Program Files (x86)/sublime text 3/subl.exe' -w"

//https://phoenixnap.com/kb/how-to-vim-save-quit-exit

//knapp fel https://codingbeautydev.com/blog/javascript-cannot-read-property-addeventlistener-of-null/

let siffra = 0;
//const siffra 0;
//var siffra = 0; Använd ej var för bryter utanför blocken men let och const!
{
    var var_variabel = "block med var variabel som bryter utanför blocket";
    let let_variabel = "blocke med let variabel";    
}
function plusClick(){
    
    siffra = siffra + 1;
    console.log(`klick ${siffra}`);
    document.getElementById("taltext").innerHTML = siffra;    
}

const minusknapp = document.getElementById("minus");
minusknapp.addEventListener("click", minusClick);
//console.log(`minusknapp type off= ${typeof(minusknapp)}`)

function minusClick(){
    siffra--;
    console.log(`siffra= ${siffra}`);
    document.getElementById("taltext").innerHTML = siffra;
}

console.log(`var_variabel = ${var_variabel}`);
//console.log(`let_variabel = ${let_variabel}`);

