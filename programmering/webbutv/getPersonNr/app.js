//https://www7.skatteverket.se/portal/apier-och-oppna-data/utvecklarportalen?dataresurs=oppna-data
//https://skatteverket.entryscape.net/rowstore/dataset/b4de7df7-63c0-4e7e-bb59-1f156a591763?_limit=1&_offset=3
//https://skatteverket.entryscape.net/rowstore/dataset/b4de7df7-63c0-4e7e-bb59-1f156a591763?_limit=2&_offset=3
//${Math.floor(Math.random() * 20000)} rundar och slumpar till ett heltal mellan 0-2000

const psvar = document.getElementById("svaret")

//Button clicked
function getPersonNr() {
    


    fetch(
        `https://skatteverket.entryscape.net/rowstore/dataset/b4de7df7-63c0-4e7e-bb59-1f156a591763?_limit=1&_offset=${Math.floor(Math.random() * 20000)}`,
        {
            method: "GET",
            headers: new Headers({
                Accept: "application/json"
            })
        }
    )
        .then(res => res.json())
        .then(response => {
            //console.log(response);
            
            let responsearray = response.results;
            console.log(responsearray[0])
            const prsnr = responsearray[0].testpersonnummer;
            psvar.innerHTML= prsnr  + " " + getGender(prsnr);
            
            //console.log(response.data.results);
        })
        .catch(error => console.log(error));       

}

//Returns the gender symbol from personnummer
function getGender(personnummer){
    let second_last_nr_str = personnummer.substr(10, 1);
    let second_last_nr = parseInt(second_last_nr_str);

    let rstr = ""
    // &#9794; &#9792; U+2640 U+2642
    if (second_last_nr % 2 === 0){
        //console.log("F");
        rstr = '\u2640';
    }
    else {
        //console.log("M");
        rstr = '\u2642';
    }

    return rstr;
}