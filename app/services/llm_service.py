"""
===========================================================================
Project     : Autonomous AI Agent Platform
Module      : llm_service.py

Description:
    Large Language Model service.

Purpose:
    Provides a centralized interface for communicating with
    Large Language Models.

Responsibilities:
    - Accept prompts
    - Invoke configured LLM
    - Return generated responses

Author      : Lokesh Kumar
Version     : v1.0.0
===========================================================================
"""

# ==========================================================================
# Standard Library Imports
# ==========================================================================

# ==========================================================================
# Third-Party Imports
# ==========================================================================

# Import the Ollama client.
import ollama

# ==========================================================================
# Application Imports
# ==========================================================================

# Import the shared application settings.
from app.config import settings

# Import the centralized logger factory.
from app.utils import get_logger

# ==========================================================================
# LLM Service
# ==========================================================================

class LLMService:
    """
    Service responsible for interacting with the configured LLM.
    """

    def __init__(self) -> None:
        """
        Initialize the LLM service.
        """

        # Create the service logger.
        self.logger = get_logger("LLMService")

    def generate(
        self,
        prompt: str,
    ) -> str:
        """
        Generate a response from the language model.

        Parameters
        ----------
        prompt : str
            Prompt for the language model.

        Returns
        -------
        str
            Generated response.
        """

        # Log response generation.
        self.logger.info(
            "Generating response using model: %s",
            settings.LLM_MODEL,
        )

        # Generate the response from Ollama.
        response = ollama.chat(
            model=settings.LLM_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        # Return the generated response.
        return (
            response["message"]["content"]
        )

# ==========================================================================
# End of File
# ==========================================================================