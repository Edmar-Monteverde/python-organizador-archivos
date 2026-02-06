from pathlib import Path
import csv
from auditor import ArchivoInfo
from auditor import escanear_archivos

def exportar_a_csv(archivos: list[ArchivoInfo], ruta_salida: str = "output/reporte.csv") -> None:
    ruta=Path(ruta_salida)
    ruta.parent.mkdir(parents=True, exist_ok=True) ## Crea el directorio de salida si no existe

    with ruta.open("w", newline="", encoding="utf-8") as file: ## Abre el archivo CSV para escritura
        writer=csv.writer(file)
        writer.writerow(["Nombre", "Extensión", "Tamaño (bytes)", "Ruta"]) ## Escribe la fila de encabezado

        for a in archivos: ## Escribe cada objeto ArchivoInfo como una fila en el CSV
            writer.writerow([a.nombre, a.extension, a.tamano_bytes, a.ruta])

 
def main() -> None:
    carpeta = Path(".")  # por ahora analiza la carpeta actual
    archivos = escanear_archivos(carpeta)

    print(f"Archivos encontrados: {len(archivos)}")
    for a in archivos[:10]:
        print(f"- {a.nombre} | {a.extension} | {a.tamano_bytes} bytes") ## Tomamos en cuenta que a es un objeto ArchivoInfo 
        # y por eso accedemos a sus atributos nombre, extension y tamano_bytes

    exportar_a_csv(archivos)
    print("Reporte exportado a output/reporte.csv")




if __name__ == "__main__":
    main()




