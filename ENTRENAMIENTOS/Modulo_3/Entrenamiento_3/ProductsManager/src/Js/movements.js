import { paintSidebar } from './Components/sidebar'

// ========== ENDPOINTS ==========
const endpointCategories = "http://localhost:3000/categories"
const endpointMovimientos = "http://localhost:3000/movimientos"

// ========== ELEMENTOS DEL DOM ==========
const formMovimientos = document.getElementById("form-movimiento")
const tbodyMovimientos = document.getElementById("tbody-movimientos")
const formEditarMovimiento = document.getElementById("formEditarMovimiento")
const modalMovimientosEdit = document.getElementById("modal-editar")
const selectCategorias = formMovimientos.categoria

// ========== EVENTOS PRINCIPALES ==========
document.addEventListener("DOMContentLoaded", function () {
    paintSidebar("movimientos")
    pintarCategorias(selectCategorias)
    pintarMovimientos()
})



// ========== CREAR UN MOVIMIENTO ==========

formMovimientos.addEventListener("submit", function (event) {
    event.preventDefault()

    const newMovimiento = {
        tipo: formMovimientos.tipoMovimiento.value,
        descripcion: formMovimientos.descripcionMovimiento.value,
        cantidad:formMovimientos.cantProdMovimiento.value,
        importe: formMovimientos.importeMovimiento.value,
        fecha: formMovimientos.fechaMovimiento.value,
        categoryId: formMovimientos.categoria.value,
    }

    crearUnNuevoMovimiento(newMovimiento)
    formMovimientos.reset()
})

async function crearUnNuevoMovimiento(newMovimiento) {
    try {
        const response = await fetch(endpointMovimientos, {
            method: "POST",
            headers: { "content-type": "application/json" },
            body: JSON.stringify(newMovimiento)
        })

        if (response.ok) {
            alert("movimiento guardado con exito")
            await pintarMovimientos()
        }
    } catch (error) {
        console.error("Error al crear movimiento:", error)
    }
}
// = = = = = = = = = = = = = = = = = = = = =  


// ========== ACTUALIZAR UN MOVIMIENTO ==========

formEditarMovimiento.addEventListener("submit", async function (e) {
    e.preventDefault()

    const id = formEditarMovimiento.idMovimiento.value

    const movimientoActualizado = {
        id: formEditarMovimiento.idMovimiento.value,
        tipo: formEditarMovimiento.editTipoMovimiento.value,
        descripcion: formEditarMovimiento.editDescripcionMovimiento.value,
        importe: formEditarMovimiento.editImporteMovimiento.value,
        cantidad: formEditarMovimiento.editCantidadMovimiento.value,
        fecha: formEditarMovimiento.editFechaMovimiento.value,
        categoryId: formEditarMovimiento.editCategoriaMovimiento.value,
    }

    await updateMovimiento(movimientoActualizado)
})

async function updateMovimiento(movimientoActualizado) {
    try {
        const res = await fetch(`${endpointMovimientos}/${movimientoActualizado.id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(movimientoActualizado)
        })

        modalMovimientosEdit.style.display = 'none'
        await pintarMovimientos()
    } catch (error) {
        console.error("Error al actualizar movimiento:", error)
    }
}
formEditarMovimiento.btnCerrarModal.addEventListener('click', () => {
    modalMovimientosEdit.style.display = 'none'
})

// ========== ACCIONES PARA ELIMIAR Y ACTUALIZAR ==========
tbodyMovimientos.addEventListener('click', async (e) => {
    const target = e.target
    const action = target.dataset.action

    if (action === 'eliminar') {
        const id = target.dataset.id
        await deleteMovimiento(id)
    } else if (action === 'editar') {
        const id = target.dataset.id

        try {
            const res = await fetch(`${endpointMovimientos}/${id}`)
            const movimiento = await res.json()

            formEditarMovimiento.idMovimiento.value = movimiento.id
            formEditarMovimiento.editTipoMovimiento.value = movimiento.tipo
            formEditarMovimiento.editDescripcionMovimiento.value = movimiento.descripcion
            formEditarMovimiento.editImporteMovimiento.value = movimiento.importe
            formEditarMovimiento.editCantidadMovimiento.value = movimiento.cantidad
            formEditarMovimiento.editFechaMovimiento.value = movimiento.fecha
            
            await pintarCategorias(document.getElementById("editCategoriaMovimiento"))

            modalMovimientosEdit.style.display = 'block'
        } catch (error) {
            console.error("Error al cargar movimiento:", error)
        }
    }
})

// = = = = = = = = = = = = = = = = = = = = =  

// ========== FUNCIONES CRUD ==========


async function deleteMovimiento(id) {
    if (confirm("¿Estás seguro de eliminar este movimiento?")) {
        try {
            await fetch(`${endpointMovimientos}/${id}`, { method: 'DELETE' })
            await pintarMovimientos()
        } catch (error) {
            console.error('Error al eliminar el movimiento:', error)
        }
    }
}

// ========== FUNCIONES DE PINTADO ==========
async function pintarMovimientos() {
    try {
        const movimientos = await traerMovimientos()
        tbodyMovimientos.innerHTML = ""

        for (const movimiento of movimientos) {
            tbodyMovimientos.innerHTML += `
                <tr>
                    <td>${movimiento.tipo}</td>
                    <td>${movimiento.descripcion}</td>
                    <td>${movimiento.importe}</td>
                    <td>${movimiento.cantidad}</td>
                    <td>${movimiento.fecha}</td>
                    <td>${movimiento.category.nameCategoria}</td>
                    <td>
                        <button class="btn-editar" data-action="editar" data-id="${movimiento.id}">Editar</button>
                        <button class="btn-eliminar" data-action="eliminar" data-id="${movimiento.id}">Eliminar</button>
                    </td>
                </tr>
            `
        }
    } catch (error) {
        console.error("Error al pintar movimientos:", error)
    }
}

async function pintarCategorias(selectElement) {
    try {
        const response = await fetch(endpointCategories)
        const data = await response.json()

        selectElement.innerHTML = ""

        if (data.length === 0) {
            selectElement.innerHTML = `
                <option disabled>Sin Categorias, por favor registre al menos una</option>
            `
        }

        data.forEach(categoria => {
            selectElement.innerHTML += `
                <option value="${categoria.id}">${categoria.nameCategoria}</option>
            `
        })
    } catch (error) {
        console.error("Error al cargar categorías:", error)
    }
}


// ========== FUNCIONES DE SERVICIO ==========
async function traerMovimientos() {
    const response = await fetch(`${endpointMovimientos}?_embed=category`)
    const data = await response.json()
    return data
}
