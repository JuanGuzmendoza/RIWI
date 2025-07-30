import { paintSidebar } from './Components/sidebar'

const endPointCategorias = 'http://localhost:3000/categories';

const tableCategorys = document.getElementById('categoria_table');
const formCategorys = document.getElementById("formCategorys")
const formEditarCategorys = document.getElementById('formEditarCategorys');
const modalCategorysEdit = document.getElementById('modal-editar');


// ==================== START ====================
document.addEventListener('DOMContentLoaded', async function () {
    paintSidebar("categorys")
    await painttableCategorys();
});


// ==================== PAINT CATEGORYES ====================
async function painttableCategorys() {
    tableCategorys.innerHTML = ""
    try {
        const categorias = await obtainCategorias();


        for (let categoria of categorias) {
            tableCategorys.innerHTML += `
                <tr>
                    <td>${categoria.id}</td>
                    <td>${categoria.nameCategoria}</td>
                    <td>
                        <button class="btn btn-danger btn-sm" data-action="delete" data-id="${categoria.id}"><i class="bi bi-trash-fill"></i> Delete</button>
                        <button class="btn btn-info btn-sm" data-action="edit" data-id="${categoria.id}" data-nombre="${categoria.nameCategoria}"><i class="bi bi-pencil-square"></i>  Edit</button>
                    </td>
                </tr>
            `;
        }
    } catch (error) {
        console.error("Error painting table:", error);
    }
}


// ==================== GET CATEGORYS ====================
async function obtainCategorias() {
    try {
        const res = await fetch(endPointCategorias);
        return await res.json();
    } catch (error) {
        console.error("Error getting category:", error);
 
    }
}


// ==================== EVENTS OF BTN IN THE TABLE ====================
tableCategorys.addEventListener('click', async (e) => {
    const target = e.target;
    const action = target.dataset.action;

    if (action === 'delete') {
        const id = target.dataset.id;
        await deleteCategoria(id);
    } else if (action === 'edit') {
        const id = target.dataset.id;
        const nombre = target.dataset.nombre;

        formEditarCategorys.idCategoria.value = id;
        formEditarCategorys.newNameCategoria.value = nombre;
        modalCategorysEdit.style.display = 'block';
    }
});


// ==================== CLOSE MODAL ====================
formEditarCategorys.btnCerrarModal.addEventListener('click', () => {
    modalCategorysEdit.style.display = 'none';
});


// ==================== EDIT CATEGORY ====================
formEditarCategorys.addEventListener('submit', async function (e) {
    e.preventDefault();

    const id = formEditarCategorys.idCategoria.value;
    const nombre = formEditarCategorys.newNameCategoria.value;

    try {
        await fetch(`${endPointCategorias}/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ id: id, nameCategoria: nombre })
        });

        modalCategorysEdit.style.display = 'none';
        await painttableCategorys();

    } catch (error) {
        console.error('Error updating category:', error);
    }
});


// ==================== ADD CATEGORY ====================
formCategorys.addEventListener("submit", async function (event) {
    event.preventDefault();
    await addCategorias();
});

async function addCategorias() {
    const nameCategoria = formCategorys.categoriaName.value;

    try {
        await fetch(endPointCategorias, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ nameCategoria })
        });

        formCategorys.reset();
        await painttableCategorys();

    } catch (error) {
        console.error("Error adding category:", error);
    }
}


// ==================== DELETE CATEOGRY ====================
async function deleteCategoria(id) {
    if (confirm("¿Are you sure you want to delete this category??")) {
        try {
            await fetch(`${endPointCategorias}/${id}`, {
                method: 'DELETE',
            });
            await painttableCategorys();
        } catch (error) {
            console.error('Error deleting category:', error);
        }
    }
}
