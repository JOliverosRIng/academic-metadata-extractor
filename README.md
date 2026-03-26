# Academic Metadata Extractor

Pipeline en Python para extraer metadatos bibliográficos de artículos académicos desde arXiv, transformar información semiestructurada en datos estructurados y almacenarla en **CSV**, **JSON** y **SQLite**.

---

## Descripción del proyecto

Este miniproyecto automatiza la recolección y organización de información bibliográfica de artículos académicos. A partir de una consulta temática, el sistema obtiene resultados desde arXiv, extrae campos relevantes, limpia el texto y lo transforma en un formato estructurado para análisis, almacenamiento y consulta posterior.

El proyecto demuestra de forma práctica:

- extracción de datos desde una fuente académica
- transformación de datos semiestructurados a estructurados
- limpieza y normalización de texto
- exportación en formatos reutilizables
- carga de datos a una base de datos relacional ligera con SQLite

---

## Problema que resuelve

Gran parte de la información académica disponible en la web aparece en formatos semiestructurados: páginas con títulos, autores, resúmenes, fechas y categorías que son legibles para humanos, pero no siempre están listas para análisis computacional directo.

Este proyecto resuelve ese problema tomando registros académicos y convirtiéndolos en:

- una tabla estructurada
- un archivo JSON reutilizable
- una base de datos SQLite consultable con SQL

---

## Objetivo general

Construir un pipeline en Python que permita consultar artículos académicos, extraer sus metadatos bibliográficos, limpiarlos, estructurarlos y almacenarlos en múltiples formatos.

---

## Objetivos específicos

- Consultar artículos académicos a partir de una palabra clave o tema.
- Extraer información relevante como título, autores, fecha, resumen y enlaces.
- Limpiar y normalizar los campos textuales.
- Transformar los resultados en una estructura tabular.
- Exportar los datos procesados a archivos CSV y JSON.
- Almacenar los registros en una base de datos SQLite para consulta posterior.

---

## Fuente de datos

La fuente utilizada en esta versión es **arXiv**, un repositorio abierto de artículos académicos ampliamente usado en áreas como informática, lingüística computacional, matemática y física.

Se eligió arXiv porque:

- ofrece acceso a metadatos de artículos
- permite consultas temáticas
- tiene una estructura adecuada para extracción automática
- facilita la construcción de un proyecto reproducible y claro para portafolio

---

## Tecnologías utilizadas

- **Python**
- **requests** para realizar consultas HTTP
- **feedparser** para procesar la respuesta de arXiv
- **pandas** para estructurar y exportar los datos
- **sqlite3** para almacenar los artículos en una base de datos SQLite
- **re** para limpieza de texto
- **json** para exportación en formato JSON

---

## Estructura del proyecto

```bash
academic-metadata-extractor/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── output/
│   ├── articles.csv
│   ├── articles.json
│   └── articles.db
│
├── src/
│   ├── database.py
│   ├── extract.py
│   ├── load.py
│   └── transform.py
│
├── .gitignore
├── main.py
├── README.md
├── requirements.txt
└── check_db.py