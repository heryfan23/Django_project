// Declaration variables : let,var,const
document.addEventListener("DOMContentLoaded", function() {
    const body = document.body;
    const modeToggle = document.getElementById("mode"); 
    let img = document.querySelector(".img_nuit");
    const currentMode = localStorage.getItem("mode");
    let header = document.getElementsByTagName("header")[0];

    // Appliquer le mode actuel au chargement de la page
    if (currentMode === "night") {
        body.classList.add("night-mode");
        img.src = "../../static/images/nuit.webp"
        header.style = "background-color:blueviolet;color:white"

    } else {
        body.classList.remove("night-mode");
        img.src = "../../static/images/jour.webp"
        header.style = "background-color:red;color:white"

    }

    // Écouter les clics sur l'élément de commutation
    modeToggle.addEventListener("click", function() {
        // Basculer entre les modes
        console.log("teste");
        if (body.classList.contains("night-mode")) {
            body.classList.remove("night-mode");
            localStorage.setItem("mode", "day");
            img.src = "../../static/images/jour.webp"
            header.style = "background-color:red;color:white"

            
        } else {
            img.src = "../../static/images/nuit.webp"
            body.classList.add("night-mode");
            localStorage.setItem("mode", "night");
            header.style = "background-color:blueviolet;color:white"


        }
    });
});


// let miova = document.getElementById("mode");
// let miova1 = document.getElementById("mode1");
// let img = document.querySelector(".img_nuit");
// let img1 = document.querySelector(".img_jour");
// let sary = document.getElementById("img_jour")


// miova.addEventListener("click", teste)
// function teste() {
//     if (miova.click) {
//         body.style = "background-color:black;color:white"
//         img1.style.display="block"
//         sary.src = "../../static/images/jour.webp"
//         img.style.display="none"
//     } 
// }
// miova1.addEventListener("click", teste1)
// function teste1() {
//         body.style = "background-color:white;color:black"
//         img1.style.display="none"
//         sary.src = "../../static/images/jour.webp"
//         img.style.display="block"
// }

