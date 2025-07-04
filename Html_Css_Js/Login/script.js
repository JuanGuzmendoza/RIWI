let usuarios = [
  {
    id: 1,
    user_name: "a",
    user_password: "a",
    name:"maria",
  },
  {
    id: 2,
    user_name: "juanguzman10102005",
    user_password: "claveSegura!2024",
    name:"maria",
  },
  {
    id: 3,
    user_name: "carlos_ramirez",
    user_password: "claveSegura!2024",
    name:"maria",
  }
];


function loginUser(){
    let user_name=document.getElementById("user").value;
    let user_password=document.getElementById("password").value;
    let label_errors=document.getElementById("errors");
    if (!user_name || !user_password){
        return label_errors.textContent="! fill in all fields !"
    }
    let user_found = usuarios.find(function(usuario) {
    return usuario.user_name == user_name && usuario.user_password == user_password;
     });
    if (user_found){
        let login_div=document.getElementById("login_div");
        console.log(user_found)
        login_div.innerHTML = `<h2>Bienvenido, <span style="color: green;">${user_found.name}</span> 🎉</h2>`;
    }else{
        label_errors.textContent="User not found"
    }
}