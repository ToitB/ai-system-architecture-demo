"""
AI System Architecture Demo - FastAPI Application

This is a minimal, educational demo showing a basic FastAPI application structure
for AI-powered document processing. 

IMPORTANT: This contains NO real AI logic - all inference is mocked.
This is NOT production-ready and lacks security, error handling, and optimizations.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, Any
import uvicorn

# Import our service layer
from services.orchestrator import Orchestrator
from services.inference_adapter import InferenceAdapter
from services.storage import Storage


# ============================================================================
# DATA MODELS
# ============================================================================

class ProcessRequest(BaseModel):
    """
    Request model for document processing.
    
    In a real system, this would have:
    - Authentication tokens
    - User/tenant identifiers
    - More sophisticated document metadata
    - Validation rules
    """
    document_text: str
    task_type: str = "analysis"  # Could be: analysis, summarization, classification, etc.
    options: Optional[Dict[str, Any]] = None


class ProcessResponse(BaseModel):
    """
    Response model for processed documents.
    
    In a real system, this would include:
    - Job IDs for async tracking
    - Confidence scores
    - Richer metadata
    - Links to stored artifacts
    """
    status: str
    result: Dict[str, Any]
    document_id: str


# ============================================================================
# APPLICATION SETUP
# ============================================================================

app = FastAPI(
    title="AI System Architecture Demo",
    description="Minimal reference architecture for AI-powered document processing (DEMO ONLY)",
    version="0.1.0"
)

# Initialize services (in production, use dependency injection)
storage_service = Storage()
inference_service = InferenceAdapter()
orchestrator = Orchestrator(
    inference_adapter=inference_service,
    storage=storage_service
)


# ============================================================================
# API ENDPOINTS
# ============================================================================

@app.get("/")
async def root():
    """
    Root endpoint - provides basic API information.
    """
    return {
        "service": "AI System Architecture Demo",
        "version": "0.1.0",
        "status": "running",
        "warning": "This is a demo API with mocked AI responses. Not for production use.",
        "docs": "/docs"
    }


@app.get("/api/health")
async def health_check():
    """
    Health check endpoint for monitoring/deployment systems.
    
    In production, this would check:
    - Database connectivity
    - External API availability
    - Resource utilization
    """
    return {
        "status": "healthy",
        "services": {
            "api": "operational",
            "orchestrator": "operational",
            "inference": "mocked",
            "storage": "in-memory"
        }
    }


@app.post("/api/process", response_model=ProcessResponse)
async def process_document(request: ProcessRequest):
    """
    Main processing endpoint.
    
    Accepts a document and task type, orchestrates processing,
    and returns results.
    
    Args:
        request: ProcessRequest containing document_text and task_type
        
    Returns:
        ProcessResponse with status, result, and document_id
        
    Note:
        This is a synchronous endpoint. For real AI workloads,
        you would use async processing with job queues.
    """
    try:
        # Basic input validation
        if not request.document_text or len(request.document_text.strip()) == 0:
            raise HTTPException(status_code=400, detail="document_text cannot be empty")
        
        if not request.task_type:
            raise HTTPException(status_code=400, detail="task_type is required")
        
        # Delegate to orchestrator
        result = orchestrator.process_request(
            document_text=request.document_text,
            task_type=request.task_type,
            options=request.options or {}
        )
        
        return ProcessResponse(**result)
    
    except HTTPException:
        # Re-raise HTTP exceptions
        raise
    
    except Exception as e:
        # In production, log this error properly
        # Don't expose internal error details to clients
        raise HTTPException(
            status_code=500,
            detail=f"Internal processing error: {str(e)}"
        )


@app.get("/api/results/{document_id}")
async def get_result(document_id: str):
    """
    Retrieve previously processed document by ID.
    
    Args:
        document_id: Unique identifier for the document
        
    Returns:
        Stored document result
        
    Note:
        Uses in-memory storage - data is lost on restart.
    """
    try:
        result = storage_service.get_result(document_id)
        
        if result is None:
            raise HTTPException(
                status_code=404,
                detail=f"Document {document_id} not found"
            )
        
        return result
    
    except HTTPException:
        raise
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error retrieving document: {str(e)}"
        )


@app.get("/api/results")
async def list_results(limit: int = 10):
    """
    List all processed documents.
    
    Args:
        limit: Maximum number of results to return (default: 10)
        
    Returns:
        List of document IDs and basic metadata
        
    Note:
        In production, this would have:
        - Pagination
        - Filtering by user/date/status
        - Proper access control
    """
    try:
        results = storage_service.list_results(limit=limit)
        return {
            "count": len(results),
            "results": results
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error listing results: {str(e)}"
        )


# ============================================================================
# APPLICATION ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    # Run the application
    # In production, use gunicorn or similar WSGI server
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True  # Auto-reload on code changes (dev only)
    )
