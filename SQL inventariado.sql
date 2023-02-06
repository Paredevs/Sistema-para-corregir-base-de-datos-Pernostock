-- SELECT
--         Maestra.Codigo, 
--         Maestra.Descripcion
        
-- FROM 
--         Maestra,
--         [Sugerencias Compras Casa Matriz],
--         [Sugerencias Compras Bodega central],
--         [Sugerencias Compras La Serena],
--         [Sugerencias Compras Barrio Industrial]  
         
-- WHERE 
-- ((([Sugerencias Compras Casa Matriz].[Descripcion producto]) In (SELECT [Sugerencias Compras Casa Matriz].[Descripcion producto] FROM [Sugerencias Compras Casa Matriz] As Tmp GROUP BY [Sugerencias Compras Casa Matriz].[Descripcion producto] HAVING COUNT([Sugerencias Compras Casa Matriz].[Descripcion producto]) >1  ))) OR 
-- ((([Sugerencias Compras Bodega central].[Descripcion producto]) In (SELECT [Sugerencias Compras Bodega central].[Descripcion producto] FROM [Sugerencias Compras Bodega central] As Tmp GROUP BY [Sugerencias Compras Bodega central].[Descripcion producto] HAVING COUNT([Sugerencias Compras Bodega central].[Descripcion producto]) >1  ))) OR
-- ((([Sugerencias Compras La Serena].[Descripcion producto]) In (SELECT[Sugerencias Compras La Serena].[Descripcion producto] FROM [Sugerencias Compras La Serena] As Tmp GROUP BY [Sugerencias Compras La Serena].[Descripcion producto] HAVING COUNT([Sugerencias Compras La Serena].[Descripcion producto]) >1  ))) OR
-- ((([Sugerencias Compras Barrio Industrial].[Descripcion producto]) In (SELECT [Sugerencias Compras Barrio Industrial].[Descripcion producto]FROM [Sugerencias Compras Barrio Industrial] As Tmp GROUP BY [Sugerencias Compras Barrio Industrial].[Descripcion producto] HAVING COUNT([Sugerencias Compras Barrio Industrial].[Descripcion producto]) >1  ))) 

-- AND (
--     Maestra.Codigo =[Sugerencias Compras Barrio Industrial].Codigo OR 
--     Maestra.Codigo = [Sugerencias Compras Bodega central].Codigo OR 
--     Maestra.Codigo = [Sugerencias Compras La Serena ].Codigo OR 
--     Maestra.Codigo = [Sugerencias Compras Casa Matriz].Codigo )
-- ORDER BY Maestra.[Descripcion];


 SELECT
         Maestra.Codigo, 
         Maestra.Descripcion      
 FROM 
         Maestra,
         [Sugerencias Compras Casa Matriz],
         [Sugerencias Compras Bodega central]
                
 WHERE 
 (   ((([Sugerencias Compras Casa Matriz].[Descripcion producto]) 
    In (SELECT [Sugerencias Compras Casa Matriz].[Descripcion producto] 
        FROM [Sugerencias Compras Casa Matriz] As Tmp 
            GROUP BY [Sugerencias Compras Casa Matriz].[Descripcion producto] 
                HAVING COUNT([Sugerencias Compras Casa Matriz].[Descripcion producto]) >1  )))  
                    AND    [Sugerencias Compras Casa Matriz].Codigo = Maestra.Codigo   ) OR 
 
 (     ((([Sugerencias Compras Bodega central].[Descripcion producto])  
    In (SELECT [Sugerencias Compras Bodega central].[Descripcion producto] 
        FROM [Sugerencias Compras Bodega central] As Tmp 
            GROUP BY [Sugerencias Compras Bodega central].[Descripcion producto] 
                HAVING COUNT([Sugerencias Compras Bodega central].[Descripcion producto]) >1  )))    
                    AND[Sugerencias Compras Bodega central].Codigo = Maestra.Codigo )
   

 ORDER BY Maestra.[Descripcion];



--SIN MAESTRA


 SELECT
       [Sugerencias Compras Casa Matriz].[Descripcion producto]
    
 FROM 
    
         [Sugerencias Compras Casa Matriz],
         [Sugerencias Compras Bodega central]
                
 WHERE 
 (   ((([Sugerencias Compras Casa Matriz].[Descripcion producto]) 
    In (SELECT [Sugerencias Compras Casa Matriz].[Descripcion producto] 
        FROM [Sugerencias Compras Casa Matriz] As Tmp 
            GROUP BY [Sugerencias Compras Casa Matriz].[Descripcion producto] 
                HAVING COUNT([Sugerencias Compras Casa Matriz].[Descripcion producto]) >1  )))  
                     ) OR
 
 (     ((([Sugerencias Compras Bodega central].[Descripcion producto])  
    In (SELECT [Sugerencias Compras Bodega central].[Descripcion producto] 
        FROM [Sugerencias Compras Bodega central] As Tmp 
            GROUP BY [Sugerencias Compras Bodega central].[Descripcion producto] 
                HAVING COUNT([Sugerencias Compras Bodega central].[Descripcion producto]) >1  )))    
                    )
   

 ORDER BY [Sugerencias Compras Casa Matriz].[Descripcion producto] ASC;










--COMPARACION DE INVENTARIADO CON SUGERENCIAS DE COMPRAS

--INV WORTH
SELECT 
        [Sugerencias Compras Casa Matriz].Codigo
FROM 
        [Sugerencias Compras Casa Matriz], Maestra

WHERE 
((([Descripcion producto]) 
    In (SELECT [Descripcion producto] 
        FROM [Sugerencias Compras Casa Matriz] As Tmp 
            GROUP BY [Descripcion producto] 
                HAVING COUNT([Descripcion producto]) >1  ))) AND Maestra.Codigo =[Sugerencias Compras Casa Matriz].Codigo
ORDER BY [Descripcion producto];

--TEST
 SELECT
        [Sugerencias Compras Casa Matriz].Codigo
 FROM 
        [Sugerencias Compras Casa Matriz],
        Maestra 
 WHERE 
((([Descripcion producto]) 
    In (SELECT [Sugerencias Compras Casa Matriz].[Descripcion producto] 
        FROM [Sugerencias Compras Casa Matriz] As Tmp 
            GROUP BY [Sugerencias Compras Casa Matriz].[Descripcion producto] 
                HAVING COUNT([Sugerencias Compras Casa Matriz].[Descripcion producto]) >1  )))  AND Maestra.Codigo =[Sugerencias Compras Casa Matriz].Codigo
 

 ORDER BY [Descripcion producto];