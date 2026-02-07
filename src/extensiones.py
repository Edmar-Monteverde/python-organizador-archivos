from __future__ import annotations
from typing import List,Dict,Tuple
from collections import defaultdict
from auditor import ArchivoInfo



def resumen_por_extension(archivos: List[ArchivoInfo]) -> Dict[str, Tuple[int, int]]:
        resumen: Dict[str, Tuple[int, int]]={}  # Diccionario para almacenar el resumen por extensión
        acumulador = defaultdict(lambda: [0, 0])  # Acumulador para contar cantidad y tamaño por extensión

        for a in archivos:  # Itera sobre cada archivo encontrado
            ext=a.extension if a.extension else '(sin extensión)'  # Si no tiene extensión, se etiqueta como '(sin extensión)'
            acumulador[ext][0] += 1  # Incrementa el conteo de archivos para esta extensión
            acumulador[ext][1] += a.tamano_bytes  # Acumula el tamaño total de archivos para esta extensión

        for ext,(cantidad, total_bytes) in acumulador.items():  # Itera sobre el acumulador para construir el resumen final
                resumen[ext]=(cantidad, total_bytes)  # Almacena la cantidad y el tamaño total en el resumen

        return resumen