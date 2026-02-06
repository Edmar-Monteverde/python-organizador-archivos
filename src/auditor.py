from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass(frozen=True)
class ArchivoInfo:
    nombre: str
    extension: str
    tamano_bytes: int
    ruta: str



def escanear_archivos(carpeta: Path) -> List[ArchivoInfo]: ## Función para escanear archivos en una carpeta dada y devolver una lista de objetos ArchivoInfo
  
    if not carpeta.exists(): ## Verifica si la ruta proporcionada existe
        raise ValueError(f"La ruta {carpeta} no existe.")
    if not carpeta.is_dir(): ## Verifica si la ruta proporcionada es un directorio válido
        raise ValueError(f"La ruta {carpeta} no es un directorio válido.")
   
  
    archivos_info =[]
    for  item in carpeta.iterdir(): ## Itera sobre cada elemento en la carpeta utilizando iterdir()

        if item.is_file():## Verifica si el elemento es un  un archivo
            archivos_info.append(ArchivoInfo( ## Crea un objeto ArchivoInfo con la información del archivo y lo agrega a la lista archivos_info
                nombre=item.name,
                extension=item.suffix.lower(),
                tamano_bytes=item.stat().st_size,
                ruta=str(item.resolve())
            ))

    return archivos_info