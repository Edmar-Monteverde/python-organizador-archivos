
from __future__ import annotations


def formatear_bytes(num_bytes: int) ->str: 
    ## Convierte un número de bytes a una cadena legible con unidades (KB, MB, GB, etc.)
    unidades = ["B", "KB", "MB", "GB","TB"]
    valor= float(num_bytes)
    indice=0
    while valor >= 1024 and indice < len(unidades) - 1:

        ## confirmamos los dos casos, 1) valor es mayor o igual a 1024, lo que indica que podemos convertir a la siguiente unidad, 
        # y 2) indice es menor que la longitud de la lista de unidades menos uno, lo que asegura que no intentemos acceder a una unidad que no existe en la lista.
        valor /= 1024 ## Divide el valor por 1024 para convertirlo a la siguiente unidad
        indice += 1 ## Incrementa el índice para pasar a la siguiente unidad
    if indice ==0:
        return f"{num_bytes} {unidades[indice]}" ## Si el índice es 0, devuelve el número original de bytes con la unidad "B"
    
    
    return f"{valor:.2f} {unidades[indice]}" 
