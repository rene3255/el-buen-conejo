export function Eye_password(){
    const eye_password=document.querySelector("#eye-password");
    if(eye_password){
        eye_password.addEventListener('click',(e)=>{
            const password=document.querySelector("#password");
            if(password){
               if(eye_password.classList.contains('eye-password-none')){
                    eye_password.classList.remove('eye-password-none');
                    eye_password.classList.add('eye-password-solid');
                    password.type="text";
               }else{
                    eye_password.classList.remove('eye-password-solid');
                    eye_password.classList.add('eye-password-none');
                    password.type="password";
               }
            }
        });
    }
}

export function valitate_string(value){
    return /^[A-Z]+$/i.test(value);
}

export function validate_Email(value) {
    return /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i.test(value)
}

export function validate_password_register(value){
    return {
        'leter':/[A-z]/.test(value),
        'upper':/[A-Z]/.test(value),
        'number':/\d/.test(value)
    }  
}

export function validate_password(value){
    return /[A-z]/.test(value)&&
           /[A-Z]/.test(value)&&
           /\d/.test(value)
}