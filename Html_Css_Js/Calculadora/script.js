

function obtainDate(){
    name_person=document.getElementById('nombre').value;
    height=document.getElementById('altura');
    weight=parseFloat(document.getElementById('peso').value);
    return {"name_person":name_person,
            "height":height,
            "weight":weight}
}

function calcularIndice(){
    dates=obtainDate()
    alert(dates.name_person+" su indice es : "+dates.weight/(dates.height**2))
}

