import {
    Eye_password,
    valitate_string,
    validate_Email,
    validate_password,
    validate_password_register
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
            form_register.submit();
        });
        console.log("se cargo");
    }
    Eye_password();

    const input_password=document.querySelector('#password');
    if(input_password){
        input_password.oninput = function() {
            let aux=validate_password_register(input_password.value);
            for(let key in aux){
                let link=document.getElementById("password-"+key)
                //console.log(document.getElementById("password-"+key),"password-"+key);
                link.style.color=(aux[key])?"#38A169":"#E53E3E";
            }
        }
    }

})