# E-commerce AI Database Query System

An end-to-end full-stack application that enables **natural language querying of a relational database** using **FastAPI, PostgreSQL, LangChain, and Gradio**.

---

## Key Features

- CRUD APIs for 6 relational tables
- AI-powered Natural Language → SQL queries
- SQL safety filtering (no destructive queries)
- FastAPI backend with SQLAlchemy ORM
- Gradio frontend for user interaction
- Explainable SQL generation (optional debug view)

---

## Development Phases

### Phase 1 — Database & Backend
- PostgreSQL schema design
- ORM models with SQLAlchemy
- Foreign key integrity
- Seeded test data

### Phase 2 — CRUD + AI Integration
- Full CRUD APIs
- LangChain SQL Agent
- Natural language querying
- SQL validation and safety checks

### Phase 3 — Frontend
- Gradio UI
- Example prompts
- Tabular result rendering
- Error handling

---

## Getting Started

### Clone Repository
```bash
git clone https://github.com/yourusername/ecommerce-ai-db.git
cd ecommerce-ai-db
