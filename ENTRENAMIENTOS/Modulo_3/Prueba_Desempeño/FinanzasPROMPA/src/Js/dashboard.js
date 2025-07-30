import { paintSidebar } from './Components/sidebar'


document.addEventListener("DOMContentLoaded",async () => {
    paintSidebar("reportes")
    iniciarReportes()
})

const endpointMovimientos = "http://localhost:3000/movimientos"

async function cantidadVentasCompras() {

    const datos = await traerMovimientos();

    const movimientosCompras = datos.filter(dato => dato.tipo === "compra");
    const movimientosVentas = datos.filter(dato => dato.tipo === "venta");
    // Mostrar cantidad total
    document.getElementById("infoCompras").textContent = `Total: ${movimientosCompras.length}`;
    document.getElementById("infoVentas").textContent = `Total: ${movimientosVentas.length}`;

    // Mostrar categoría más repetida
    document.getElementById("cateMayorCompras").textContent = obtenerCategoriaMasRepetida(movimientosCompras);
    document.getElementById("cateMayorVentas").textContent = obtenerCategoriaMasRepetida(movimientosVentas);

    // Mes con más compras y ventas
    const comprasMes = agruparPorMes(movimientosCompras);
    const ventasMes = agruparPorMes(movimientosVentas);
    document.getElementById("mesMayorCompras").textContent=comprasMes
    document.getElementById("mesMayorVentas").textContent=ventasMes
}

    // 1. CATEGORÍA MÁS REPETIDA

    function obtenerCategoriaMasRepetida(movimientos) {
        const conteo = {};
        movimientos.forEach(mov => {
            const nombreCategoria = mov.category?.nameCategoria || mov.categoryId;
            if (nombreCategoria) {
                conteo[nombreCategoria] = (conteo[nombreCategoria] || 0) + 1;
            }
        });

        let max = 0;
        let masRepetida = "Ninguna";
        for (const cat in conteo) {
            if (conteo[cat] > max) {
                max = conteo[cat];
                masRepetida = cat;
            }
        }

        return masRepetida;
    }
    // 2. AGRUPAR POR MES
function agruparPorMes(movimientos) {
    const conteoMeses = {};

    movimientos.forEach(mov => {
        const fecha = new Date(mov.fecha);
        if (isNaN(fecha)) return; // Ignorar fechas inválidas

        const mes = fecha.toLocaleString('default', { month: 'long' }); // Solo mes
        conteoMeses[mes] = (conteoMeses[mes] || 0) + 1;
    });

    let mesMayor = "Ninguno";
    let max = 0;

    for (const mes in conteoMeses) {
        if (conteoMeses[mes] > max) {
            max = conteoMeses[mes];
            mesMayor = mes;
        }
    }

    return mesMayor;
}

async function iniciarReportes() {
    
    await cantidadVentasCompras()
}
async function traerMovimientos() {
    const response = await fetch(`${endpointMovimientos}?_embed=category`)
    const data = await response.json()
    return data
}