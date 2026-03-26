import json
import pandas as pd # Importa pandas, que nos ayuda a convertir los datos en tabla.

def save_to_csv(data, filepath:str):
    """
    Guarda los datos en un archivo CSV.
    """
    df = pd.DataFrame(data) # Convierte la lista de diccionarios en un DataFrame de pandas
    df.to_csv(filepath, index=False, encoding="utf-8") # Guarda el DataFrame en un archivo CSV sin incluir el índice

def save_to_json(data, filepath:str):
     """
     Guarda los datos en un archivo JSON.
     """
     with open(filepath, "w", encoding="utf-8") as f: # Abre el archivo en modo escritura con codificación UTF-8
          json.dump(data, f, ensure_ascii=False, indent=4) # Escribe los datos en formato JSON con una indentación de 4 espacios