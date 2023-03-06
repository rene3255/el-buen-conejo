import {menu_display} from "./navbar/navbar.js";


const d=document;
/*DOMContentLoaded es la primera carga del documento
mas rapido que load */

d.addEventListener('DOMContentLoaded',(e)=>{
    /*menu-navbar */
    if(document.querySelector('.menu-mobile__icon')) menu_display("menu-mobile__icon","menu","menu-mobile__icon-clouse","menu_active");
    if(document.querySelector('.input-user-setting')) menu_display("input-user-setting","menu-user","input-user-setting-active","menu-user-active");
    
})