import csv
import sqlite3
from pathlib import Path


CSV_PATH = Path(__file__).with_name("users.csv")
DB_PATH = Path(__file__).with_name("users.db")


def create_table(connection: sqlite3.Connection) -> None:
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
        """
    )
    connection.commit()


def import_users(
    connection: sqlite3.Connection, csv_path: Path
) -> int:
    inserted = 0

    with csv_path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        required_columns = {"name", "email"}
        if not required_columns.issubset(reader.fieldnames or set()):
            raise ValueError(
                "CSV must contain 'name' and 'email' columns."
            )

        for row in reader:
            name = (row.get("name") or "").strip()
            email = (row.get("email") or "").strip()

            if not name or not email:
                print("Skipping row with missing name/email.")
                continue

            try:
                connection.execute(
                    "INSERT INTO users (name, email) VALUES (?, ?)",
                    (name, email),
                )
                inserted += 1
            except sqlite3.IntegrityError:
                print(f"Skipping duplicate email: {email}")

    connection.commit()
    return inserted


def display_users(connection: sqlite3.Connection) -> None:
    rows = connection.execute(
        "SELECT id, name, email FROM users ORDER BY id"
    ).fetchall()

    print("\nUsers stored in SQLite:")
    print("-" * 70)

    for user_id, name, email in rows:
        print(f"{user_id:>3} | {name:<20} | {email}")


def main() -> None:
    try:
        with sqlite3.connect(DB_PATH) as connection:
            create_table(connection)
            inserted = import_users(connection, CSV_PATH)
            display_users(connection)

        print(f"\nInserted {inserted} new record(s).")
        print(f"Database created at: {DB_PATH}")

    except (OSError, ValueError, sqlite3.Error) as exc:
        print(f"Import failed: {exc}")


if __name__ == "__main__":
    main()
