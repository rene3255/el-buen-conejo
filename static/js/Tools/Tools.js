export function active_display(
    class_ancla_1="",class_ancla_2="",
    elment_active_1='',elment_desative_2=''
    ){
        const menu=document.querySelector("."+class_ancla_1);
        menu.addEventListener("click",(e)=>{
            const menu_ul=document.querySelector("."+class_ancla_2);
            if(menu.classList.contains(elment_active_1)){
                menu.classList.remove(elment_active_1);
                menu_ul.classList.remove(elment_desative_2);
            }else{
                menu.classList.add(elment_active_1);
                menu_ul.classList.add(elment_desative_2);
        
            }
        })
    }
export function MenuProfileGeneral(
    class_ancla="",
    button_active="",
    elment_active='',
    attribute=""
){
        const button=document.querySelectorAll('.'+class_ancla);
        button.forEach(el=>{
            el.addEventListener("click",(e)=>{
                const button=document.querySelector("."+button_active);
                const element=document.querySelector("."+button.getAttribute(attribute));
                const element_menu=document.querySelector("."+el.getAttribute(attribute));
                
                button.classList.remove(button_active);
                element.classList.remove(elment_active);
    
                el.classList.add(button_active);
                element_menu.classList.add(elment_active);
            })
        })
    }