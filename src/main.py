import argparse
from pathlib import Path
import csv
from typing import List,Dict,Tuple
from auditor import ArchivoInfo, escanear_archivos
from collections import defaultdict
from formatear_tamano import formatear_bytes

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
    
    parser.add_argument(
        "--human",
        action="store_true",
        help="Muestra el tamaño de los archivos en formato legible (KB, MB, GB, etc.)")
    
    return parser.parse_args()

                       






def exportar_a_csv(archivos: list[ArchivoInfo], ruta_salida: str = "output/reporte.csv") -> None:
    ruta=Path(ruta_salida)
    ruta.parent.mkdir(parents=True, exist_ok=True) ## Crea el directorio de salida si no existe

    with ruta.open("w", newline="", encoding="utf-8") as file: ## Abre el archivo CSV para escritura
        writer=csv.writer(file)
        writer.writerow(["Nombre", "Extensión", "Tamaño ", "Ruta"]) ## Escribe la fila de encabezado

        for a in archivos: ## Escribe cada objeto ArchivoInfo como una fila en el CSV
            writer.writerow([a.nombre, a.extension, formatear_bytes(a.tamano_bytes), a.ruta])

 
def main() -> None:

    args=leer_argumentos()
    carpeta = Path(args.path)  # por ahora analiza la carpeta actual
    archivos = escanear_archivos(carpeta)

    print(f"\n📁 Carpeta: {carpeta.resolve()}")
    print(f"📄 Archivos encontrados: {len(archivos)}")

    print(f"\n--- MOSTRANDO {min(args.limite, len(archivos))} ---")
    print(f"Archivos encontrados: {len(archivos)}")

    for a in archivos[:args.limite]: ## Muestra en la consola los primeros archivos encontrados, limitados por el argumento --limite
    
        tam=formatear_bytes(a.tamano_bytes) if args.human else f"{a.tamano_bytes} bytes"  ## Si se especificó --human, cambiar  unidad, de lo contrario muestra el tamaño en bytes
        print(f"- {a.nombre} | {a.extension} | {tam}") ## Tomamos en cuenta que a es un objeto ArchivoInfo 
        # y por eso accedemos a sus atributos nombre, extension y tamano_bytes

    if not args.no_csv: ## Si no se especificó la opción --no-csv, exporta el reporte a CSV
            print(f"\nExportando reporte a CSV...")
            exportar_a_csv(archivos, args.output)
            print(f"Reporte exportado a {args.output}")
            
    def resumen_por_extension(archivos: List[ArchivoInfo]) -> Dict[str, Tuple[int, int]]:
        resumen : Dict[str, Tuple[int, int]]={}  # Diccionario para almacenar el resumen por extensión
        acumulador = defaultdict(lambda: [0, 0])  # Acumulador para contar cantidad y tamaño por extensión

        for a in archivos:  # Itera sobre cada archivo encontrado
            ext=a.extension if a.extension else '(sin extensión)'  # Si no tiene extensión, se etiqueta como '(sin extensión)'
            acumulador[ext][0] += 1  # Incrementa el conteo de archivos para esta extensión
            acumulador[ext][1] += a.tamano_bytes  # Acumula el tamaño total de archivos para esta extensión

        for ext,(cantidad, total_bytes) in acumulador.items():  # Itera sobre el acumulador para construir el resumen final
                resumen[ext]=(cantidad, total_bytes)  # Almacena la cantidad y el tamaño total en el resumen

        return resumen

        
    print('\n--- RESUMEN POR EXTENSIÓN ---')
    resumen=resumen_por_extension(archivos)  # Obtiene el resumen por extensión
    
    for ext,(cantidad, total_bytes) in sorted(resumen.items(),key=lambda x: x[1][1],reverse=True):
         ## Ordena el resumen por tamaño total en bytes de forma descendente
         
            if args.human:  # Si se especificó la opción --human, formatea el tamaño total a un formato legible
                unidad_B=formatear_bytes(total_bytes)  # llamo a la función formatear_bytes para convertir el tamaño total a un formato legible
                print(f"{ext}: {cantidad} archivos, {unidad_B}")  
            else:
                print(f"{ext}: {cantidad} archivos, {total_bytes} bytes") 

    


        
    




if __name__ == "__main__":
    main()




