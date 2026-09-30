# AI/ML Engineer Technical Assignment

This repository contains my complete submission for the technical
assignment.

## Repository Structure

```text
AI-Assignment/
│
├── assignment_1/
│   ├── 01_api_books/
│   │   ├── api_books.py
│   │   └── README.md
│   │
│   ├── 02_student_scores/
│   │   ├── student_scores.py
│   │   └── README.md
│   │
│   └── 03_csv_to_sqlite/
│       ├── csv_to_sqlite.py
│       ├── users.csv
│       └── README.md
│
├── assignment_2/
│   └── assignment_2_answers.md
│
├── complex_python_project/
│   └── README.md
│
├── complex_database_project/
│   └── README.md
│
├── requirements.txt
└── README.md
```

---

# Assignment 1

## 1. API Data Retrieval and Storage

`assignment_1/01_api_books/api_books.py`

The program:

- Calls the Open Library REST API
- Retrieves book information in JSON format
- Extracts title, author and publication year
- Creates a local SQLite database
- Inserts the API data into a `books` table
- Retrieves the stored records using SQL
- Displays the records

## 2. Data Processing and Visualization

`assignment_1/02_student_scores/student_scores.py`

The program:

- Fetches student score data from a public JSON endpoint
- Calculates the average score for each student
- Calculates the overall average
- Creates a Matplotlib bar chart

## 3. CSV Data Import to SQLite

`assignment_1/03_csv_to_sqlite/csv_to_sqlite.py`

The program:

- Reads `users.csv`
- Validates the required columns
- Inserts users into SQLite
- Prevents duplicate email records
- Displays the stored records

---

# Assignment 2

The detailed answers are available in:

`assignment_2/assignment_2_answers.md`

Topics covered:

1. Self-assessment of LLM / AI / ML / Deep Learning skills
2. High-level architecture of an LLM chatbot
3. Vector databases, a hypothetical use case, architecture and selection criteria

---

# Most Complex Python Code

I selected my **AI Research Agent** as the most complex Python/GenAI
project because it combines multiple processing stages in a LangGraph
workflow.

The workflow contains:

```text
Planner
   ↓
Researcher
   ↓
Summarizer
   ↓
Evaluator
   ↓
┌───────────────┐
│ Sufficient?   │
└───────┬───────┘
    No  │  Yes
        │
        └──→ Research again
                 or
               Final report
```

See `complex_python_project/README.md` for the project description and
replace its TODO URL with the actual public repository URL.

---

# Most Complex Database Code

I selected my **Resume ATS Assistant** because its recruiter mode uses
semantic matching between resumes and job descriptions with Pinecone.

See `complex_database_project/README.md` for the project description and
replace its TODO URL with the actual public repository URL.

---

# Setup

Python 3.10+ is recommended.

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run Assignment 1

### API → SQLite

```bash
python assignment_1/01_api_books/api_books.py
```

### Student Scores → Average → Chart

```bash
python assignment_1/02_student_scores/student_scores.py
```

### CSV → SQLite

```bash
python assignment_1/03_csv_to_sqlite/csv_to_sqlite.py
```

---

# Design Notes

The examples intentionally use parameterized SQL queries rather than
constructing SQL statements with user-controlled strings.

API calls use timeouts and `raise_for_status()` so HTTP failures are not
silently ignored.

The student-score example processes only the available numeric subject
scores and calculates the arithmetic mean.

---

# External Data Sources

The book example uses the Open Library Search API.

The student-score example uses Sling Academy's public student-score JSON
dataset. The dataset provides student identifiers and multiple subject
scores such as mathematics, history, physics, chemistry, biology, English
and geography.

---

# Submission Checklist

Before submitting the repository:

- [ ] Make the GitHub repository public, if the company requested a public link.
- [ ] Push all files in this repository.
- [ ] Replace the two `TODO` project URLs with your actual GitHub URLs.
- [ ] Run all three Assignment 1 programs locally.
- [ ] Confirm that the generated SQLite databases are not required to be committed.
- [ ] Confirm the README opens correctly on GitHub.
- [ ] Submit the root GitHub repository URL.
