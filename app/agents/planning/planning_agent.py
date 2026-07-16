"""
===========================================================================
Project     : Autonomous AI Agent Platform
Module      : planning_agent.py

Description:
    Planning Agent implementation.

Purpose:
    This module implements the Planning Agent responsible for
    generating an execution plan for the current workflow.

Responsibilities:
    - Receive workflow state
    - Analyze retrieved knowledge (future implementation)
    - Generate an execution plan (future implementation)
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
# Planning Agent
# ==========================================================================

class PlanningAgent(BaseAgent):
    """
    Planning Agent.

    Responsible for generating an execution plan for the workflow.
    """

    # ----------------------------------------------------------------------
    # Constructor
    # ----------------------------------------------------------------------

    def __init__(self) -> None:
        """
        Initialize the Planning Agent.
        """

        # Initialize the Base Agent.
        super().__init__("PlanningAgent")

    # ----------------------------------------------------------------------
    # Execute Agent
    # ----------------------------------------------------------------------

    def execute(
        self,
        workflow_state: WorkflowState,
    ) -> WorkflowState:
        """
        Execute the Planning Agent.

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
        self.logger.info("Planning Agent execution started.")

        # ------------------------------------------------------------------
        # Future Implementation
        # ------------------------------------------------------------------
        #
        # Planned responsibilities:
        #
        # 1. Analyze retrieved knowledge.
        # 2. Break the problem into executable tasks.
        # 3. Create an execution plan.
        # 4. Attach the execution plan to the workflow state.
        #
        # ------------------------------------------------------------------

        # Build the prompt for the language model.
        prompt = (
            "You are the Planning Agent.\n\n"
            f"User Request:\n{workflow_state.user_request}\n\n"
            f"Knowledge:\n{workflow_state.knowledge}\n\n"
            "Create a high-level execution plan.\n"
            "Limit the response to a maximum of 20 words.\n"
            "Return plain text only."
        )

        # Invoke the shared language model helper.
        workflow_state.plan = (
            self.invoke_llm(
                prompt,
            )
        )

        # Log the generated execution plan.
        self.logger.info(
            "Plan : %s",
            workflow_state.plan,
        )

        # Log successful completion.
        self.logger.info("Planning Agent execution completed.")

        # Return the workflow state unchanged.
        return workflow_state


# ==========================================================================
# End of File
# ==========================================================================