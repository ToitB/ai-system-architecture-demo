"""
Storage Service

This service handles persistence of processing results.
In this demo, it uses in-memory storage (Python dictionary).

In a production system, this would:
- Use a real database (PostgreSQL, MongoDB, etc.)
- Implement connection pooling
- Handle transactions
- Provide query/search capabilities
- Implement backup/recovery
"""

from typing import Dict, Any, List, Optional
from datetime import datetime


class Storage:
    """
    In-memory storage service for document processing results.
    
    This is a minimal implementation for demonstration purposes.
    
    IMPORTANT LIMITATIONS:
    - All data is lost when the application restarts
    - No concurrent access protection
    - No query capabilities
    - No size limits or eviction policy
    - Not suitable for production use
    """
    
    def __init__(self):
        """
        Initialize in-memory storage.
        
        In production, this would:
        - Establish database connections
        - Set up connection pooling
        - Configure retry policies
        - Initialize caching layers
        """
        # Simple dictionary to store results
        # Key: document_id, Value: result dictionary
        self._store: Dict[str, Dict[str, Any]] = {}
    
    def store_result(self, document_id: str, result: Dict[str, Any]) -> bool:
        """
        Store a processing result.
        
        Args:
            document_id: Unique identifier for the document
            result: Complete result dictionary to store
            
        Returns:
            True if successful, False otherwise
            
        In production, this would:
        - Validate the data schema
        - Handle database transactions
        - Return detailed error information
        - Log storage operations
        """
        try:
            # Add storage timestamp
            result["stored_at"] = datetime.utcnow().isoformat()
            
            # Store in memory
            self._store[document_id] = result
            
            return True
        
        except Exception as e:
            # In production, log this error
            print(f"Error storing result: {e}")
            return False
    
    def get_result(self, document_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve a stored result by document ID.
        
        Args:
            document_id: Unique identifier for the document
            
        Returns:
            Result dictionary if found, None otherwise
            
        In production, this would:
        - Query the database
        - Handle connection errors
        - Implement caching
        - Log access for audit trails
        """
        return self._store.get(document_id)
    
    def list_results(self, limit: int = 10) -> List[Dict[str, Any]]:
        """
        List stored results.
        
        Args:
            limit: Maximum number of results to return
            
        Returns:
            List of result summaries
            
        In production, this would:
        - Support pagination
        - Allow filtering by user, date, status
        - Implement proper access control
        - Return only authorized results
        """
        # Get all document IDs
        all_ids = list(self._store.keys())
        
        # Limit results
        limited_ids = all_ids[:limit]
        
        # Return summary information
        results = []
        for doc_id in limited_ids:
            result = self._store[doc_id]
            results.append({
                "document_id": doc_id,
                "status": result.get("status", "unknown"),
                "timestamp": result.get("metadata", {}).get("timestamp"),
                "task_type": result.get("metadata", {}).get("task_type"),
                "stored_at": result.get("stored_at")
            })
        
        return results
    
    def delete_result(self, document_id: str) -> bool:
        """
        Delete a stored result.
        
        Args:
            document_id: Unique identifier for the document
            
        Returns:
            True if deleted, False if not found
            
        In production, this would:
        - Implement soft deletes
        - Maintain audit logs
        - Check access permissions
        - Archive data before deletion
        """
        if document_id in self._store:
            del self._store[document_id]
            return True
        return False
    
    def get_statistics(self) -> Dict[str, Any]:
        """
        Get storage statistics.
        
        Returns:
            Dictionary with storage metrics
            
        Useful for monitoring and debugging.
        """
        return {
            "total_documents": len(self._store),
            "storage_type": "in-memory",
            "warning": "All data will be lost on restart"
        }
    
    # ========================================================================
    # Methods that would exist in a production database implementation
    # ========================================================================
    
    def _create_connection(self):
        """
        Placeholder for database connection setup.
        
        NOT IMPLEMENTED - Example for PostgreSQL:
        
        import psycopg2
        self.conn = psycopg2.connect(
            host="localhost",
            database="mydb",
            user="user",
            password="password"
        )
        """
        raise NotImplementedError("Database connections not implemented in demo")
    
    def _execute_query(self, query: str, params: tuple):
        """
        Placeholder for executing database queries.
        
        NOT IMPLEMENTED - Example:
        
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
        """
        raise NotImplementedError("Database queries not implemented in demo")
