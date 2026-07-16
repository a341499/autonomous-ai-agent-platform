"""
===========================================================================
Project     : Autonomous AI Agent Platform
Module      : memory_service.py

Description:
    Memory service.

Purpose:
    Provides a centralized interface for interacting with
    the application's persistent memory.

Responsibilities:
    - Initialize memory backend
    - Store memories
    - Retrieve memories
    - Manage memory collections

Author      : Lokesh Kumar
Version     : v1.0.0
===========================================================================
"""

# ==========================================================================
# Third-Party Imports
# ==========================================================================

# Import the ChromaDB client.
import chromadb

# ==========================================================================
# Application Imports
# ==========================================================================

# Import the centralized logger factory.
from app.utils import get_logger

# Import the application settings.
from app.config import settings

# ==========================================================================
# Memory Service
# ==========================================================================

class MemoryService:
    """
    Service responsible for interacting with
    the application's persistent memory.
    """

    def __init__(
        self,
    ) -> None:
        """
        Initialize the Memory Service.
        """

        # Create the service logger.
        self.logger = get_logger(
            "MemoryService",
        )

        # Create the ChromaDB persistent client.
        self.client = chromadb.PersistentClient(
            path=settings.CHROMA_DB_PATH,
        )

        # Create or open the agent memory collection.
        self.collection = self.client.get_or_create_collection(
            name="agent_memory",
        )

        # Log successful initialization.
        self.logger.info(
            "MemoryService initialized successfully.",
        )

    # ----------------------------------------------------------------------
    # Store Memory
    # ----------------------------------------------------------------------

    # ----------------------------------------------------------------------
    # Store Memory
    # ----------------------------------------------------------------------

    def store_memory(
        self,
        memory_id: str,
        memory_text: str,
        memory_type: str,
    ) -> None:
        """
        Store a memory in the ChromaDB collection.

        Parameters
        ----------
        memory_id : str
            Unique identifier for the memory.

        memory_text : str
            Memory content to be stored.

        memory_type : str
            Classification of the memory.

        Returns
        -------
        None
        """

        # Log the memory storage operation.
        self.logger.info(
            "Storing %s memory: %s",
            memory_type,
            memory_id,
        )

        # Store the memory in the collection.
        self.collection.add(
            ids=[
                memory_id,
            ],
            documents=[
                memory_text,
            ],
            metadatas=[
                {
                    "memory_type": memory_type,
                },
            ],
        )

        # Log successful completion.
        self.logger.info(
            "Memory stored successfully.",
        )

    # ----------------------------------------------------------------------
    # Retrieve Memory
    # ----------------------------------------------------------------------

    def retrieve_memory(
        self,
        query_text: str,
        n_results: int = 1,
    ) -> list[str]:
        """
        Retrieve workflow memories from the ChromaDB collection.

        Parameters
        ----------
        query_text : str
            Search query.

        n_results : int
            Maximum number of memories to retrieve.

        Returns
        -------
        list[str]
            Matching workflow memory documents.
        """

        # Log the retrieval request.
        self.logger.info(
            "Retrieving workflow memories for: %s",
            query_text,
        )

        # Query the workflow memories.
        results = self.collection.query(
            query_texts=[
                query_text,
            ],
            n_results=n_results,
            where={
                "memory_type": "workflow",
            },
        )

        # Log successful retrieval.
        self.logger.info(
            "Workflow memory retrieval completed.",
        )

        # Return the matching workflow documents.
        return results.get(
            "documents",
            [[]],
        )[0]

# ==========================================================================
# End of File
# ==========================================================================