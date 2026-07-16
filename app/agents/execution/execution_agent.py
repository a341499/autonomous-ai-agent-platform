"""
===========================================================================
Project     : Autonomous AI Agent Platform
Module      : execution_agent.py

Description:
    Execution Agent implementation.

Purpose:
    This module implements the Execution Agent responsible for
    executing the approved workflow.

Responsibilities:
    - Receive workflow state
    - Execute the approved workflow (future implementation)
    - Generate the final response (future implementation)
    - Return updated workflow state

Author      : Lokesh Kumar
Version     : v1.0.0
===========================================================================
"""

# ==========================================================================
# Application Imports
# ==========================================================================

# Import the Base Agent.
from app.agents.base import BaseAgent

# Import the workflow state model.
from app.models.workflow_state import WorkflowState

# Import the Memory Service.
from app.services.memory import MemoryService

# Import memory type constants.
from app.config.constants import MEMORY_TYPE_WORKFLOW

# Import UUID generation utilities.
import uuid

# ==========================================================================
# Execution Agent
# ==========================================================================

class ExecutionAgent(BaseAgent):
    """
    Execution Agent.

    Responsible for executing the approved workflow and
    producing the final response.
    """

    # ----------------------------------------------------------------------
    # Constructor
    # ----------------------------------------------------------------------

    def __init__(self) -> None:
        """
        Initialize the Execution Agent.
        """

        # Initialize the Base Agent.
        super().__init__("ExecutionAgent")

        # Create the Memory Service.
        self.memory_service = MemoryService()

    # ----------------------------------------------------------------------
    # Execute Agent
    # ----------------------------------------------------------------------

    def execute(
        self,
        workflow_state: WorkflowState,
    ) -> WorkflowState:
        """
        Execute the Execution Agent.

        Parameters
        ----------
        workflow_state : WorkflowState
            Current workflow state.

        Returns
        -------
        WorkflowState
            Updated workflow state.
        """

        # Log the start of execution.
        self.logger.info("Execution Agent execution started.")

        # ------------------------------------------------------------------
        # Future Implementation
        # ------------------------------------------------------------------
        #
        # Planned responsibilities:
        #
        # 1. Execute the approved workflow.
        # 2. Generate the final response.
        # 3. Update the workflow state.
        # 4. Return the completed workflow.
        #
        # ------------------------------------------------------------------

        # Build the prompt for the language model.
        prompt = (
            "You are the Execution Agent.\n\n"
            f"User Request:\n{workflow_state.user_request}\n\n"
            f"Knowledge:\n{workflow_state.knowledge}\n\n"
            f"Execution Plan:\n{workflow_state.plan}\n\n"
            f"Research:\n{workflow_state.research}\n\n"
            f"Review:\n{workflow_state.review}\n\n"
            "Generate the final execution summary.\n"
            "Limit the response to a maximum of 20 words.\n"
            "Return plain text only."
        )

        # Invoke the shared language model helper.
        workflow_state.execution_result = (
            self.invoke_llm(
                prompt,
            )
        )

        # Log the execution result.
        self.logger.info(
            "Execution Result : %s",
            workflow_state.execution_result,
        )

        # Store the final workflow response.
        workflow_state.final_response = (
            workflow_state.execution_result
        )

        # Build the workflow summary.
        workflow_summary = (
            f"User Request: {workflow_state.user_request}\n"
            f"Knowledge: {workflow_state.knowledge}\n"
            f"Plan: {workflow_state.plan}\n"
            f"Research: {workflow_state.research}\n"
            f"Review: {workflow_state.review}\n"
            f"Execution Result: {workflow_state.execution_result}"
        )

        # Store the completed workflow.
        self.memory_service.store_memory(
            memory_id=str(uuid.uuid4()),
            memory_text=workflow_summary,
            memory_type=MEMORY_TYPE_WORKFLOW,
        )

        # Log successful workflow storage.
        self.logger.info(
            "Workflow summary stored successfully.",
        )

        # Log successful completion.
        self.logger.info("Execution Agent execution completed.")

        # Return the workflow state unchanged.
        return workflow_state


# ==========================================================================
# End of File
# ==========================================================================