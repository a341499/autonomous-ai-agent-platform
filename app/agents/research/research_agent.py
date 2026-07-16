"""
===========================================================================
Project     : Autonomous AI Agent Platform
Module      : research_agent.py

Description:
    Research Agent implementation.

Purpose:
    This module implements the Research Agent responsible for
    performing external research to supplement enterprise knowledge.

Responsibilities:
    - Receive workflow state
    - Perform external research (future implementation)
    - Enrich workflow state
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


# ==========================================================================
# Research Agent
# ==========================================================================

class ResearchAgent(BaseAgent):
    """
    Research Agent.

    Responsible for performing external research and enriching
    the workflow with additional information.
    """

    # ----------------------------------------------------------------------
    # Constructor
    # ----------------------------------------------------------------------

    def __init__(self) -> None:
        """
        Initialize the Research Agent.
        """

        # Initialize the Base Agent.
        super().__init__("ResearchAgent")

    # ----------------------------------------------------------------------
    # Execute Agent
    # ----------------------------------------------------------------------

    def execute(
        self,
        workflow_state: WorkflowState,
    ) -> WorkflowState:
        """
        Execute the Research Agent.

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
        self.logger.info("Research Agent execution started.")

        # ------------------------------------------------------------------
        # Future Implementation
        # ------------------------------------------------------------------
        #
        # Planned responsibilities:
        #
        # 1. Analyze missing information.
        # 2. Perform external research.
        # 3. Validate research results.
        # 4. Enrich the workflow state.
        #
        # ------------------------------------------------------------------

        # Build the prompt for the language model.
        prompt = (
            "You are the Research Agent.\n\n"
            f"User Request:\n{workflow_state.user_request}\n\n"
            f"Knowledge:\n{workflow_state.knowledge}\n\n"
            f"Execution Plan:\n{workflow_state.plan}\n\n"
            "Identify additional research required.\n"
            "Limit the response to a maximum of 20 words.\n"
            "Return plain text only."
        )

        # Invoke the shared language model helper.
        workflow_state.research = (
            self.invoke_llm(
                prompt,
            )
        )

        # Log the research summary.
        self.logger.info(
            "Research : %s",
            workflow_state.research,
        )

        # Log successful completion.
        self.logger.info("Research Agent execution completed.")

        # Return the workflow state unchanged.
        return workflow_state


# ==========================================================================
# End of File
# ==========================================================================