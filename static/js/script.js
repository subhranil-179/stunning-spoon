const hamBtn = document.querySelector(".ham-menu");
const hamOpenIcon = document.querySelector("#ham-open-svg");
const hamCloseIcon = document.querySelector("#ham-close-svg");
const navMid = document.querySelector(".nav-mid");

let isHamClose = true;

hamBtn.addEventListener("click", (e)=>{
    if (isHamClose){
        navMid.style.top = 0;
        hamOpenIcon.style.display = "none";
        hamCloseIcon.style.display = "block";
        isHamClose = false;
    }
    else{
        navMid.style.top = "calc(-100% - 60px)";
        hamOpenIcon.style.display = "block";
        hamCloseIcon.style.display = "none";
        isHamClose = true;
    }
})
