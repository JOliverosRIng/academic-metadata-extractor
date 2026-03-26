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
           