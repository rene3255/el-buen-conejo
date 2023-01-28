const d=document;
/*DOMContentLoaded es la primera carga del documento
mas rapido que load */

d.addEventListener('DOMContentLoaded',(e)=>{
    const menu=document.querySelector(".menu-mobile__icon");
    menu.addEventListener("click",(e)=>{
        const menu_ul=document.querySelector(".menu");
        if(menu.classList.contains('menu-mobile__icon-clouse')){
            menu.classList.remove('menu-mobile__icon-clouse');
            menu_ul.classList.remove('menu_active');
        }else{
            menu.classList.add('menu-mobile__icon-clouse');
            menu_ul.classList.add('menu_active');

        }
    })
})