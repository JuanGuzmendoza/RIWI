const LoginForm = document.getElementById("loginForm")

LoginForm.addEventListener("submit", function (event) {

    const inputUsername = LoginForm.userName.value
    const inputPassword = LoginForm.userPassword.value
    login(inputUsername, inputPassword)

    event.preventDefault()
})


async function login(inputUsername, inputPassword) {
    let response = await fetch(`http://localhost:3000/users?userName=${inputUsername}`)
    let data = await response.json()

    if (data.length === 0) {
        //Cambiar por alerta con css
        alert("credenciales incorrectas, revisa el correo o la contraseña")
    } else {
        const userFound = data[0]
        if (userFound.userPassword === inputPassword) {
            localStorage.setItem("currentUser", JSON.stringify(userFound))
            window.location.href = "dashboard.html"


        } else {
            //Cambiar por alerta con css
            alert("credenciales incorrectas, revisa el correo o la contraseña")
        }
    }
}

