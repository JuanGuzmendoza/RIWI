import { paintSidebar } from './Components/sidebar'

const endPointCategorias = 'http://localhost:3000/categories';

const tableCategorias = document.getElementById('categoria_table');
const formCategorias = document.getElementById("formCategorias")
const formEditarCategoria = document.getElementById('formEditarCategoria');
const modalCategoriaEdit = document.getElementById('modal-editar');


// ==================== INICIO ====================
document.addEventListener('DOMContentLoaded', async function () {
    paintSidebar("categorias")
    await paintTableCategorias();
});


// ==================== PINTAR TABLA ====================
async function paintTableCategorias() {
    tableCategorias.innerHTML = ""
    try {
        const categorias = await obtainCategorias();


        for (let categoria of categorias) {
            tableCategorias.innerHTML += `
                <tr>
                    <td>${categoria.id}</td>
                    <td>${categoria.nameCategoria}</td>
                    <td>
                        <button class="btn btn-danger btn-sm" data-action="eliminar" data-id="${categoria.id}">Eliminar</button>
                        <button class="btn btn-info btn-sm" data-action="editar" data-id="${categoria.id}" data-nombre="${categoria.nameCategoria}">Editar</button>
                    </td>
                </tr>
            `;
        }
    } catch (error) {
        console.error("Error al pintar la tabla:", error);
    }
}


// ==================== OBTENER CATEGORÍAS ====================
async function obtainCategorias() {
    try {
        const res = await fetch(endPointCategorias);
        return await res.json();
    } catch (error) {
        console.error("Error al obtener categorías:", error);
 
    }
}


// ==================== EVENTOS DE BOTONES DE LA TABLA ====================
tableCategorias.addEventListener('click', async (e) => {
    const target = e.target;
    const action = target.dataset.action;

    if (action === 'eliminar') {
        const id = target.dataset.id;
        await deleteCategoria(id);
    } else if (action === 'editar') {
        const id = target.dataset.id;
        const nombre = target.dataset.nombre;

        formEditarCategoria.idCategoria.value = id;
        formEditarCategoria.newNameCategoria.value = nombre;
        modalCategoriaEdit.style.display = 'block';
    }
});


// ==================== CERRAR MODAL ====================
formEditarCategoria.btnCerrarModal.addEventListener('click', () => {
    modalCategoriaEdit.style.display = 'none';
});


// ==================== ACTUALIZAR CATEGORÍA ====================
formEditarCategoria.addEventListener('submit', async function (e) {
    e.preventDefault();

    const id = formEditarCategoria.idCategoria.value;
    const nombre = formEditarCategoria.newNameCategoria.value;

    try {
        await fetch(`${endPointCategorias}/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ id: id, nameCategoria: nombre })
        });

        modalCategoriaEdit.style.display = 'none';
        await paintTableCategorias();

    } catch (error) {
        console.error('Error al actualizar categoría:', error);
    }
});


// ==================== AÑADIR CATEGORÍA ====================
formCategorias.addEventListener("submit", async function (event) {
    event.preventDefault();
    await addCategorias();
});

async function addCategorias() {
    const nameCategoria = formCategorias.categoriaName.value;

    try {
        await fetch(endPointCategorias, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ nameCategoria })
        });

        formCategorias.reset();
        await paintTableCategorias();

    } catch (error) {
        console.error("Error al añadir categoría:", error);
    }
}


// ==================== ELIMINAR CATEGORÍA ====================
async function deleteCategoria(id) {
    if (confirm("¿Estás seguro de eliminar esta categoría?")) {
        try {
            await fetch(`${endPointCategorias}/${id}`, {
                method: 'DELETE',
            });
            await paintTableCategorias();
        } catch (error) {
            console.error('Error al eliminar categoría:', error);
        }
    }
}
