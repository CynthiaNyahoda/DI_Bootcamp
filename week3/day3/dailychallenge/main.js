const username = document.forms["myform"]["username"];
const letters = /^[a-zA-Z]*$/;


username.addEventListener('keyup', (e) =>{
    if (e.keycode === 13){
        console.log(e.target.value)
    }
})

function validation(){
  
    if( username.value =='') {
        alert ("username must be complete!!");
        return false;
    }

    if (!username.value.match(letters)){
        alert ("username Must contain only alphabets");
        return false
    }
   
    return true;
}


function gettext(e) {
   let key
   if(window.event){
    key = e.keycode
    console.log(key)
   }
   else if (e.which){
    key = e.which
    console.log(key)
   }
   const str = document.getElementById('infor').innerHTML
   str += String.fromCharCode(key)
   document.getElementById('infor'). innerHTML = str
}