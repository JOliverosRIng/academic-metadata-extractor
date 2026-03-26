import sqlite3


def main():
    conn = sqlite3.connect("output/articles.db")
    cursor = conn.cursor()

    # 1. Ver tablas
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tablas en la base de datos:")
    for table in tables:
        print("-", table[0])

    # 2. Contar artículos
    cursor.execute("SELECT COUNT(*) FROM articles;")
    total_articles = cursor.fetchone()[0]
    print(f"\nTotal de artículos: {total_articles}")

    # 3. Ver algunos títulos
    cursor.execute("SELECT title, authors, primary_category FROM articles LIMIT 5;")
    rows = cursor.fetchall()

    print("\nPrimeros 5 artículos:")
    for i, row in enumerate(rows, start=1):
        title, authors, category = row
        print(f"{i}. {title}")
        print(f"   Autores: {authors}")
        print(f"   Categoría: {category}\n")

    # 4. Contar artículos por categoría
    cursor.execute("""
        SELECT primary_category, COUNT(*)
        FROM articles
        GROUP BY primary_category
        ORDER BY COUNT(*) DESC
        LIMIT 10;
    """)
    categories = cursor.fetchall()

    print("Top categorías:")
    for category, count in categories:
        print(f"- {category}: {count}")

    conn.close()


if __name__ == "__main__":
    main()