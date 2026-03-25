# Academic Metadata Extractor

Pipeline en Python para extraer metadatos bibliográficos de artículos académicos desde arXiv y transformar información semiestructurada en datos estructurados exportables a CSV y JSON.

---

## Descripción del proyecto

Este miniproyecto tiene como objetivo automatizar la recolección y organización de información bibliográfica de artículos académicos. A partir de una consulta temática, el sistema obtiene resultados desde arXiv, extrae campos relevantes, limpia el texto y lo transforma en un formato estructurado que puede ser utilizado para análisis, visualización o almacenamiento.

El proyecto fue diseñado como una demostración práctica de:

- extracción de datos desde una fuente académica
- transformación de datos semiestructurados a estructurados
- limpieza y normalización de texto
- organización de un pipeline en Python
- exportación de resultados en formatos reutilizables

---

## Problema que resuelve

Gran parte de la información académica disponible en la web aparece en formatos semiestructurados: páginas con títulos, autores, resúmenes, fechas y categorías que son legibles para humanos, pero no siempre están listas para análisis computacional directo.

Este proyecto busca resolver ese problema tomando registros académicos y convirtiéndolos en una tabla organizada con campos estandarizados.

---

## Objetivo general

Construir un pipeline en Python que permita consultar artículos académicos, extraer sus metadatos bibliográficos y convertirlos en un conjunto de datos estructurado.

---

## Objetivos específicos

- Consultar artículos académicos a partir de una palabra clave o tema.
- Extraer información relevante como título, autores, fecha, resumen y enlace.
- Limpiar y normalizar los campos textuales.
- Convertir los resultados en una estructura tabular.
- Exportar los datos procesados a archivos CSV y JSON.

---

## Fuente de datos

La fuente utilizada en esta primera versión es **arXiv**, un repositorio abierto de artículos académicos ampliamente usado en áreas como informática, lingüística computacional, matemática y física.

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
├── src/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── output/
│   ├── articles.csv
│   └── articles.json
│
├── README.md
├── requirements.txt
└── main.py
