import {
    Eye_password,
    valitate_string,
    validate_Email,
    validate_password
} from "./Tools.js";

const d=document;
/*DOMContentLoaded es la primera carga del documento
mas rapido que load */

d.addEventListener('DOMContentLoaded',(e)=>{
    const form_register=document.querySelector('.form-register');
    if(form_register){
        form_register.addEventListener("submit",(e)=>{
            e.preventDefault();
            console.log(valitate_string(form_register.name.value));
            console.log(valitate_string(form_register.last_name.value));
            console.log(validate_Email(form_register.email.value));
            console.log(validate_password(form_register.password.value));
            //form_register.submit();
        });
        console.log("se cargo");
    }
    Eye_password();
})