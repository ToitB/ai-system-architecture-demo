# AI System Architecture Demo

## How to Discuss This Repository in Interviews

- Demonstrates how I design AI-enabled systems with clear separation between API, orchestration, inference, and storage layers.
- Focuses on architecture, boundaries, and operational constraints rather than model training or optimisation.
- AI inference is intentionally mocked; production inference logic is private, but the architectural patterns are the same.

---

## ⚠️ IMPORTANT DISCLAIMER

This is a **REFERENCE ARCHITECTURE** and **EDUCATIONAL DEMO ONLY**.

This project demonstrates a minimal, skeletal architecture for AI-powered document processing systems. It is intentionally incomplete and **NOT suitable for production use**.

All AI processing is mocked and produces synthetic results.

---

## What This Demo Includes

- Basic FastAPI application structure
- Simple orchestration pattern for handling requests
- Mock inference adapter (no real AI/ML logic)
- In-memory storage simulation
- Clean separation of concerns between layers

---

## What This Demo Does NOT Include

- ❌ Real AI/ML models or inference logic  
- ❌ Domain-specific business logic or workflows  
- ❌ Optimized prompts or production-ready AI strategies  
- ❌ Proprietary processing pipelines  
- ❌ Authentication, authorization, or security features  
- ❌ Production-ready error handling or logging  
- ❌ Database integration or persistent storage  
- ❌ Performance optimizations  
- ❌ Comprehensive testing  

---

## Architecture Overview

This demo illustrates a simple three-tier architecture:

```text
┌─────────────┐
│   FastAPI   │  ← HTTP REST API Layer
│   (app.py)  │
└──────┬──────┘
       │
       ▼
┌─────────────────┐
│  Orchestrator   │  ← Business Logic Coordination
└──────┬──────────┘
       │
       ├──────────────┬───────────────┐
       ▼              ▼               ▼
┌──────────────┐ ┌─────────────┐ ┌──────────┐
│  Inference   │ │   Storage   │ │  Other   │
│   Adapter    │ │             │ │ Services │
└──────────────┘ └─────────────┘ └──────────┘
```

See `architecture/system-overview.md` for more detailed architectural notes.

---

## Quick Start

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate

# Linux / macOS:
source venv/bin/activate

# Install dependencies
pip install -r backend/requirements.txt
```

---

## Running the Demo

```bash
# From the project root
cd backend
uvicorn app:app --reload
```

The API will be available at:

- http://localhost:8000  
- Swagger UI: http://localhost:8000/docs

---

## Example Request

```bash
curl -X POST "http://localhost:8000/api/process" \
  -H "Content-Type: application/json" \
  -d '{"document_text": "Sample document content", "task_type": "analysis"}'
```

---

## Project Structure

```text
ai-system-architecture-demo/
├── README.md
├── LICENSE
├── architecture/
│   └── system-overview.md
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── services/
│       ├── orchestrator.py
│       ├── inference_adapter.py
│       └── storage.py
└── sample_data/
    └── example_documents.txt
```

---

## Design Principles Demonstrated

- **Separation of Concerns** – API layer, orchestration logic, and services are isolated
- **Dependency Injection** – Services are loosely coupled and easily mockable
- **Interface-based Design** – External dependencies are abstracted
- **Stateless API** – Each request is handled independently
- **Simple Error Handling** – Demonstrative, not production-grade

---

## Use Cases for This Demo

- Understanding basic AI application architecture
- Learning FastAPI service patterns
- Exploring orchestration layer design
- Educational purposes and technical discussion
- Starting point for experimentation (requires significant extension)

---

## License

MIT License — see the `LICENSE` file for details.

---

## Contributing

This is a reference demo and is not actively maintained.  
Feel free to fork and adapt it for your own learning purposes.

> **Reminder:** This is a skeleton architecture only.  
> Real-world AI applications require additional work including security, monitoring, testing, optimisation, and domain-specific logic.
