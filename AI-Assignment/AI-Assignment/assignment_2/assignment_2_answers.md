# Assignment 2 — LLM / AI / ML / Vector Database

## 1. Self-rating: LLM, Deep Learning, AI and ML

I would rate myself based on my current practical experience as follows:

| Area | Rating | Explanation |
|---|---|---|
| LLM / Generative AI | A | I can independently build LLM-based applications. I have practical experience with prompt engineering, LangChain, RAG, embeddings, vector databases, structured outputs and LangGraph-based workflows. |
| AI / ML | B | I understand the core ML concepts required for practical AI applications, including supervised learning, regression/classification, evaluation metrics, overfitting and basic model selection. I am continuing to strengthen my ML depth. |
| Deep Learning | C | I have basic theoretical exposure to deep learning and understand concepts such as neural networks, layers, activation functions, loss functions and backpropagation, but I have limited independent deep-learning implementation experience. |

I prefer to rate myself based on what I can demonstrate practically rather
than overstate my expertise. My strongest area currently is LLM/Generative AI,
while I am continuing to build deeper knowledge in ML and Deep Learning.

---

## 2. High-level architecture of an LLM-based chatbot

An LLM chatbot can be designed as a pipeline that receives a user message,
manages conversation context, optionally retrieves external knowledge, sends
the required context to an LLM, and returns a validated response.

### High-level architecture

```text
                     ┌─────────────────┐
                     │      User       │
                     └────────┬────────┘
                              │
                              ▼
                     ┌─────────────────┐
                     │ Chat UI / API   │
                     └────────┬────────┘
                              │
                              ▼
                     ┌─────────────────┐
                     │ Input Handling  │
                     │ + Validation    │
                     └────────┬────────┘
                              │
                ┌─────────────┴─────────────┐
                │                           │
                ▼                           ▼
         Conversation                Knowledge Retrieval
            History                    (optional RAG)
                │                           │
                └─────────────┬─────────────┘
                              ▼
                     ┌─────────────────┐
                     │ Prompt Builder  │
                     └────────┬────────┘
                              │
                              ▼
                     ┌─────────────────┐
                     │      LLM        │
                     └────────┬────────┘
                              │
                              ▼
                     ┌─────────────────┐
                     │ Output Handling │
                     │ / Guardrails    │
                     └────────┬────────┘
                              │
                              ▼
                     ┌─────────────────┐
                     │      User       │
                     └─────────────────┘
```

### Main components

**1. User interface / API**

The user can interact through a web interface, mobile application or REST
API. The application receives the user's message and sends it to the backend.

**2. Input processing**

The system validates the input, applies basic safety or formatting rules,
and can classify the request if different workflows are required.

**3. Conversation memory**

A chatbot normally needs conversation history so that follow-up questions
can be understood. For long conversations, the application can summarize
older messages instead of continuously sending the complete history.

**4. Knowledge retrieval**

If the chatbot needs information from private or frequently changing
documents, a RAG pipeline can be added. Documents are split into chunks,
converted into embeddings and stored in a vector database. At query time,
relevant chunks are retrieved and provided to the LLM as context.

**5. Prompt construction**

The system combines the system instructions, relevant conversation history,
retrieved context and the current user query into a prompt.

**6. LLM**

The language model uses the supplied instructions and context to generate
the response.

**7. Output validation / guardrails**

The response can be checked for format, prohibited content, missing fields,
unsupported claims or application-specific business rules before it reaches
the user.

### RAG chatbot flow

```text
Documents
    ↓
Chunking
    ↓
Embedding Model
    ↓
Vector Database
    ↑
    │
User Query
    ↓
Query Embedding
    ↓
Similarity Search
    ↓
Relevant Chunks
    ↓
Prompt + Retrieved Context
    ↓
LLM
    ↓
Answer
```

RAG is useful when the chatbot must answer from a controlled knowledge base
without retraining the language model every time the source documents change.

---

## 3. Vector databases — explanation and selection

### What is a vector database?

A vector database is a data system designed to store and retrieve numerical
vector representations called embeddings.

An embedding model converts text into a vector:

```text
"How can I return a product?"
              ↓
         Embedding Model
              ↓
   [0.12, -0.41, 0.73, ...]
```

Texts with similar semantic meaning tend to have vectors that are close
according to a chosen similarity or distance measure.

A vector database allows an application to perform similarity search and
retrieve the most relevant stored vectors.

### Hypothetical problem

Suppose I need to build an **enterprise HR knowledge assistant**.

The company has thousands of documents:

- HR policies
- Leave policies
- Benefits documents
- Employee handbooks
- Travel policies
- Payroll FAQs

Employees should be able to ask questions such as:

> "How many days of parental leave are available?"

A keyword-only search may fail when the wording in the question differs
from the wording in the document. Semantic vector search can retrieve
documents based on meaning.

### Proposed architecture

```text
HR Documents
     ↓
Document Loading
     ↓
Text Chunking
     ↓
Embedding Model
     ↓
Pinecone Vector Database
     ↑
     │
Employee Question
     ↓
Query Embedding
     ↓
Similarity Search
     ↓
Relevant HR Chunks
     ↓
Prompt + Context
     ↓
LLM
     ↓
Answer
```

### Vector database I would choose

For this hypothetical production application, I would choose **Pinecone**.

The main reasons are:

1. **Managed service** — the application does not need to operate the
   underlying vector-search infrastructure itself.
2. **Scalability** — it is designed for vector-search workloads that can
   grow as the document collection grows.
3. **Metadata filtering** — metadata such as department, document type,
   region and policy version can be associated with vectors and used to
   narrow retrieval.
4. **Semantic retrieval** — it provides the core similarity-search capability
   required for a RAG pipeline.
5. **Practical experience** — I have used Pinecone in my Resume ATS Assistant
   project for semantic resume/JD matching, so I can explain the integration
   from practical experience.

### Example metadata

```json
{
  "document_id": "leave_policy_2026",
  "department": "HR",
  "document_type": "policy",
  "version": "2026.1",
  "chunk_id": "leave_policy_2026_07"
}
```

Metadata filtering can help ensure that retrieval uses the appropriate
documents instead of searching every stored chunk indiscriminately.

### Alternatives

**ChromaDB:** Simple and convenient for local development and prototypes.
I have used ChromaDB in my AI Refund Assistant project.

**FAISS:** A strong library for efficient vector similarity search, especially
when building a custom/local retrieval system. It is a library rather than
a fully managed database service.

**Weaviate:** An open-source vector database with capabilities for semantic
search and metadata-aware retrieval.

The final choice depends on requirements such as scale, deployment model,
operational ownership, filtering needs, latency, cost and existing
infrastructure.

### Important considerations when designing vector search

I would also evaluate:

- Chunk size and overlap
- Embedding model quality
- Similarity metric
- Top-k retrieval
- Metadata filtering
- Hybrid search when keyword matching is important
- Reranking for improving retrieved-context relevance
- Document/version management
- Retrieval evaluation
- Latency and cost

A vector database is therefore only one component of a RAG system. Good
retrieval also depends on document preprocessing, chunking, embeddings,
query construction and evaluation.
