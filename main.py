"""
===========================================================================
Project     : Autonomous AI Agent Platform
Module      : main.py

Description:
    Main application entry point.

Purpose:
    This module serves as the starting point for the Autonomous AI
    Agent Platform.

Responsibilities:
    - Initialize the application
    - Verify configuration
    - Start the application lifecycle

Author      : Lokesh Kumar
Version     : v1.0.0
===========================================================================
"""

# ==========================================================================
# Standard Library Imports
# ==========================================================================

# Import UUID generation utilities.
import uuid

# ==========================================================================
# Application Imports
# ==========================================================================

# Import the centralized application settings.
from app.config import settings

# Import the centralized logger factory.
from app.utils import get_logger

# Import the Agent Orchestrator.
from app.orchestration import AgentOrchestrator

# Import the workflow state model.
from app.models import WorkflowState

# Import the Memory Service.
from app.services.memory import MemoryService

# ==========================================================================
# Initialize Logger
# ==========================================================================

# Create the application logger.
logger = get_logger(__name__)

# ==========================================================================
# Main Function
# ==========================================================================

def main() -> None:
    """
    Start the Autonomous AI Agent Platform.

    Returns
    -------
    None
    """

    # Log application startup.
    logger.info("Starting Autonomous AI Agent Platform...")

    # Log the configured LLM model.
    logger.info("LLM Model : %s", settings.LLM_MODEL)

    # Log the configured embedding model.
    logger.info("Embedding Model : %s", settings.EMBEDDING_MODEL)

    # Log the configured ChromaDB location.
    logger.info("ChromaDB Path : %s", settings.CHROMA_DB_PATH)

    # Log successful initialization.
    logger.info("Application initialized successfully.")

    # Create the Agent Orchestrator.
    agent_orchestrator = AgentOrchestrator()

    # Log successful orchestrator creation.
    logger.info("Agent Orchestrator created successfully.")

    # Create the workflow state.
    workflow_state = WorkflowState(
        workflow_id="WF-000001",
        user_request="Test Autonomous AI Agent Platform",
    )

    # Log successful workflow state creation.
    logger.info("WorkflowState created successfully.")

    # Execute the workflow.
    workflow_state = agent_orchestrator.execute_workflow(
        workflow_state,
    )

    # Display the final workflow response.
    logger.info(
        "=" * 80
    )

    # Log the final workflow response.
    logger.info(
        "Final Response : %s",
        workflow_state.final_response,
    )

    # Display the closing separator.
    logger.info(
        "=" * 80
    )

    # Display the workflow identifier.
    logger.info(
        "Workflow ID   : %s",
        workflow_state.workflow_id,
    )

    # Display the workflow status.
    logger.info(
        "Workflow Status : %s",
        workflow_state.workflow_status,
    )

    # Display the generated knowledge.
    logger.info(
        "Knowledge        : %s",
        workflow_state.knowledge,
    )

    # Display the generated execution plan.
    logger.info(
        "Execution Plan   : %s",
        workflow_state.plan,
    )

    # Display the generated research.
    logger.info(
        "Research         : %s",
        workflow_state.research,
    )

    # Display the generated review.
    logger.info(
        "Review           : %s",
        workflow_state.review,
    )

    # Display the generated execution result.
    logger.info(
        "Execution Result : %s",
        workflow_state.execution_result,
    )

    # Display the final workflow response.
    logger.info(
        "Final Response   : %s",
        workflow_state.final_response,
    )

# ==========================================================================
# Application Entry Point
# ==========================================================================

# Execute the application only when this module is run directly.
if __name__ == "__main__":

    # Start the application.
    main()


# ==========================================================================
# End of File
# ==========================================================================