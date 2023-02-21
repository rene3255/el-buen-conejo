import {
    Eye_password,
    validate_password,
    validate_Email
} from "./Tools.js";

const d=document;
/*DOMContentLoaded es la primera carga del documento
mas rapido que load */
/*
d.addEventListener('DOMContentLoaded',(e)=>{
    const form_login=document.querySelector('.form-login');
    if(form_login){
        form_login.addEventListener("submit",(e)=>{
            e.preventDefault();
            console.log(validate_password(form_login.password.value));
            console.log(validate_Email(form_login.email_username.value));
            form_login.submit();
        });
        console.log("se cargo");
    }
    Eye_password();
})
*/
