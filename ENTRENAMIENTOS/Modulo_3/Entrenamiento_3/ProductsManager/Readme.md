# Aplicativo de Gestión de Movimientos (Compras y Ventas)

## Descripción

Este proyecto es una **aplicación web de gestión de movimientos**, diseñada para llevar el control de compras y ventas de productos.

El sistema cuenta con tres vistas principales:

1. **Gestión de Categorías (CRUD)**  
   Permite crear, leer, actualizar y eliminar categorías de productos. Aquí puedes:
   - Agregar nuevas categorías.
   - Editar nombres de categorías existentes.
   - Visualizar la lista completa de categorías.
   - Eliminar categorías que ya no sean necesarias.

2. **Gestión de Movimientos (CRUD)**  
   En esta vista se gestionan los movimientos de productos, que pueden ser compras o ventas. Las funcionalidades incluyen:
   - Agregar nuevos movimientos especificando tipo (compra/venta), categoría, importe y fecha.
   - Editar movimientos existentes.
   - Visualizar y filtrar movimientos.
   - Eliminar movimientos si es necesario.

3. **Dashboard de Reportes (Vista inicial tras login)**  
   Al iniciar sesión, el usuario accede al dashboard principal donde se presentan reportes analíticos basados en los movimientos registrados:
   - Cantidad total de compras y ventas.
   - Categoría con mayor número de compras y ventas.
   - Mes con más compras y ventas.
   - Visualización clara y ordenada mediante tarjetas informativas.

---

## Tecnologías utilizadas

- JavaScript 
- HTML5 y CSS3 
- [JSON Server](https://github.com/typicode/json-server) para simulación de backend REST API
- Fetch API para consumo de datos
- [Bootstrap Icons](https://icons.getbootstrap.com/) para iconografía (opcional)

---

## Instalación y ejecución

Sigue estos pasos para levantar el proyecto localmente:

### 1. Clonar repositorio

```bash
git clone <url-del-repositorio>
cd <nombre-del-proyecto>
