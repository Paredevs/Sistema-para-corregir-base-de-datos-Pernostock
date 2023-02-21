## Funcionalidad

Los scripts se encargan de leer archivos de texto plano (```.csv```) y realizar una serie de funciones para identificar los fallos en la base de datos. Cuando finaliza, se genera un archivo de texto plano en formato ```.csv``` en  el directorio ```./resultados/``` 

 En total las bases de datos son 5 archivos, las cuales 4 corresponden a las sucursales y uno a la base de datos Maestra


 ## Fallos en las bases de datos

A continuacion se mecionan los fallos que se encontraron en las 5 bases de datos: 

 - Duplicados exactos
 - Descripciones mal escritas 
 - Correccion de descripciones que pertenecen a otros productos
 - Productos que no tienen inventario ni movimiento 
 - Busqueda de productos (codigos) en las 4 sucursales que no se encuentren en la base de datos Maestra
 - Errores en las fechas de venta/compra de los productos

> Nota: La base de datos maestra contiene todos los productos, las sucursales se generan atraves de esta, no pueden haber productos en sucursales que no se encuentren en la maestra

## Caracteristicas

Actulmente el programa no cuanta con un GUI (interfaz grafica),todo funciona a traves de la terminal

## Requisitos

Para la funcionalidad correcta, el script exige que las 5 bases de datos se encuentren en la ubicacion ```./database/ ``` las cuales deben tener los siguientes nombres:

 - Base de datos Maestra: ```Maestra.csv```
 - Bodega central:```Bodega central.csv```
 - Casa matriz:```Casa matriz.csv```
 - La Serena: - ```La Serena.csv```
 - Barrio industrial - ```Barrio industrial.csv```

> Nota: Todas las bases de datos son requeridas para que el script funcione correctamente ademas de su nombre, si una falta el programa lo informa.

## Scripts

A continuacion estan los archivos ```.py``` 