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

def get_pdf_url(entry) -> str:
    """
     Obtiene la URL del PDF de un artículo de arXiv.
     Busca en los enlaces del artículo el que tenga el tipo "application/pdf".
     """
    for link in entry.get("links", []):
        href = link.get("href", "")
        title = link.get("title", "")
        link_type = link.get("type", "")

        if title == "pdf" or link_type == "application/pdf":
            return href # Devuelve la URL del PDF si se encuentra
    
    return "" # Devuelve una cadena vacía si no se encuentra la URL del PDF

def transform_entries(entries): #Esta función recibe la lista de artículos devueltos por extract.py. Su trabajo es convertirlos en una lista ordenada de diccionarios.
    """
    Convierte las entradas de arXiv en una lista de diccionarios estructurados.
    """
    structured_data = [] # Inicializa una lista vacía para almacenar los artículos estructurados

    for entry in entries:
        authors_list = [author.name for author in entry.get("authors", [])] # Obtiene la lista de autores del artículo

        article = {
            "article_id": entry.get("id", ""),
            "title": clean_text(entry.get("title", "")),
            "authors": ", ".join(authors_list), # Convierte la lista de autores en una cadena separada por comas
            "authors_count": len(authors_list), # Cuenta el número de autores
            "published": entry.get("published", ""),
            "summary": clean_text(entry.get("summary", "")),
            "category": entry.tags[0]["term"] if hasattr(entry, "tags") and entry.tags else "",
            "url": entry.get("link", ""),
            "pdf_url": get_pdf_url(entry)
        }
        
        structured_data.append(article)
        
    return structured_data