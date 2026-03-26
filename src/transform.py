import re # Importa el módulo de expresiones regulares para limpiar el texto

def clean_text(text:str) -> str:
    """
     Limpia el texto eliminando caracteres no deseados y normalizando espacios.
     elimina espacios, saltos de línea, tabulaciones y caracteres especiales.
     """
    if not text:
        return "" # Si el texto es None o vacío, devuelve una cadena vacía
    
    text = re.sub(r"\s+", " ", text).strip() # Reemplaza múltiples espacios por uno solo y elimina espacios al inicio y al final
    return text

def transform_entries(entries): #Esta función recibe la lista de artículos devueltos por extract.py. Su trabajo es convertirlos en una lista ordenada de diccionarios.
     """
     Convierte las entradas de arXiv en una lista de diccionarios estructurados.
     """
     structured_data = [] # Inicializa una lista vacía para almacenar los artículos estructurados

     for entry in entries:
         article = {
             "title": clean_text(entry.get("title", "")),
             "authors": ", ".join(
                 [author.name for author in entry.get("authors", [])]
             ),
             "published": entry.get("published", ""),
             "summary": clean_text(entry.get("summary", "")),
             "category": entry.tags[0]["term"] if hasattr(entry, "tags") and entry.tags else "",
             "url": entry.get("link", "")
         }
         
         structured_data.append(article)
         
     return structured_data