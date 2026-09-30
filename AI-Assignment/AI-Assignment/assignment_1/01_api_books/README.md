# 1. API Data Retrieval and SQLite Storage

This program fetches book information from the Open Library REST API,
stores the title, author and publication year in a local SQLite database,
and retrieves/displays the stored records.

## Run

From the repository root:

```bash
pip install -r requirements.txt
python assignment_1/01_api_books/api_books.py
```

The script creates `books.db` in this folder.
