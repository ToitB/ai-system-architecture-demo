# AI System Architecture Demo

## How to Discuss This Repository in Interviews

- This repository demonstrates how I design AI-enabled systems with clear separation between API, orchestration, inference, and storage layers.
- The focus is on architecture, boundaries, and operational constraints rather than model training or optimisation.
- AI inference is intentionally mocked; production inference logic is private, but the architectural patterns are the same.


## ⚠️ IMPORTANT DISCLAIMER

**This is a REFERENCE ARCHITECTURE and EDUCATIONAL DEMO ONLY.**

This project demonstrates a minimal, skeletal architecture for AI-powered document processing systems. It is intentionally incomplete and NOT suitable for production use.

### What This Demo Includes

- Basic FastAPI application structure
- Simple orchestration pattern for handling requests
- Mock inference adapter (no real AI/ML logic)
- In-memory storage simulation
- Clean separation of concerns between layers

### What This Demo DOES NOT Include

- ❌ Real AI/ML models or inference logic
- ❌ Domain-specific business logic or workflows
- ❌ Optimized prompts or production-ready AI strategies
- ❌ Proprietary processing pipelines
- ❌ Authentication, authorization, or security features
- ❌ Production-ready error handling or logging
- ❌ Database integration or persistent storage
- ❌ Performance optimizations
- ❌ Comprehensive testing

## Architecture Overview

This demo illustrates a three-tier architecture:

```
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

See [architecture/system-overview.md](architecture/system-overview.md) for more details.

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
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r backend/requirements.txt
```

### Running the Demo

```bash
# From the project root
cd backend
uvicorn app:app --reload
```

The API will be available at `http://localhost:8000`

API documentation (Swagger UI): `http://localhost:8000/docs`

### Example Request

```bash
curl -X POST "http://localhost:8000/api/process" \
  -H "Content-Type: application/json" \
  -d '{"document_text": "Sample document content", "task_type": "analysis"}'
```

## Project Structure

```
ai-system-architecture-demo/
├── README.md                          # This file
├── LICENSE                            # MIT License
├── architecture/
│   └── system-overview.md             # Detailed architecture notes
├── backend/
│   ├── app.py                         # FastAPI application entry point
│   ├── requirements.txt               # Python dependencies
│   └── services/
│       ├── orchestrator.py            # Request coordination logic
│       ├── inference_adapter.py       # Mock AI inference interface
│       └── storage.py                 # Mock storage interface
└── sample_data/
    └── example_documents.txt          # Sample inputs for testing
```

## Design Principles Demonstrated

1. **Separation of Concerns**: API layer, business logic, and external services are clearly separated
2. **Dependency Injection**: Services are loosely coupled and easily mockable
3. **Interface-based Design**: Abstract interfaces for external dependencies
4. **Stateless API**: Each request is independent
5. **Simple Error Handling**: Basic error responses (not production-ready)

## Use Cases for This Demo

- Understanding basic AI application architecture
- Learning FastAPI patterns
- Exploring service layer design
- Educational purposes and technical discussions
- Starting point for experimentation (requires significant extension)

## License

MIT License - See [LICENSE](LICENSE) file for details.

## Contributing

This is a reference demo and not actively maintained. Feel free to fork and adapt for your own learning purposes.

---

**Remember**: This is a skeleton architecture only. Real-world AI applications require significant additional work including security, monitoring, testing, optimization, and domain-specific logic.
