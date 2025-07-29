
function ageValidation(){
    let user_name=document.getElementById("nombre").value;
    let user_age=parseInt(document.getElementById("edad").value);
    let label_errors=document.getElementById("errors");
    if (!user_age || !user_name) {
        return label_errors.textContent="! Please complete all inputs !"
    }

    if (user_age ==0 || user_age <=0) {
        return label_errors.textContent="! Please only numbers greater than 0 !"
    }

    if (user_age>=18) {
        
        let form_div=document.getElementById("form_div");
        form_div.innerHTML = `<h2>You are of legal age, <span style="color: green;">${user_name}</span> 🎉</h2>`;
    }else{
        let form_div=document.getElementById("form_div");
        form_div.innerHTML = `<h2>You are not of legal age, <span style="color: red;">${user_name}</span> ❌</h2>`;
    }
}