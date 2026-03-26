import sqlite3


def save_to_sqlite(data, db_path: str):
    """
    Guarda los artículos en una base de datos SQLite.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS articles (
        article_id TEXT PRIMARY KEY,
        title TEXT,
        authors TEXT,
        author_count INTEGER,
        published TEXT,
        summary TEXT,
        primary_category TEXT,
        category TEXT,
        url TEXT,
        pdf_url TEXT
    )
    """)

    for article in data:
        cursor.execute("""
        INSERT OR REPLACE INTO articles (
            article_id,
            title,
            authors,
            author_count,
            published,
            summary,
            primary_category,
            category,
            url,
            pdf_url
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            article.get("article_id", ""),
            article.get("title", ""),
            article.get("authors", ""),
            article.get("author_count", 0),
            article.get("published", ""),
            article.get("summary", ""),
            article.get("primary_category", ""),
            article.get("category", ""),
            article.get("url", ""),
            article.get("pdf_url", "")
        ))

    conn.commit()
    conn.close()