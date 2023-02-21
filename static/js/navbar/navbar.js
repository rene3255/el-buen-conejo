export function menu_display(
class_ancla_1="",class_ancla_2="",
button_active_1='',detail_active_2=''
){
    const menu=document.querySelector("."+class_ancla_1);
    menu.addEventListener("click",(e)=>{
        const menu_ul=document.querySelector("."+class_ancla_2);
        if(menu.classList.contains(button_active_1)){
            menu.classList.remove(button_active_1);
            menu_ul.classList.remove(detail_active_2);
        }else{
            menu.classList.add(button_active_1);
            menu_ul.classList.add(detail_active_2);
    
        }
    })
}