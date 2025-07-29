

const endPointUsers = 'http://localhost:3000/users';

const tableUser = document.getElementById('usersTableBody');
const formUser=document.getElementById("formUser")
const formUpdateUser = document.getElementById('updateUserForm');

document.addEventListener('DOMContentLoaded', async  function() {
    await paintTableUser();
});



//=============== CRUD USER ===============
// ## PAINT TABLE USER
async function paintTableUser() {
    let users = await obtainUser();
    for ( let elemente of users) {
        tableUser.innerHTML += `
        <tr>
            <td>${elemente.id}</td>
            <td>${elemente.name}</td>
            <td>
                <button class="btn btn-danger" onclick="deleteUser(${elemente.id})">Eliminar</button>
                <button class="btn btn-info btn-sm" onclick="modalUpdateUser(${elemente.id})">Actualizar</button>
            </tr>
        `;
    }    
}


// ## OBTAIN USER
async function obtainUser(){
    let promise= await fetch(endPointUsers);
    let usuarios= await promise.json();
    console.log(usuarios);
    return usuarios
}


async function modalUpdateUser(id) {
    const modal = new bootstrap.Modal(document.getElementById('updateUserModal'));
    document.getElementById('idUser').value = id;
    modal.show();
 
}


// ## UPDATE USER
formUpdateUser.addEventListener('submit', async function(e) {
    e.preventDefault();
     
    const id=document.getElementById('idUser').value;
    const userName = formUpdateUser.newNameUser.value;
    let promesa = await fetch(`${endPointUsers}/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ id:id,name: userName })
    });
    bootstrap.Modal.getInstance(document.getElementById('updateUserModal')).hide();
});

// ## ADD USER
async function addUser() {
    const user=await obtainUser();
    console.log(user.length);
    let newUser={
        id: (user.length + 1).toString(), 
        name: formUser.userName.value,
    }
    let promesa= await fetch(endPointUsers, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newUser)
    });
    console.log(await promesa.json());
}

// ## DELETE USER
async function deleteUser(id) {
    let promesa= await fetch(`${endPointUsers}/${id}`, {
        method: 'DELETE',
    });
    console.log(await promesa.json());
}
