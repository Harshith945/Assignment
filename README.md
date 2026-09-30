# AI/ML Engineer Technical Assignment

This repository contains my complete submission for the AI/ML Engineer technical assignment.

The submission is divided into two major sections:

1. **Assignment 1 — Python, REST API, CSV, SQLite and Data Visualization**
2. **Assignment 2 — AI/ML, LLM, RAG and Vector Database concepts**

The repository also includes two projects demonstrating my practical experience with Generative AI and database-driven AI applications:

- **AI Research Agent** — Complex Python / Agentic AI project
- **Resume ATS Assistant** — Complex database / Semantic Search project

---

# Table of Contents

- [Repository Overview](#repository-overview)
- [Repository Structure](#repository-structure)
- [Assignment 1](#assignment-1)
  - [Task 1 - REST API to SQLite](#task-1---rest-api-to-sqlite)
  - [Task 2 - Student Scores and Visualization](#task-2---student-scores-and-visualization)
  - [Task 3 - CSV to SQLite](#task-3---csv-to-sqlite)
- [Assignment 2](#assignment-2)
  - [Self Assessment](#1-self-assessment)
  - [LLM Chatbot Architecture](#2-llm-chatbot-architecture)
  - [RAG Architecture](#3-rag-architecture)
  - [Vector Database](#4-vector-database)
  - [Vector Database Selection](#5-vector-database-selection)
- [Complex Python Project](#complex-python-project)
- [Complex Database Project](#complex-database-project)
- [Technologies Used](#technologies-used)
- [Error Handling](#error-handling)
- [Security and Good Practices](#security-and-good-practices)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Design Decisions](#design-decisions)
- [Testing](#testing)
- [Future Improvements](#future-improvements)
- [Submission Checklist](#submission-checklist)

---

# Repository Overview

The objective of this assignment is to demonstrate practical knowledge of:

- Python programming
- REST APIs
- JSON processing
- CSV processing
- SQLite
- SQL
- Data visualization
- Exception handling
- LLM applications
- Generative AI
- Retrieval-Augmented Generation
- Embeddings
- Vector databases
- Semantic search
- Agentic AI
- LangChain
- LangGraph

The implementation focuses on keeping the solutions simple, readable and practical while following common software-development practices.

---

# Repository Structure

```text
AI-Assignment/
│
├── assignment_1/
│   │
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
├── .gitignore
└── README.md
```

---

# Assignment 1

Assignment 1 contains three Python implementations.

## Tasks

| Task | Description | Main Technologies |
|---|---|---|
| 1 | REST API → SQLite → Display | Python, Requests, SQLite |
| 2 | Student Scores → Average → Chart | Python, Requests, Matplotlib |
| 3 | CSV → SQLite | Python, CSV, SQLite |

---

# Task 1 - REST API to SQLite

## Objective

The objective of this task is to:

1. Call a public REST API.
2. Retrieve book information in JSON format.
3. Extract the required fields.
4. Store the information in a SQLite database.
5. Retrieve the stored information using SQL.
6. Display the records.

---

## File

```text
assignment_1/01_api_books/api_books.py
```

---

## API Used

The implementation uses the Open Library Search API.

```text
https://openlibrary.org/search.json
```

The search query used by the application is:

```text
python
```

The application requests a limited number of results instead of retrieving an unnecessarily large response.

---

# Task 1 Workflow

```text
                REST API
                   │
                   ▼
        HTTP GET Request
                   │
                   ▼
             JSON Response
                   │
                   ▼
         Extract Required Fields
                   │
          ┌────────┼────────┐
          ▼        ▼        ▼
        Title    Author    Year
          │        │        │
          └────────┼────────┘
                   ▼
             SQLite Table
                   │
                   ▼
             SQL SELECT
                   │
                   ▼
           Display Records
```

---

# Implementation Details

## Step 1 - Import Required Libraries

The program uses:

```python
import requests
import sqlite3
```

### `requests`

Used for making the HTTP request to the REST API.

### `sqlite3`

Used for creating and interacting with the local SQLite database.

---

# Step 2 - API Request

The application sends a GET request to the Open Library API.

Conceptually:

```python
response = requests.get(
    API_URL,
    params={
        "q": "python",
        "limit": 10
    },
    timeout=10
)
```

Using `params` allows query parameters to be passed cleanly instead of manually constructing the URL.

---

# Step 3 - Validate HTTP Response

The response is checked using:

```python
response.raise_for_status()
```

This ensures that HTTP errors are not silently ignored.

For example:

- `200` → successful request
- `404` → resource not found
- `500` → server-side error

If the API request fails, the program handles the exception.

---

# Step 4 - Convert Response to JSON

The API response is converted into a Python dictionary:

```python
data = response.json()
```

The book records are then retrieved from the response.

---

# Step 5 - Extract Required Information

For every book, the application extracts:

- Title
- Author
- First publication year

A book can contain multiple authors, so the implementation handles the author list and stores a readable representation.

Example:

```text
Title: Learning Python
Author: Mark Lutz
Publication Year: 2013
```

---

# Step 6 - Create SQLite Database

A local SQLite database is created.

```text
books.db
```

SQLite is suitable for this task because:

- It does not require a separate database server.
- It is lightweight.
- It is included with Python.
- It supports SQL.
- It is sufficient for small datasets.

---

# Database Schema

The application creates the following table:

```sql
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT,
    publication_year INTEGER
);
```

## Columns

| Column | Type | Description |
|---|---|---|
| `id` | INTEGER | Unique identifier |
| `title` | TEXT | Book title |
| `author` | TEXT | Author name |
| `publication_year` | INTEGER | First publication year |

---

# Step 7 - Insert Records

Records are inserted using parameterized SQL.

```python
connection.execute(
    """
    INSERT INTO books
    (title, author, publication_year)
    VALUES (?, ?, ?)
    """,
    (title, author, publication_year)
)
```

The `?` placeholders are important because they separate SQL instructions from data values.

---

# Step 8 - Retrieve Records

After inserting the data, the application executes:

```sql
SELECT id, title, author, publication_year
FROM books;
```

The retrieved records are then printed.

Example output:

```text
1 | Learning Python | Mark Lutz | 2013
2 | Python Crash Course | Eric Matthes | 2019
...
```

---

# Error Handling

The implementation handles:

```python
requests.RequestException
```

for API-related failures.

SQLite-related failures are handled using:

```python
sqlite3.Error
```

The API request also uses a timeout.

This prevents the application from waiting indefinitely if the API becomes unavailable.

---

# How to Run

From the repository root:

```bash
python assignment_1/01_api_books/api_books.py
```

The program will:

1. Call the API.
2. Process the JSON response.
3. Create `books.db`.
4. Insert records.
5. Retrieve records.
6. Display them.

---

# Task 2 - Student Scores and Visualization

## Objective

The objective of this task is to:

1. Fetch student score data from a public API.
2. Process the JSON response.
3. Calculate the average score for each student.
4. Calculate the overall average.
5. Visualize the student averages using a bar chart.

---

## File

```text
assignment_1/02_student_scores/student_scores.py
```

---

# Task 2 Workflow

```text
              Student Score API
                     │
                     ▼
                JSON Data
                     │
                     ▼
             Extract Scores
                     │
                     ▼
             Calculate Average
                     │
            ┌────────┴────────┐
            ▼                 ▼
     Student Average     Overall Average
            │
            ▼
        Matplotlib
            │
            ▼
       Bar Chart PNG
```

---

# API Request

The program retrieves JSON data from the configured public student-score endpoint.

The request follows the same basic process:

```python
response = requests.get(
    API_URL,
    timeout=10
)
```

Then:

```python
response.raise_for_status()
```

and:

```python
data = response.json()
```

---

# JSON Processing

The program supports a JSON response containing a list of students.

Depending on the response structure, the program can process the student records from the appropriate list field.

Each student record contains subject scores.

---

# Subjects

The implementation processes the available subject fields, including:

- Mathematics
- History
- Physics
- Chemistry
- Biology
- English
- Geography

The implementation does not assume that every student necessarily has every score.

Only available numeric subject scores are included in the calculation.

---

# Average Calculation

For every student:

```text
Average =
Sum of available subject scores
/
Number of available subject scores
```

For example:

```text
Math       = 80
Physics    = 70
Chemistry  = 90

Average = (80 + 70 + 90) / 3
        = 80
```

---

# Overall Average

The application also calculates the overall average from the processed student averages.

This provides a high-level view of the dataset.

---

# Visualization

Matplotlib is used to create a bar chart.

Conceptually:

```text
Score
100 |             █
 90 |       █     █
 80 |   █   █     █
 70 |   █   █ █   █
 60 |   █   █ █   █
    +------------------
       A   B   C   D
          Students
```

The X-axis represents students.

The Y-axis represents their average scores.

---

# Output File

The generated chart is saved as:

```text
student_average_scores.png
```

The chart is generated using Matplotlib.

---

# Error Handling

The program handles:

- HTTP request errors
- Invalid API responses
- Missing data
- Invalid score values
- Data processing errors

This prevents the application from failing silently.

---

# How to Run

```bash
python assignment_1/02_student_scores/student_scores.py
```

The application will:

1. Fetch the student data.
2. Calculate averages.
3. Print the results.
4. Calculate the overall average.
5. Generate the bar chart.
6. Save the chart as a PNG file.

---

# Task 3 - CSV to SQLite

## Objective

The objective is to:

1. Read user data from a CSV file.
2. Validate the input.
3. Create a SQLite database.
4. Store the users.
5. Prevent duplicate email addresses.
6. Display the stored records.

---

## Files

```text
assignment_1/03_csv_to_sqlite/
│
├── csv_to_sqlite.py
├── users.csv
└── README.md
```

---

# Task 3 Workflow

```text
                 users.csv
                    │
                    ▼
                CSV Reader
                    │
                    ▼
               Validation
                    │
                    ▼
              SQLite Database
                    │
                    ▼
               users Table
                    │
                    ▼
               SQL SELECT
                    │
                    ▼
              Display Users
```

---

# CSV Input

The CSV file contains:

```csv
name,email
Aarav Sharma,aarav.sharma@example.com
Priya Reddy,priya.reddy@example.com
Rahul Kumar,rahul.kumar@example.com
Ananya Rao,ananya.rao@example.com
Vikram Singh,vikram.singh@example.com
```

---

# Step 1 - Read CSV

Python's built-in `csv` module is used.

The application opens the CSV file and uses `csv.DictReader`.

Conceptually:

```python
with open(CSV_FILE, newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
```

Using `DictReader` makes it easier to access columns by name.

For example:

```python
row["name"]
row["email"]
```

---

# Step 2 - Validate Columns

The program verifies that the CSV contains the required columns:

```text
name
email
```

If the required columns are missing, the program reports the problem rather than continuing with invalid input.

---

# Step 3 - Validate Values

The program checks that:

- Name is not empty.
- Email is not empty.

Blank records are skipped.

---

# Step 4 - Create Database

The application creates:

```text
users.db
```

and the following table:

```sql
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);
```

---

# Database Schema

| Column | Type | Constraint |
|---|---|---|
| `id` | INTEGER | Primary Key |
| `name` | TEXT | NOT NULL |
| `email` | TEXT | NOT NULL, UNIQUE |

---

# Step 5 - Insert Data

Parameterized SQL is used:

```python
connection.execute(
    """
    INSERT INTO users (name, email)
    VALUES (?, ?)
    """,
    (name, email)
)
```

This is preferable to constructing SQL strings manually.

---

# Duplicate Handling

The `email` column has a `UNIQUE` constraint.

Therefore, if the CSV contains:

```text
john@example.com
john@example.com
```

the second record will not create another user.

The implementation handles the resulting:

```python
sqlite3.IntegrityError
```

and continues processing.

---

# Step 6 - Retrieve Users

The application retrieves the stored records using:

```sql
SELECT id, name, email
FROM users;
```

Example output:

```text
1 | Aarav Sharma | aarav.sharma@example.com
2 | Priya Reddy | priya.reddy@example.com
3 | Rahul Kumar | rahul.kumar@example.com
```

---

# How to Run

```bash
python assignment_1/03_csv_to_sqlite/csv_to_sqlite.py
```

---

# Assignment 1 Summary

Assignment 1 demonstrates practical implementation of:

```text
REST API
   ↓
JSON
   ↓
Python Processing
   ↓
SQLite

CSV
   ↓
Python CSV Module
   ↓
Validation
   ↓
SQLite

JSON Student Data
   ↓
Data Processing
   ↓
Average Calculation
   ↓
Matplotlib
```

---

# Assignment 2

Assignment 2 contains the conceptual AI/ML and Generative AI answers.

The detailed answers are also available in:

```text
assignment_2/assignment_2_answers.md
```

The major topics are:

1. Self-assessment
2. LLM chatbot architecture
3. RAG
4. Vector databases
5. Vector database selection
6. Retrieval considerations

---

# 1. Self Assessment

## LLM / Generative AI — A

I have practical experience building LLM-based applications using:

- Python
- LangChain
- LangGraph
- RAG
- Embeddings
- Vector databases
- Prompt engineering
- Structured outputs
- LLM APIs

I have implemented multiple practical projects involving these technologies.

---

# AI / Machine Learning — B

I have a good understanding of core machine-learning concepts and their practical use in AI applications.

My focus has been on applying ML concepts in real-world AI applications while continuing to improve the depth of my ML knowledge.

---

# Deep Learning — C

I have a basic theoretical understanding of deep-learning concepts such as:

- Neural networks
- Activation functions
- Forward propagation
- Backpropagation
- Loss functions
- Optimizers
- CNN fundamentals

My practical experience is currently stronger in Generative AI, RAG and LLM applications than in independently building deep-learning models from scratch.

---

# 2. LLM Chatbot Architecture

A high-level LLM chatbot can be designed as follows:

```text
                       ┌──────────────┐
                       │     User     │
                       └──────┬───────┘
                              │
                              ▼
                       ┌──────────────┐
                       │  Chat UI/API │
                       └──────┬───────┘
                              │
                              ▼
                       ┌──────────────┐
                       │Input Handling│
                       └──────┬───────┘
                              │
               ┌──────────────┴──────────────┐
               │                             │
               ▼                             ▼
       Conversation History          Knowledge Retrieval
                                      (Optional RAG)
               │                             │
               └──────────────┬──────────────┘
                              │
                              ▼
                       ┌──────────────┐
                       │Prompt Builder│
                       └──────┬───────┘
                              │
                              ▼
                       ┌──────────────┐
                       │     LLM      │
                       └──────┬───────┘
                              │
                              ▼
                       ┌──────────────┐
                       │Output Validate│
                       └──────┬───────┘
                              │
                              ▼
                       ┌──────────────┐
                       │     User     │
                       └──────────────┘
```

---

# Component Details

## 1. User

The user sends a question or instruction.

Example:

```text
What is the leave policy?
```

---

## 2. Chat UI / API

The application receives the user input through:

- Web interface
- REST API
- Chat interface
- Application frontend

---

## 3. Input Processing

Input processing can include:

- Validation
- Length checks
- Input sanitization
- Intent detection
- Safety checks

---

## 4. Conversation History

The application stores relevant previous messages.

Example:

```text
User:
What is RAG?

Assistant:
RAG stands for Retrieval-Augmented Generation.

User:
Why are embeddings needed?
```

The second question depends on the context of the previous interaction.

Conversation history provides that context.

For very long conversations, the system can summarize older messages to control token usage.

---

# 5. Knowledge Retrieval

If the chatbot needs to answer questions using private documents, the application can use RAG.

The knowledge pipeline is:

```text
Documents
    ↓
Document Loader
    ↓
Text Splitting
    ↓
Chunking
    ↓
Embeddings
    ↓
Vector Database
```

At query time:

```text
User Query
    ↓
Query Embedding
    ↓
Similarity Search
    ↓
Relevant Chunks
```

---

# 6. Prompt Builder

The application combines:

```text
System Instructions
        +
User Query
        +
Conversation History
        +
Retrieved Context
```

and creates the final prompt sent to the LLM.

---

# 7. LLM

The LLM generates the response based on:

- System instructions
- User input
- Conversation context
- Retrieved context

---

# 8. Output Validation

The generated output can be validated before returning it.

Examples:

- JSON validation
- Pydantic validation
- Safety checks
- Business-rule validation
- Required-field validation

---

# 3. RAG Architecture

RAG stands for:

**Retrieval-Augmented Generation**

Instead of depending entirely on the information contained within the LLM, RAG retrieves relevant external information and provides it to the LLM as context.

---

# RAG Pipeline

```text
                 OFFLINE / INDEXING
                 
Documents
    ↓
Document Loading
    ↓
Text Cleaning
    ↓
Chunking
    ↓
Embedding Model
    ↓
Vector Database
```

Then during a user query:

```text
                 ONLINE / QUERY

User Question
      ↓
Query Embedding
      ↓
Similarity Search
      ↓
Top-K Relevant Chunks
      ↓
Prompt + Retrieved Context
      ↓
LLM
      ↓
Generated Answer
```

---

# Why RAG?

RAG is useful when:

- The information is private.
- The information changes frequently.
- The model does not have the required domain knowledge.
- The organization wants to update documents without retraining the LLM.

---

# RAG Example

Suppose an organization has:

```text
HR Policy.pdf
Leave Policy.pdf
Travel Policy.pdf
Benefits.pdf
Employee Handbook.pdf
```

An employee asks:

```text
How many days of parental leave can I take?
```

The system:

1. Converts the query into an embedding.
2. Searches the vector database.
3. Retrieves relevant chunks from the leave policy.
4. Adds those chunks to the prompt.
5. Sends the prompt to the LLM.
6. Generates an answer based on the retrieved context.

---

# 4. Vector Database

A vector database stores vector representations called embeddings and provides efficient similarity search.

---

# What are Embeddings?

An embedding model converts data such as text into numerical vectors.

Example:

```text
"How can I return my product?"
             ↓
       Embedding Model
             ↓
[0.12, -0.45, 0.71, 0.09, ...]
```

Another sentence with similar meaning may have a similar vector representation.

---

# Semantic Search

Traditional keyword search:

```text
Query:
How can I return my product?

Document:
Product return procedure
```

Keyword matching can work when the same terms appear.

But semantic search can also understand relationships such as:

```text
Query:
I want to send the item back.

Document:
Customers can request a product return within 30 days.
```

Even though the exact words are different, the meanings are related.

---

# Vector Database Workflow

```text
Document
    ↓
Chunk
    ↓
Embedding
    ↓
Vector
    ↓
Vector Database
```

Query:

```text
User Query
    ↓
Embedding
    ↓
Similarity Search
    ↓
Relevant Vectors
    ↓
Original Text Chunks
```

---

# 5. Vector Database Selection

## Hypothetical Use Case

I would build an:

**Enterprise HR Knowledge Assistant**

The application would contain documents such as:

- Employee handbook
- Leave policies
- Benefits
- Travel policies
- Payroll information
- HR FAQs

Employees could ask questions in natural language.

---

# Selected Vector Database

For this production-oriented hypothetical application, I would use:

**Pinecone**

---

# Why Pinecone?

## 1. Managed Vector Database

A managed service reduces the amount of infrastructure that needs to be maintained manually.

---

## 2. Scalability

The system can be designed to support a growing number of documents and vectors.

---

## 3. Metadata Filtering

Metadata can be stored along with vectors.

Example:

```json
{
  "document_id": "leave_policy",
  "department": "HR",
  "document_type": "policy",
  "version": "2026",
  "chunk_id": "leave_07"
}
```

This can be useful when retrieval needs to be restricted.

For example:

```text
department = HR
document_type = policy
version = 2026
```

---

## 4. Semantic Search

Pinecone can be used to perform similarity search over embeddings.

---

## 5. Practical Experience

I have used Pinecone in my Resume ATS Assistant project for semantic matching between resumes and job descriptions.

---

# Alternative Vector Databases

## ChromaDB

ChromaDB is useful for:

- Local development
- Prototyping
- Smaller RAG applications

I have used ChromaDB in my AI Refund Assistant project.

---

## FAISS

FAISS is a similarity-search library that can be used for efficient vector search.

It is useful for custom or local retrieval systems.

---

## Weaviate

Weaviate is an open-source vector database that supports semantic search and metadata-based retrieval.

---

# Vector Database Design Considerations

When implementing a production RAG system, I would consider:

### Chunking

The documents should be divided into meaningful chunks.

Poor chunking can reduce retrieval quality.

---

### Chunk Size

Very small chunks may lose context.

Very large chunks may contain too much unrelated information.

---

### Chunk Overlap

A small overlap between chunks can prevent important information from being split across boundaries.

---

### Embedding Model

The embedding model determines how text is represented in vector space.

The model should be selected based on:

- Domain
- Language
- Accuracy
- Latency
- Cost

---

### Similarity Metric

Common similarity metrics include:

- Cosine similarity
- Euclidean distance
- Dot product

---

### Top-K Retrieval

The system needs to determine how many relevant chunks should be retrieved.

For example:

```text
top_k = 5
```

means the system retrieves the five most relevant chunks.

---

### Metadata Filtering

Metadata can improve retrieval by narrowing the search space.

---

### Reranking

A reranker can reorder retrieved documents based on their relevance to the query.

---

### Evaluation

Retrieval quality should be evaluated independently from the final LLM response.

Useful evaluation considerations include:

- Retrieval relevance
- Precision
- Recall
- Context quality
- Answer correctness

---

# Complex Python Project

# AI Research Agent

The AI Research Agent is the most complex Python / Generative AI project included in this submission.

---

# Problem Statement

The goal of the project is to build an AI agent that can:

1. Accept a research topic.
2. Generate research questions.
3. Search the web.
4. Collect information.
5. Summarize findings.
6. Evaluate whether the collected information is sufficient.
7. Perform additional research when necessary.
8. Generate a final research report.

---

# AI Research Agent Architecture

```text
                 User Topic
                     │
                     ▼
               ┌───────────┐
               │  Planner  │
               └─────┬─────┘
                     │
                     ▼
               ┌───────────┐
               │ Researcher│
               └─────┬─────┘
                     │
                     ▼
               ┌───────────┐
               │ Summarizer│
               └─────┬─────┘
                     │
                     ▼
               ┌───────────┐
               │ Evaluator │
               └─────┬─────┘
                     │
                Sufficient?
                 /       \
               No         Yes
               │           │
               ▼           ▼
          Research       Final
            Again        Report
```

---

# Agent Workflow

## Planner

The Planner receives the user's topic.

Example:

```text
Topic:
Impact of Generative AI in Software Development
```

The Planner generates focused research questions.

For example:

```text
- How is GenAI used in software development?
- What productivity benefits are reported?
- What are the risks?
- What impact does it have on code quality?
- What are the challenges of adoption?
```

---

# Researcher

The Researcher performs web searches for the generated questions.

The project uses a web-search tool to collect external information.

---

# Summarizer

The collected search results are summarized into concise findings.

This reduces the amount of raw information that needs to be passed to later stages.

---

# Evaluator

The Evaluator checks whether the collected research is sufficient.

For example:

```text
Research complete:
False
```

may indicate that more evidence is required.

The evaluator can identify missing areas such as:

```text
More evidence required regarding:
- Productivity
- Code quality
- Time-to-market
```

---

# Conditional Loop

If the research is insufficient:

```text
Evaluator
    ↓
Research incomplete
    ↓
Researcher
    ↓
Additional research
```

If sufficient:

```text
Evaluator
    ↓
Research complete
    ↓
Final Report
```

---

# Preventing Infinite Loops

The workflow uses a maximum research iteration limit.

Conceptually:

```python
MAX_RESEARCH_ITERATIONS = 5
```

This prevents the agent from continuously performing research.

The workflow can therefore terminate after a maximum number of iterations even if the evaluator continues requesting more information.

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| LangGraph | Agent workflow orchestration |
| LangChain | LLM application framework |
| Groq | LLM inference |
| DuckDuckGo Search | Web research |
| Pydantic | Structured output validation |
| Streamlit | User interface |

---

# Why LangGraph?

LangGraph is useful for this project because the workflow is not simply:

```text
Input → LLM → Output
```

Instead, it contains multiple stages and conditional execution:

```text
Planner
   ↓
Researcher
   ↓
Summarizer
   ↓
Evaluator
   ↓
Conditional Routing
   ↓
Research Again / Final Report
```

LangGraph makes it easier to explicitly represent these states and transitions.

---

# Why This Is an Agentic Workflow

The system does more than generate a single response.

It:

- Plans
- Uses tools
- Performs research
- Evaluates results
- Makes a routing decision
- Iterates when required
- Produces a final output

This makes it an agentic workflow rather than a simple chatbot.

---

# Project Link

Replace this placeholder with the actual repository:

```text
AI Research Agent GitHub:
PASTE YOUR AI RESEARCH AGENT GITHUB LINK HERE
```

---

# Complex Database Project

# Resume ATS Assistant

The Resume ATS Assistant is the most complex database-related project included in this submission.

---

# Problem Statement

Recruiters may need to evaluate a large number of resumes against a job description.

Traditional keyword matching can fail when candidates use different words to describe similar skills.

The Resume ATS Assistant uses semantic matching to identify relevant resumes.

---

# Recruiter Mode Workflow

```text
             Job Description
                    │
                    ▼
              Text Processing
                    │
                    ▼
               Embedding
                    │
                    ▼
              Query Vector
                    │
                    ▼
             Pinecone Search
                    ▲
                    │
                    │
              Resume Vectors
                    ▲
                    │
                 Resumes
```

---

# Resume Processing

A resume is processed into text.

The relevant content can include:

- Skills
- Experience
- Projects
- Education
- Technologies

The processed content is converted into embeddings.

---

# Vector Storage

The embedding representation is stored in Pinecone.

Conceptually:

```text
Resume
   ↓
Text
   ↓
Embedding Model
   ↓
Vector
   ↓
Pinecone
```

Metadata can also be associated with the vector.

Example:

```json
{
  "resume_id": "resume_001",
  "candidate": "Candidate A",
  "document_type": "resume"
}
```

---

# Job Description Matching

The job description is also converted into an embedding.

```text
Job Description
      ↓
Embedding Model
      ↓
Query Vector
      ↓
Pinecone
      ↓
Similarity Search
      ↓
Relevant Resumes
```

---

# Why Vector Search?

Consider a job description containing:

```text
Natural Language Processing
Large Language Models
Retrieval-Augmented Generation
```

A candidate resume may contain:

```text
Built applications using language models,
text processing and retrieval-based AI systems.
```

Keyword matching may not capture the full semantic relationship.

Vector embeddings allow the system to compare the meaning of the content.

---

# Technologies

- Python
- Embeddings
- Pinecone
- Semantic Search
- Generative AI
- Streamlit

---

# Project Link

Replace the placeholder with the actual repository:

```text
Resume ATS Assistant GitHub:
PASTE YOUR RESUME ATS ASSISTANT GITHUB LINK HERE
```

---

# Technologies Used

| Technology | Usage |
|---|---|
| Python | Application development |
| Requests | HTTP/API communication |
| SQLite | Relational database |
| CSV | Data input |
| Matplotlib | Visualization |
| LangChain | LLM application development |
| LangGraph | Agent workflow |
| Groq | LLM inference |
| Pinecone | Vector database |
| ChromaDB | Vector database |
| Pydantic | Data validation |
| Streamlit | Application interface |

---

# Error Handling

The implementation includes error handling at important points.

---

## API Errors

The API-based applications handle:

```python
requests.RequestException
```

This covers errors such as:

- Connection failures
- Timeout
- HTTP errors
- Network-related problems

---

## SQLite Errors

Database operations handle:

```python
sqlite3.Error
```

This prevents database failures from crashing the application without a useful message.

---

## Duplicate Records

The CSV-to-SQLite implementation handles:

```python
sqlite3.IntegrityError
```

This is especially useful for duplicate email addresses.

---

## Invalid Input

The CSV implementation validates:

- Required columns
- Empty names
- Empty emails

The student-score application validates the availability and type of score values before performing calculations.

---

# Security and Good Practices

## Parameterized SQL

Instead of:

```python
query = f"INSERT INTO users VALUES ('{name}', '{email}')"
```

the implementation uses:

```python
connection.execute(
    "INSERT INTO users (name, email) VALUES (?, ?)",
    (name, email)
)
```

This helps prevent SQL injection.

---

# API Timeout

API requests use a timeout.

Example:

```python
requests.get(
    API_URL,
    timeout=10
)
```

This prevents the program from waiting forever for an unavailable API.

---

# Input Validation

External data should not be blindly trusted.

The implementation checks for:

- Missing fields
- Empty values
- Unexpected data structures
- Invalid numeric values

---

# Database Constraints

The database uses constraints such as:

```sql
PRIMARY KEY
NOT NULL
UNIQUE
```

These constraints help maintain data integrity.

---

# Installation

## Prerequisites

Make sure Python 3.9+ is installed.

Check the version:

```bash
python --version
```

---

# Create Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

The main dependencies are:

```text
requests
matplotlib
```

Python's built-in modules such as:

```text
sqlite3
csv
```

do not need to be installed separately.

---

# How to Run

## Assignment 1 — Task 1

```bash
python assignment_1/01_api_books/api_books.py
```

---

## Assignment 1 — Task 2

```bash
python assignment_1/02_student_scores/student_scores.py
```

---

## Assignment 1 — Task 3

```bash
python assignment_1/03_csv_to_sqlite/csv_to_sqlite.py
```

---

# Generated Files

Running the programs may create local files such as:

```text
books.db
users.db
student_average_scores.png
```

These generated files are excluded from Git using `.gitignore`.

---

# `.gitignore`

The repository ignores generated files such as:

```text
__pycache__/
*.pyc
*.db
*.sqlite
*.sqlite3
student_average_scores.png
venv/
.env
```

This keeps the GitHub repository clean and prevents local database files from being committed unnecessarily.

---

# Design Decisions

## Why SQLite?

SQLite was selected because the assignment uses relatively small datasets.

Advantages:

- Lightweight
- Serverless
- Easy to configure
- SQL support
- Built into Python
- Suitable for local applications and prototypes

For a large production system, a server-based relational database such as PostgreSQL could be considered.

---

# Why REST API?

A REST API provides a standard way to retrieve external data.

The implementation demonstrates:

```text
HTTP Request
    ↓
JSON Response
    ↓
Python Processing
```

This is a common pattern in real-world applications.

---

# Why JSON?

JSON is commonly used for communication between web services and applications.

Python can easily convert JSON responses into dictionaries and lists for processing.

---

# Why Parameterized SQL?

Parameterized SQL improves security and separates data from SQL instructions.

Example:

```python
cursor.execute(
    "INSERT INTO users (name, email) VALUES (?, ?)",
    (name, email)
)
```

---

# Why Matplotlib?

Matplotlib is a standard Python visualization library.

It is sufficient for creating the required student-score bar chart without introducing unnecessary dependencies.

---

# Why RAG Instead of Fine-Tuning?

RAG is useful when the application needs access to external or changing knowledge.

For example:

```text
Company Policy
     ↓
Updated Document
     ↓
Re-index Document
     ↓
RAG System
     ↓
New Answer
```

The LLM does not need to be retrained every time a policy changes.

Fine-tuning is more suitable for adapting model behavior, style or specialized task patterns rather than simply injecting frequently changing factual knowledge.

---

# Why a Vector Database?

A vector database allows the application to search based on semantic similarity.

Instead of asking:

```text
Does this document contain the exact keyword?
```

the system can ask:

```text
Is this document semantically related to the query?
```

This is especially useful for:

- RAG
- Semantic search
- Recommendation systems
- Resume matching
- Knowledge assistants

---

# Retrieval Quality

A RAG system's quality depends on multiple components.

```text
Document Quality
      ↓
Chunking Strategy
      ↓
Embedding Model
      ↓
Retrieval
      ↓
Reranking
      ↓
Context Selection
      ↓
Prompt
      ↓
LLM
      ↓
Answer
```

A powerful LLM cannot completely compensate for poor retrieval.

---

# Testing Approach

The implementations can be tested using:

## Task 1

Verify that:

- API request succeeds.
- JSON response is processed.
- Database is created.
- `books` table is created.
- Records are inserted.
- Records are displayed.

---

## Task 2

Verify that:

- API data is retrieved.
- Scores are correctly processed.
- Student averages are correct.
- Overall average is calculated.
- Chart is generated.

---

## Task 3

Verify that:

- CSV file is read correctly.
- Required columns are detected.
- Users are inserted.
- Duplicate emails are handled.
- Records are displayed.

---

# Example Test Cases

## Empty Name

Input:

```csv
name,email
,example@example.com
```

Expected behavior:

```text
Record skipped or rejected because name is empty.
```

---

## Empty Email

Input:

```csv
name,email
John,
```

Expected behavior:

```text
Record skipped or rejected because email is empty.
```

---

## Duplicate Email

Input:

```csv
name,email
John,john@example.com
Jane,john@example.com
```

Expected behavior:

```text
First record inserted.
Second record rejected because email is already present.
```

---

# Future Improvements

The current implementation is intentionally kept focused on the assignment requirements.

Possible future improvements include:

## API Layer

- Retry logic
- Exponential backoff
- Better API logging
- Configuration through environment variables
- Unit tests
- API response caching

---

## Database

- PostgreSQL for production-scale applications
- Database migrations
- Connection pooling
- Better indexing
- Repository pattern

---

## Student Analytics

Possible improvements:

- Multiple chart types
- Subject-wise comparison
- Grade classification
- Statistical analysis
- Interactive dashboards

---

## RAG System

Possible improvements:

- Hybrid search
- Reranking
- Query rewriting
- Metadata filtering
- Better chunking
- Retrieval evaluation
- Citation generation
- Document versioning
- Automated evaluation

---

## AI Research Agent

Possible improvements:

- Better source ranking
- Source credibility evaluation
- Parallel research agents
- More robust tool calling
- Research caching
- Citation tracking
- Persistent research history
- Better evaluator metrics
- Cost and token monitoring

---

## Resume ATS Assistant

Possible improvements:

- Hybrid keyword + semantic search
- Resume section-level embeddings
- Reranking
- Skill extraction
- Job-specific scoring
- Recruiter dashboard
- Candidate comparison
- Explainable matching

---

# Project Comparison

| Project | Main Problem | Main AI / Data Technique |
|---|---|---|
| API Books | Retrieve and store book data | REST API + SQLite |
| Student Scores | Calculate and visualize scores | JSON + Matplotlib |
| CSV Users | Store CSV records | CSV + SQLite |
| AI Research Agent | Automated research | Agentic AI + LangGraph |
| Resume ATS Assistant | Resume/JD matching | Embeddings + Pinecone |

---

# Key Learning Outcomes

Through these implementations, I demonstrated practical understanding of:

### Python

- Functions
- Loops
- Lists
- Dictionaries
- Exception handling
- File handling
- Modules
- API integration

### Databases

- SQLite
- SQL
- Table creation
- Constraints
- INSERT
- SELECT
- Parameterized queries
- Data integrity

### APIs

- HTTP GET
- Query parameters
- JSON
- Status-code handling
- Request timeouts
- API error handling

### Data Processing

- CSV
- JSON
- Numerical calculations
- Data validation

### Visualization

- Matplotlib
- Bar charts
- Saving charts as files

### Generative AI

- LLMs
- Prompt engineering
- RAG
- Embeddings
- Vector databases
- Semantic search
- Structured outputs

### Agentic AI

- LangGraph
- Workflow orchestration
- Conditional routing
- Iterative research
- Tool usage
- Evaluation loops

---

# Submission Checklist

Before submitting the repository, verify the following:

- [x] Assignment 1 Task 1 implemented
- [x] Assignment 1 Task 2 implemented
- [x] Assignment 1 Task 3 implemented
- [x] SQLite database operations implemented
- [x] REST API integration implemented
- [x] CSV processing implemented
- [x] Matplotlib visualization implemented
- [x] Error handling added
- [x] Parameterized SQL queries used
- [x] Assignment 2 answers included
- [x] LLM architecture explained
- [x] RAG architecture explained
- [x] Vector database explained
- [x] Vector database selection explained
- [x] Complex Python project documented
- [x] Complex database project documented
- [x] Installation instructions included
- [x] Execution instructions included
- [x] Future improvements included

---

# Important: Replace Project Links

Before submitting, replace the following placeholders.

## AI Research Agent

```text
PASTE YOUR AI RESEARCH AGENT GITHUB LINK HERE
```

Replace with the actual GitHub repository URL.

---

## Resume ATS Assistant

```text
PASTE YOUR RESUME ATS ASSISTANT GITHUB LINK HERE
```

Replace with the actual GitHub repository URL.

---

## Main Assignment Repository

Replace:

```text
YOUR_GITHUB_REPOSITORY_URL
```

with the URL of this assignment repository.

---

# Final Summary

This repository demonstrates an end-to-end understanding of both traditional Python/database development and modern AI/Generative AI application development.

The first part demonstrates practical programming skills through:

```text
REST API
   ↓
JSON
   ↓
Python
   ↓
SQLite
```

and:

```text
CSV
   ↓
Python
   ↓
Validation
   ↓
SQLite
```

as well as:

```text
Student Data
   ↓
Processing
   ↓
Average Calculation
   ↓
Matplotlib
```

The AI/ML section demonstrates understanding of:

```text
LLM
 ↓
Prompt
 ↓
RAG
 ↓
Embeddings
 ↓
Vector Database
 ↓
Semantic Search
```

The project section further demonstrates practical experience with:

```text
LangGraph
    ↓
Planner
    ↓
Researcher
    ↓
Summarizer
    ↓
Evaluator
    ↓
Final Report
```

and:

```text
Resume
   ↓
Embeddings
   ↓
Pinecone
   ↑
   │
Job Description
   ↓
Semantic Matching
```

Overall, the repository combines Python programming, databases, APIs, data processing, visualization, Generative AI, RAG, vector search and agentic workflows in a single submission.

---

# Author

**AI/ML Engineer Candidate**

This repository was created as part of an AI/ML Engineer technical assignment.
