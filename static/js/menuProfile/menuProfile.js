export function MenuProfile(){
    const button=document.querySelectorAll('.button-menu-profile');
    button.forEach(el=>{
        el.addEventListener("click",(e)=>{
            const button=document.querySelector(".active-button-menu-profile");
            const element=document.querySelector("."+button.getAttribute("loadElement"));
            const element_menu=document.querySelector("."+el.getAttribute("loadElement"));
            
            button.classList.remove("active-button-menu-profile");
            element.classList.remove("active-element-profile");

            el.classList.add("active-button-menu-profile");
            element_menu.classList.add("active-element-profile");
            //console.log(button,element,element_menu);
        })
        //console.log(el.getAttribute("loadElement"),el.classList.contains("active-button-menu-profile"));
    })
}