import argparse
from pathlib import Path
import csv
from typing import List
from auditor import ArchivoInfo, escanear_archivos

def leer_argumentos() -> argparse.Namespace:

    parser=argparse.ArgumentParser(description="Escanea una carpeta y exporta un reporte CSV con información de los archivos.")

    parser.add_argument(
        "--path",
         default=".",
        help="Ruta de la carpeta a escanear (por defecto: carpeta actual")
    
    parser.add_argument(
        "--output",
        default="output/reporte.csv",
        help="Ruta del archivo CSV de salida (por defecto: output/reporte.csv)"
    )

    parser.add_argument(
        "--no_csv",
        action="store_true",
        help="Si se especifica, no se exportará el reporte a CSV")
    
    parser.add_argument( 
        "--limite",
        type=int,
        default=10, 
        help="Número máximo de archivos a mostrar en la consola (por defecto: 10)")
    
    return parser.parse_args()

                       






def exportar_a_csv(archivos: list[ArchivoInfo], ruta_salida: str = "output/reporte.csv") -> None:
    ruta=Path(ruta_salida)
    ruta.parent.mkdir(parents=True, exist_ok=True) ## Crea el directorio de salida si no existe

    with ruta.open("w", newline="", encoding="utf-8") as file: ## Abre el archivo CSV para escritura
        writer=csv.writer(file)
        writer.writerow(["Nombre", "Extensión", "Tamaño (bytes)", "Ruta"]) ## Escribe la fila de encabezado

        for a in archivos: ## Escribe cada objeto ArchivoInfo como una fila en el CSV
            writer.writerow([a.nombre, a.extension, a.tamano_bytes, a.ruta])

 
def main() -> None:

    args=leer_argumentos()
    carpeta = Path(args.path)  # por ahora analiza la carpeta actual
    archivos = escanear_archivos(carpeta)

    print(f"\n📁 Carpeta: {carpeta.resolve()}")
    print(f"📄 Archivos encontrados: {len(archivos)}")

    print(f"\n--- MOSTRANDO {min(args.limite, len(archivos))} ---")
    print(f"Archivos encontrados: {len(archivos)}")
    for a in archivos[:args.limite]: ## Muestra en la consola los primeros archivos encontrados, limitados por el argumento --limite
        print(f"- {a.nombre} | {a.extension} | {a.tamano_bytes} bytes") ## Tomamos en cuenta que a es un objeto ArchivoInfo 
        # y por eso accedemos a sus atributos nombre, extension y tamano_bytes

    if not args.no_csv: ## Si no se especificó la opción --no-csv, exporta el reporte a CSV
            print(f"\nExportando reporte a CSV...")
    
        
    exportar_a_csv(archivos, args.output)
    print(f"Reporte exportado a {args.output}")




if __name__ == "__main__":
    main()




