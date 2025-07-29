

const table = document.getElementById('tableBody');
const form=document.getElementById("formUser")


document.addEventListener('DOMContentLoaded', async  function() {

    let users = await obtainUser();
    for ( let elemente of users) {
        table.innerHTML += `
        <tr>
            <td>${elemente.id}</td>
            <td>${elemente.role}</td>
            <td>${elemente.name}</td>
            <td>${elemente.email}</td>
            <td><img src="${elemente.avatar}" alt="Avatar" width="50"></td>
        </tr>
        `;
    }    
});


form.addEventListener('submit', function(event) {
    event.preventDefault(); 
    let newUser={
        role: form.role.value,
        name: form.name.value,
        email: form.email.value,
        password: form.password.value,
        avatar: form.foto.value
    }
    addUser(newUser);

});

async function obtainUser(){

    let promise= await fetch('https://api.escuelajs.co/api/v1/users');
    let usuarios= await promise.json();
    console.log(usuarios);
    return usuarios
}




async function addUser(user) {

    let promesa= await fetch('https://api.escuelajs.co/api/v1/users', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(user)
    });

    console.log(await promesa.json());

}
