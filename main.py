from pathlib import Path
from src.extract import fetch_arxiv_data
from src.transform import transform_entries
from src.load import save_to_csv, save_to_json


def main():
    query = "computational linguistics"
    max_results = 20

    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True) # Crea el directorio de salida si no existe

    print(f"Buscando artículos sobre: {query}")
    entries = fetch_arxiv_data(query=query, max_results=max_results)

    print(f"Se encontraron {len(entries)} artículos")
    structured_data = transform_entries(entries)

    save_to_csv(structured_data, "output/articles.csv")
    save_to_json(structured_data, "output/articles.json")

    print("Archivos guardados en output/articles.csv y output/articles.json")


if __name__ == "__main__":
    main()