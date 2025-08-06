select * from clientes ;
select * from compras ;
/* 1 */


/* 2 */
select nombre,apellido,edad from clientes where edad>=20 and edad <=30;

/* 3 */
select * from compras where metodo_pago="Tarjeta";

/* 4 */
select producto from compras where producto like '%Celular%';

/* 5 */
select * from clientes where email is null;

/* 6 */
select * from clientes order by created_at limit 5;

/* 7 */
select distinct ciudad from clientes;

/* 8 */
select * from compras where calificacion_compra =5;

/* 9 */
SELECT producto,fecha_compra from compras where YEAR(fecha_compra)=2025 ;

/* 10 */
select count(*) as cant_metodos_pago_PSE from compras where metodo_pago ="PSE" ;

/* 11 */
SELECT ciudad, COUNT(*) AS cantidad_clientes
FROM clientes
GROUP BY ciudad;

/* 12 */
select metodo_pago , SUM(cantidad*precio_unitario) as recaudo
from compras 
group by metodo_pago;

/* 13 */
select genero , AVG(edad) as promedio_edad
from clientes
group by genero;

/* 14 */
SELECT categoria, COUNT(*) AS total_productos
FROM compras
GROUP BY categoria
HAVING COUNT(*) > 2;

/* 15 */ 
SELECT producto, MAX(precio_unitario) AS precio_unitario
FROM compras;

/* 16 */
SELECT producto, SUM(cantidad) AS total_unidades, COUNT(*) AS veces_comprado
FROM compras
GROUP BY producto;

/* 17 */
SELECT 
  marca,
  AVG(calificacion_compra) AS promedio_calificacion
FROM compras
GROUP BY marca
HAVING AVG(calificacion_compra) > 4;

/* 18 */
select categoria , sum(cantidad*precio_unitario) as total_gastado
from compras
group by categoria;

/* 19 */
SELECT 
  ciudad, 
  COUNT(*) AS total_activos
FROM clientes
WHERE activo = '1'
GROUP BY ciudad
ORDER BY total_activos DESC
LIMIT 3;

/* 20 */
SELECT 
  clientes.nombre, 
  COUNT(*) AS total_compras
FROM compras
JOIN clientes ON compras.cliente_id = clientes.id
WHERE clientes.edad > 30
GROUP BY clientes.id, clientes.nombre;


/* 21 */
SELECT 
  producto,
  COUNT(DISTINCT cliente_id) AS cantidad_personas
FROM compras
GROUP BY producto
HAVING COUNT(DISTINCT cliente_id) > 3;

/* 22 */
SELECT nombre, referido_por
FROM clientes
WHERE referido_por IS NOT NULL;




