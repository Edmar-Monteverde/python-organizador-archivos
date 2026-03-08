## 📁 Python – Organizador y Auditor de Archivos

Herramienta en Python para analizar carpetas, listar archivos, agruparlos por extensión, calcular tamaños y exportar reportes en CSV..


## 🚀 Funcionalidades

- 📂 Escaneo de archivos en una carpeta dada

- 📄 Listado de archivos con nombre, extensión y tamaño

- 🗂️ Resumen agrupado por extensión

- 📊 Cálculo de cantidad y tamaño total por tipo de archivo

- 📦 Conversión de tamaños a formato humano (KB / MB / GB)

- 📄 Exportación de reportes a CSV

- ⚙️ Configuración mediante argumentos de línea de comandos (argparse)

- 🧱 Código modular y organizado por responsabilidades

---

## 📁 Estructura del proyecto
```text
python-organizador-archivos/
│
├── src/
│   ├── auditor.py              # Escaneo de archivos
│   ├── exportar.py             # Exportación a CSV
│   ├── extensiones.py          # Resumen por extensión
│   ├── formatear_tamano.py     # Conversión de bytes a KB/MB/GB
│   └── main.py                 # Punto de entrada (CLI)
│
├── output/
│   └── reporte.csv             # Reportes generados (no versionados)
│
├── .gitignore
└── README.md
```

---
### ▶️ Uso


Desde la raíz del proyecto, ejecuta:

 ▶️Usar valores por defecto: 
```bash
📌 python src/main.py
```

▶️Analizar una carpeta específica 
```bash
📌python src/main.py --path /ruta/a/la/carpeta

```
▶️Limitar la cantidad de archivos mostrados

```bash
📌 python src/main.py --limit 5
```
▶️Mostrar tamaños en formato humano
```bash
📌 python src/main.py --human
```

▶️Exportar el reporte con un nombre personalizado 
```bash
📌python src/main.py --output output/mi_reporte.csv
```

▶️Ejecutar sin generar CSV

```bash
📌 python src/main.py --no-csv

```
---
## ⚙️ Argumentos disponibles

| Argumento  | Descripción                                  |
| ---------- | -------------------------------------------- |
| `--path`   | Carpeta a analizar (default: carpeta actual) |
| `--limit`  | Número de archivos a mostrar por pantalla    |
| `--output` | Ruta del archivo CSV de salida               |
| `--no-csv` | No genera el archivo CSV                     |
| `--human`  | Muestra tamaños en KB / MB / GB              |

---
## 🧠 Aprendizajes clave

Este proyecto me permitió practicar y consolidar:

- Uso de pathlib para trabajar con rutas de forma multiplataforma

- Creación de herramientas por línea de comandos con argparse

- Separación de responsabilidades en módulos

- Uso de @dataclass para modelar datos

- Procesamiento y agrupación de información con defaultdict

- Exportación de datos a CSV reutilizables

- Diseño de código limpio y mantenible

- Uso práctico de Git durante el desarrollo

---
## 🛠️ Tecnologías usadas

- Python 3

- argparse

- pathlib

- dataclasses

- collections.defaultdict

- Git & GitHub

 ---
## 🎯 Objetivo del proyecto

- Proyecto creado con fines de aprendizaje y portafolio, enfocado en:

- Automatización

- Procesamiento de datos

- Buenas prácticas de programación

- Construcción de herramientas útiles por CLI

---
## 📌 Posibles mejoras futuras

- Escaneo recursivo de subcarpetas (--recursive)

- Filtros por tipo de archivo

- Ordenar resultados por tamaño o cantidad

- Tests automatizados

- Exportación a otros formatos (JSON, Excel)



👤 Autor

Edmar Monteverde
Desarrollador en formación – Python / Backend
📌 Proyecto desarrollado como parte de mi proceso de aprendizaje.







