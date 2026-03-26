import requests
import feedparser

def fetch_arxiv_data(query: str, max_results: int = 10):
      """
    Consulta la API de arXiv y devuelve los resultados parseados.

    Parámetros:
        query (str): tema o palabra clave de búsqueda
        max_results (int): número máximo de artículos a recuperar

    Retorna:
        list: lista de entradas devueltas por arXiv
    """
     base_url = 'http://export.arxiv.org/api/query?' # URL base de la API de arXiv

     params = {
            'search_query': query, # consulta de búsqueda
            'start': 0, # índice de inicio para paginación
            'max_results': max_results # número máximo de resultados a recuperar
     }

     response = requests.get(base_url, params=params, timeout=30) # realizar la solicitud GET a la API de arXiv
     response.raise_for_status() # verificar que la solicitud fue exitosa
     feed = feedparser.parse(response.text) # parsear la respuesta XML utilizando feedparser
     return feed.entries # retornar las entradas parseadas del feed