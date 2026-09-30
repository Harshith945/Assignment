import sqlite3
from pathlib import Path

import requests


API_URL = "https://openlibrary.org/search.json"
DB_PATH = Path(__file__).with_name("books.db")


def fetch_books(query: str = "python", limit: int = 10) -> list[dict]:
    """Fetch books from the Open Library REST API."""
    response = requests.get(
        API_URL,
        params={"q": query, "limit": limit},
        timeout=15,
    )
    response.raise_for_status()

    data = response.json()
    books = []

    for doc in data.get("docs", []):
        title = doc.get("title")
        if not title:
            continue

        authors = doc.get("author_name", [])
        author = ", ".join(authors[:3]) if authors else "Unknown"

        books.append(
            {
                "title": title,
                "author": author,
                "publication_year": doc.get("first_publish_year"),
            }
        )

    return books


def create_table(connection: sqlite3.Connection) -> None:
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT,
            publication_year INTEGER
        )
        """
    )
    connection.commit()


def store_books(
    connection: sqlite3.Connection, books: list[dict]
) -> None:
    connection.executemany(
        """
        INSERT INTO books (title, author, publication_year)
        VALUES (?, ?, ?)
        """,
        [
            (
                book["title"],
                book["author"],
                book["publication_year"],
            )
            for book in books
        ],
    )
    connection.commit()


def display_books(connection: sqlite3.Connection) -> None:
    rows = connection.execute(
        """
        SELECT id, title, author, publication_year
        FROM books
        ORDER BY id
        """
    ).fetchall()

    print("\nBooks stored in SQLite:")
    print("-" * 90)

    for book_id, title, author, year in rows:
        print(f"{book_id:>3} | {title[:45]:<45} | {author[:25]:<25} | {year}")


def main() -> None:
    try:
        books = fetch_books()

        if not books:
            print("No books were returned by the API.")
            return

        with sqlite3.connect(DB_PATH) as connection:
            create_table(connection)
            store_books(connection, books)
            display_books(connection)

        print(f"\nDatabase created at: {DB_PATH}")

    except requests.RequestException as exc:
        print(f"API request failed: {exc}")
    except sqlite3.Error as exc:
        print(f"SQLite error: {exc}")


if __name__ == "__main__":
    main()
