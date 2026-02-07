
import csv
from typing import List
from auditor import ArchivoInfo, escanear_archivos
from formatear_tamano import formatear_bytes
from pathlib import Path


def exportar_a_csv(archivos: list[ArchivoInfo], ruta_salida: str = "output/reporte.csv") -> None:
    ruta=Path(ruta_salida)
    ruta.parent.mkdir(parents=True, exist_ok=True) ## Crea el directorio de salida si no existe

    with ruta.open("w", newline="", encoding="utf-8") as file: ## Abre el archivo CSV para escritura
        writer=csv.writer(file)
        writer.writerow(["Nombre", "Extensión", "Tamaño", "Ruta"]) ## Escribe la fila de encabezado

        for a in archivos: ## Escribe cada objeto ArchivoInfo como una fila en el CSV
            writer.writerow([a.nombre, a.extension, formatear_bytes(a.tamano_bytes), a.ruta])