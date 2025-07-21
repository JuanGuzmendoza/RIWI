

const endPointUsers = 'http://localhost:3000/usuarios'

const table = document.getElementById('tableBody');
const form = document.getElementById("formUser")




table.addEventListener("click", function (event) {
    if (event.target.classList.contains("btn-danger")) {
        const id = event.target.getAttribute("data-id");
        let seguro = confirm("Estas seguro?")

        if (seguro == true) {
            deleteUser(id)

        }
    }
})


document.addEventListener('DOMContentLoaded', async function () {
    await paintTable()

});


form.addEventListener('submit', function (event) {
    event.preventDefault();
    let newUser = {
        name: form.name.value,
        email: form.email.value,
        password: form.password.value,
    }
    addUser(newUser);
    

});

async function paintTable() {
    let users = await obtainUser();
    for (let elemente of users) {
        table.innerHTML += `
        <tr>
            <td>${elemente.id}</td>
            <td>${elemente.name}</td>
            <td>${elemente.email}</td>
            <td>

            <button data-id="${elemente.id}"class="btn btn-danger"
            >Delete</button>
            </td>
        </tr>
        `;
    }
}
async function obtainUser() {

    let promise = await fetch(endPointUsers);
    let usuarios = await promise.json();
    console.log(usuarios);
    return usuarios
}

async function addUser(user) {

    let promesa = await fetch(endPointUsers, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(user)
    });


}

async function deleteUser(id) {

    let promesa = await fetch(
        `${endPointUsers}/${id}`
        , {
            method: 'DELETE',
        });

    if (promesa.ok) {
        await paintTable()
    }
}

async function updateUser(id, user) {

    let promesa = await fetch(endPointUsers, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(user)
    });

    console.log(await promesa.json());

}
