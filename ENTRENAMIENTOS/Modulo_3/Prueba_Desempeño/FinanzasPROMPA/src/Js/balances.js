import { paintSidebar } from './Components/sidebar'

// ========== ENDPOINTS ==========
const endpointCategories = "http://localhost:3000/categories"
const endpointProcesses = "http://localhost:3000/operations"

// ========== ELEMENTS DOM ==========

const btnModalProcessCreate = document.getElementById("btnModalCreateProcess")
const formProcesses = document.getElementById("form-processes")
const tbodyProcesses = document.getElementById("tbody-processes")
const formEditarProcess = document.getElementById("formEditProcess")
const modalProcessesEdit = document.getElementById("modal-editar")
const modalProcessesCreate = document.getElementById("modal-create")



async function countBalance(){
    let datos=await getProcesses()
    let earnings=0;
    let bills=0;
    let total=0;
    const processesCompras = datos.filter(dato => dato.tipe === "Spent");
    processesCompras.forEach(pc=>{
        bills+=parseInt(pc.amount)
    })
    
    const processesVentas = datos.filter(dato => dato.tipe === "gain");
    processesVentas.forEach(pv =>{
        earnings+=parseInt(pv.amount)
    })
    document.getElementById("earnigs").textContent=earnings
    document.getElementById("bills").textContent=bills
    document.getElementById("total").textContent=earnings-bills


}

// ========== EVENTOS PRINCIPALES ==========
document.addEventListener("DOMContentLoaded", async function () {
    paintSidebar("balance")
    await countBalance()
    await paintProcesses(await getProcesses())
})



// ========== ADD PROCESS ==========


/* Event for modal voters to create a new process */ 
btnModalProcessCreate.addEventListener("click", async function () {
    modalProcessesCreate.style.display = 'block'
    await paintCategorys(document.getElementById("createCategoryProcess"))

})
/* Event for close the modal voters to create a new process */ 
formProcesses.btnCerrarModalCreate.addEventListener("click", () => {
    modalProcessesCreate.style.display = 'none'
})

/* Event for the form of create a new process*/ 
formProcesses.addEventListener("submit", async function (e) {
    e.preventDefault()


    const newProcess = {
        description: formProcesses.createDescriptionProcess.value,
        amount: formProcesses.createAmoutProcess.value,
        tipe: formProcesses.createTipProcess.value,
        categoryId: formProcesses.createCategoryProcess.value,
        date: formProcesses.createDateProcess.value,
    }

    await createNewProcess(newProcess)
})

/*function that communicates with the database to create the new process */
async function createNewProcess(newProcess) {
    try {
        const response = await fetch(endpointProcesses, {
            method: "POST",
            headers: { "content-type": "application/json" },
            body: JSON.stringify(newProcess)
        })

        if (response.ok) {
            alert("Process add")
            modalProcessesCreate.style.display = 'none'
            await paintProcesses(await getProcesses())
        }
    } catch (error) {
        console.error("Error al crear movimiento:", error)
    }
}






// ========== EDIT A PROCESS ==========


/* Event for close the modal voters to edit a process */ 
formEditarProcess.btnCerrarModal.addEventListener('click', () => {
    modalProcessesEdit.style.display = 'none'
})

/* Event for the form of edit a process*/ 
formEditarProcess.addEventListener("submit", async function (e) {
    e.preventDefault()

    const id = formEditarProcess.idProcess.value

    const updatedProcess = {
        id: formEditarProcess.idProcess.value,
        description: formEditarProcess.editDescriptionProcess.value,
        amount: formEditarProcess.editAmoutProcess.value,
        tipe: formEditarProcess.editTipProcess.value,
        categoryId: formEditarProcess.editCategoryProcess.value,
        date: formEditarProcess.editDateProcess.value,
    }

    await updateProcess(updatedProcess)
})
/*function that communicates with the database to edit a process */
async function updateProcess(updatedProcess) {
    try {
        const res = await fetch(`${endpointProcesses}/${updatedProcess.id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(updatedProcess)
        })

        modalProcessesEdit.style.display = 'none'
        await paintProcesses(await getProcesses())
    } catch (error) {
        console.error("Error Update Process:", error)
    }
}

// ====================


// ========== PAINT  CATEGORYS ==========

async function paintCategorys(selectElement) {
    try {
        const response = await fetch(endpointCategories)
        const data = await response.json()

        selectElement.innerHTML = ""

        if (data.length === 0) {
            selectElement.innerHTML = `
                <option disabled>No Categories, please register at least one</option>
            `
        }

        data.forEach(categoria => {
            selectElement.innerHTML += `
                <option value="${categoria.id}">${categoria.nameCategoria}</option>
            `
        })
    } catch (error) {
        console.error("Error loading categories:", error)
    }
}
// ====================




// ========== DELETE A PROCESS ==========

async function deleteOperation(id) {
    if (confirm("¿Estás seguro de eliminar este movimiento?")) {
        try {
            await fetch(`${endpointProcesses}/${id}`, { method: 'DELETE' })
            await paintProcesses(await getProcesses())
        } catch (error) {
            console.error('Error al eliminar el movimiento:', error)
        }
    }
}
// ====================



// ========== EVENTS A BOTONS ( EDIT AND DELETE) ==========

/*event to create events on buttons so they can create or edit a process*/
tbodyProcesses.addEventListener('click', async (e) => {
    const target = e.target
    const action = target.dataset.action

    if (action === 'delete') {
        const id = target.dataset.id
        await deleteOperation(id)
    } else if (action === 'edit') {
        const id = target.dataset.id

        try {
            const res = await fetch(`${endpointProcesses}/${id}`)
            const process = await res.json()

            formEditarProcess.idProcess.value = process.id
            formEditarProcess.editDescriptionProcess.value = process.description
            formEditarProcess.editAmoutProcess.value = process.amount
            formEditarProcess.editTipProcess.value = process.tipe
            formEditarProcess.editDateProcess.value = process.date
            await paintCategorys(document.getElementById("editCategoryProcess"))


            modalProcessesEdit.style.display = 'block'
        } catch (error) {
            console.error("Error loading process", error)
        }
    }
})
// ====================

// ========== PAINT  PROCESSES ==========
async function paintProcesses(processes) {

    try {
        tbodyProcesses.innerHTML = ""

        for (const process of processes) {
            console.log(process)
            let category;
            if(process.categoryId=="null" || process.categoryId==null){
                category="Dont Exist"
            }
            if(process.categoryId!=null){
            category=process.category.nameCategoria
            }
  
            tbodyProcesses.innerHTML += `
                <tr>
                    <td>${process.description}</td>
                    <td>${category}</td>
                    <td>${process.date}</td>
                    <td>${process.amount}</td>
                    <td>
                        <button class="btn-editar" data-action="edit" data-id="${process.id}"><i class="bi bi-pencil-square"></i> Edit</button>
                        <button class="btn-eliminar" data-action="delete" data-id="${process.id}"><i class="bi bi-trash-fill"></i>
 Delete</button>
                    </td>
                </tr>
            `
        }
    } catch (error) {
        console.error("Error al pintar movimientos:", error)
    }


}
// ========== GET PROCESSES IN THE DATA BASE ==========
async function getProcesses() {
    const response = await fetch(`${endpointProcesses}?_embed=category`)
    const data = await response.json()
    return data
}





