"""
===========================================================================
Project     : Autonomous AI Agent Platform
Module      : knowledge_agent.py

Description:
    Knowledge Agent implementation.

Purpose:
    This module implements the Knowledge Agent responsible for
    retrieving enterprise knowledge.

Responsibilities:
    - Receive workflow state
    - Execute knowledge retrieval workflow
    - Return updated workflow state

Author      : Lokesh Kumar
Version     : v1.0.0
===========================================================================
"""

# ==========================================================================
# Application Imports
# ==========================================================================

# Import the base agent implementation.
from app.agents.base import BaseAgent

# Import the workflow state model.
from app.models.workflow_state import WorkflowState

# Import the Memory Service.
from app.services.memory import MemoryService

# ==========================================================================
# Knowledge Agent
# ==========================================================================

class KnowledgeAgent(BaseAgent):
    """
    Enterprise Knowledge Agent.

    Responsible for retrieving relevant enterprise knowledge
    for a workflow.
    """

    # ----------------------------------------------------------------------
    # Constructor
    # ----------------------------------------------------------------------

    def __init__(self) -> None:
        """
        Initialize the Knowledge Agent.
        """

        # Initialize the parent BaseAgent.
        super().__init__("KnowledgeAgent")

        # Create the Memory Service.
        self.memory_service = MemoryService()

    # ----------------------------------------------------------------------
    # Execute
    # ----------------------------------------------------------------------

    def execute(
        self,
        workflow_state: WorkflowState,
    ) -> WorkflowState:
        """
        Execute the Knowledge Agent.

        Parameters
        ----------
        workflow_state : WorkflowState
            Current workflow state.

        Returns
        -------
        WorkflowState
            Updated workflow state.
        """

        # Log the beginning of execution.
        self.logger.info("Knowledge Agent execution started.")

        # ==============================================================
        # Future Implementation
        # ==============================================================
        #
        # Planned workflow:
        #
        # 1. Read the user's request.
        # 2. Generate embeddings.
        # 3. Perform semantic search.
        # 4. Retrieve relevant documents.
        # 5. Attach retrieved context to the workflow.
        # 6. Return the updated workflow state.
        #
        # ==============================================================

        # Build the prompt for the language model.
        prompt = (
            "You are the Knowledge Agent.\n\n"
            f"User Request:\n{workflow_state.user_request}\n\n"
            "Provide only the essential knowledge needed.\n"
            "Limit the response to a maximum of 20 words.\n"
            "Return plain text only."
        )

        # Retrieve relevant memories.
        retrieved_memories = self.memory_service.retrieve_memory(
            query_text=workflow_state.user_request,
            n_results=3,
        )

        # Log the retrieved memories.
        self.logger.info(
            "Retrieved Memories : %s",
            retrieved_memories,
        )

        # Invoke the shared language model helper.
        workflow_state.knowledge = (
            self.invoke_llm(
                prompt,
            )
        )

        # Log the knowledge gathered during execution.
        self.logger.info(
            "Knowledge : %s",
            workflow_state.knowledge,
        )

        # Log successful completion.
        self.logger.info("Knowledge Agent execution completed.")

        # Return the updated workflow state.
        return workflow_state

# ==========================================================================
# End of File
# ==========================================================================