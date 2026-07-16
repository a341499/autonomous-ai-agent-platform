"""
===========================================================================
Project     : Autonomous AI Agent Platform
Module      : agent_orchestrator.py

Description:
    Agent Orchestrator implementation.

Purpose:
    This module implements the Agent Orchestrator responsible for
    coordinating workflow execution across multiple AI agents.

Responsibilities:
    - Initialize workflow execution
    - Coordinate agent execution
    - Manage workflow state
    - Return the completed workflow

Author      : Lokesh Kumar
Version     : v1.0.0
===========================================================================
"""

# ==========================================================================
# Application Imports
# ==========================================================================

# Import the centralized logger factory.
from app.utils import get_logger

# Import the workflow state model.
from app.models.workflow_state import WorkflowState

# Import workflow status constants.
from app.config.constants import (
    WORKFLOW_COMPLETED,
    WORKFLOW_RUNNING,
)

# Import the Knowledge Agent.
from app.agents.knowledge import KnowledgeAgent

# Import the Planning Agent.
from app.agents.planning import PlanningAgent

# Import the Research Agent.
from app.agents.research import ResearchAgent

# Import the Reviewer Agent.
from app.agents.reviewer import ReviewerAgent

# Import the Execution Agent.
from app.agents.execution import ExecutionAgent

# ==========================================================================
# Agent Orchestrator
# ==========================================================================


class AgentOrchestrator:
    """
    Agent Orchestrator.

    Coordinates workflow execution across multiple AI agents.
    """

    # ----------------------------------------------------------------------
    # Constructor
    # ----------------------------------------------------------------------

    def __init__(self) -> None:
        """
        Initialize the Agent Orchestrator.
        """

        # Create the orchestrator logger.
        self.logger = get_logger("AgentOrchestrator")

        # Create the Knowledge Agent.
        self.knowledge_agent = KnowledgeAgent()

        # Create the Planning Agent.
        self.planning_agent = PlanningAgent()

        # Create the Research Agent.
        self.research_agent = ResearchAgent()

        # Create the Reviewer Agent.
        self.reviewer_agent = ReviewerAgent()

        # Create the Execution Agent.
        self.execution_agent = ExecutionAgent()

    # ----------------------------------------------------------------------
    # Execute Workflow
    # ----------------------------------------------------------------------

    def execute_workflow(
        self,
        workflow_state: WorkflowState,
    ) -> WorkflowState:
        """
        Execute the workflow.

        Parameters
        ----------
        workflow_state : WorkflowState
            Current workflow state.

        Returns
        -------
        WorkflowState
            Updated workflow state.
        """

        # Log the start of workflow execution.
        self.logger.info("Workflow execution started.")

        # Update the workflow status.
        workflow_state.workflow_status = (
            WORKFLOW_RUNNING
        )

        # Execute the Knowledge Agent.
        workflow_state = self.knowledge_agent.execute(workflow_state)

        # Execute the Planning Agent.
        workflow_state = self.planning_agent.execute(
            workflow_state,
        )

        # Execute the Research Agent.
        workflow_state = self.research_agent.execute(
            workflow_state,
        )

        # Execute the Reviewer Agent.
        workflow_state = self.reviewer_agent.execute(
            workflow_state,
        )

        # Execute the Execution Agent.
        workflow_state = self.execution_agent.execute(
            workflow_state,
        )

        # Update the workflow status.
        workflow_state.workflow_status = (
            WORKFLOW_COMPLETED
        )

        # Log successful completion.
        self.logger.info("Workflow execution completed.")

        # Return the updated workflow state.
        return workflow_state

# ==========================================================================
# End of File
# ==========================================================================