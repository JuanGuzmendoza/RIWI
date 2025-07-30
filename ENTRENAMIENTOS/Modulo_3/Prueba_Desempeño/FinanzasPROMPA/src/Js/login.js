const LoginForm = document.getElementById("loginForm")

/*event that is triggered when people try to log in*/
LoginForm.addEventListener("submit", function (event) {

    const inputUsername = LoginForm.userName.value
    const inputPassword = LoginForm.userPassword.value
    login(inputUsername, inputPassword)

    event.preventDefault()
})


/*Function that communicates with the database to verify that the user can log in.*/ 
async function login(inputUsername, inputPassword) {
    let response = await fetch(`http://localhost:3000/users?userName=${inputUsername}`)
    let data = await response.json()

    if (data.length === 0) {
        alert("Incorrect credentials, check email or password")
    } else {
        const userFound = data[0]
        if (userFound.userPassword === inputPassword) {
            localStorage.setItem("currentUser", JSON.stringify(userFound))
            window.location.href = "../pages/balances.html"


        } else {
            alert("Incorrect credentials, check email or password")
        }
    }
}

