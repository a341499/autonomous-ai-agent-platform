"""
===========================================================================
Project     : Autonomous AI Agent Platform
Module      : base_agent.py

Description:
    Base class for all AI agents.

Purpose:
    This module provides a common foundation for every AI agent in the
    platform.

Responsibilities:
    - Store agent information
    - Initialize application logger
    - Provide access to application settings
    - Define the common execution interface

Author      : Lokesh Kumar
Version     : v1.0.0
===========================================================================
"""

# ==========================================================================
# Standard Library Imports
# ==========================================================================

# Import the Abstract Base Class framework.
from abc import ABC

# Import the abstractmethod decorator.
from abc import abstractmethod

# ==========================================================================
# Application Imports
# ==========================================================================

# Import the shared application settings.
from app.config.settings import settings

# Import the centralized logger factory.
from app.utils.logger import get_logger

# Import the centralized LLM service.
from app.services import LLMService

# ==========================================================================
# Base Agent Class
# ==========================================================================

class BaseAgent(ABC):
    """
    Abstract base class for all AI agents.

    Every specialized agent in the application must inherit from this
    class and implement the execute() method.
    """

    # ----------------------------------------------------------------------
    # Constructor
    # ----------------------------------------------------------------------

    def __init__(self, agent_name: str) -> None:
        """
        Initialize the base agent.

        Parameters
        ----------
        agent_name : str
            Human-readable name of the agent.
        """

        # Store the agent name.
        self.agent_name = agent_name

        # Store the shared application settings.
        self.settings = settings

        # Create a logger dedicated to this agent.
        self.logger = get_logger(agent_name)

        # Create the shared LLM service.
        self.llm_service = LLMService()

        # Log successful initialization.
        self.logger.info(
            "%s initialized successfully.",
            self.agent_name,
        )

    # ----------------------------------------------------------------------
    # LLM Helper Methods
    # ----------------------------------------------------------------------

    def invoke_llm(
        self,
        prompt: str,
    ) -> str:
        """
        Invoke the configured Large Language Model.

        Parameters
        ----------
        prompt : str
            Prompt to send to the language model.

        Returns
        -------
        str
            Language model response.
        """

        # Log the LLM invocation.
        self.logger.info("Invoking LLM.")

        # Generate the response using the shared LLM service.
        return (
            self.llm_service.generate(
                prompt,
            )
        )

    # ----------------------------------------------------------------------
    # Abstract Methods
    # ----------------------------------------------------------------------

    @abstractmethod
    def execute(self, workflow_state: dict) -> dict:
        """
        Execute the agent.

        Parameters
        ----------
        workflow_state : dict
            Current workflow state.

        Returns
        -------
        dict
            Updated workflow state.
        """

        # Every derived agent must implement this method.
        raise NotImplementedError(
            "Derived agent must implement the execute() method."
        )


# ==========================================================================
# End of File
# ==========================================================================