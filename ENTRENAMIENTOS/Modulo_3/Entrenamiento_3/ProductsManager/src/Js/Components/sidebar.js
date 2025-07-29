
//Funcion que agrega el sidebar en la vista correspondiente
export function paintSidebar(vista) {
    fetch('../pages/components/sidebar.html')
    .then(Response =>Response.text())
    .then(html=> {
        document.getElementById("sidebar").innerHTML=html;
        const lgoutBtn=document.getElementById("logout-btn");

        //Creacion de evento para el boton de cerrar sesion
        lgoutBtn.addEventListener('click',logoutSeccion)
        
        //llamado de la funcion para pintar el boton de la vista en el sidebar
        paintVist(vista)
    })

}

//Funcion que borra el usuario en el Local Storage y redirecciona a el index
function logoutSeccion(){
    localStorage.removeItem("currentUser")
    window.location.href="/"
}

//Funcion que agrega la clase de active para activar el boton en el sidebar
function paintVist(vista){
    let b=document.getElementById(vista)
    b.classList.add("active")
}