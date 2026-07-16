"""
===========================================================================
Project     : Autonomous AI Agent Platform
Module      : reviewer_agent.py

Description:
    Reviewer Agent implementation.

Purpose:
    This module implements the Reviewer Agent responsible for
    reviewing and validating the workflow before execution.

Responsibilities:
    - Receive workflow state
    - Review workflow output (future implementation)
    - Validate execution plan (future implementation)
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
# Reviewer Agent
# ==========================================================================

class ReviewerAgent(BaseAgent):
    """
    Reviewer Agent.

    Responsible for reviewing and validating
    the workflow before execution.
    """

    # ----------------------------------------------------------------------
    # Constructor
    # ----------------------------------------------------------------------

    def __init__(self) -> None:
        """
        Initialize the Reviewer Agent.
        """

        # Initialize the Base Agent.
        super().__init__("ReviewerAgent")

    # ----------------------------------------------------------------------
    # Execute Agent
    # ----------------------------------------------------------------------

    def execute(
        self,
        workflow_state: WorkflowState,
    ) -> WorkflowState:
        """
        Execute the Reviewer Agent.

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
        self.logger.info("Reviewer Agent execution started.")

        # ------------------------------------------------------------------
        # Future Implementation
        # ------------------------------------------------------------------
        #
        # Planned responsibilities:
        #
        # 1. Review workflow output.
        # 2. Validate execution plan.
        # 3. Identify potential issues.
        # 4. Approve or reject the workflow.
        #
        # ------------------------------------------------------------------

        # Build the prompt for the language model.
        prompt = (
            "You are the Reviewer Agent.\n\n"
            f"User Request:\n{workflow_state.user_request}\n\n"
            f"Knowledge:\n{workflow_state.knowledge}\n\n"
            f"Execution Plan:\n{workflow_state.plan}\n\n"
            f"Research:\n{workflow_state.research}\n\n"
            "Review the proposed solution.\n"
            "Limit the response to a maximum of 20 words.\n"
            "Return plain text only."
        )

        # Invoke the shared language model helper.
        workflow_state.review = (
            self.invoke_llm(
                prompt,
            )
        )

        # Log the review.
        self.logger.info(
            "Review : %s",
            workflow_state.review,
        )

        # Log successful completion.
        self.logger.info("Reviewer Agent execution completed.")

        # Return the workflow state unchanged.
        return workflow_state


# ==========================================================================
# End of File
# ==========================================================================