var passed=false;
document.querySelector('form').addEventListener('change', function(event){
    if (event.target.id === 'id_transaction_type'){
        updateTypeTransaction();
        passed=true;
    } 

});

function updateTypeTransaction(){
  if (id_transaction_type.value === 'I'){
    id_credit.disabled = false
    var myValue = document.getElementById('id_debit');
    myValue.value = "";
    id_debit.disabled = true;
    
  } else {
    id_debit.disabled = false;
    var myValue = document.getElementById('id_credit');
    myValue.value = "";
    id_credit.disabled = true
  }
}

if (passed == false) {
    /* 
    var transaction_type = document.getElementById('id_transaction_type').value;
    */
    id_debit.disabled = false;
    var id_credit_field = document.getElementById('id_credit').value;
    id_credit.disabled = true
}

