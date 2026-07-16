"""
===========================================================================
Project     : Autonomous AI Agent Platform
Module      : settings.py

Description:
    Centralized application configuration.

Purpose:
    This module loads configuration values from environment variables
    and exposes them through a single shared Settings object.

Responsibilities:
    - Load environment variables
    - Store application configuration
    - Provide default values
    - Eliminate direct environment variable access elsewhere

Author      : Lokesh Kumar
Version     : v1.0.0
=========================================================================== 
"""

# ==========================================================================
# Standard Library Imports
# ==========================================================================

# Import the operating system module to access environment variables.
import os

# ==========================================================================
# Third-Party Imports
# ==========================================================================

# Import the dotenv helper for loading values from the .env file.
from dotenv import load_dotenv

# ==========================================================================
# Load Environment Variables
# ==========================================================================

# Load environment variables from the project's .env file.
#
# If the .env file is present, the variables defined within it are loaded
# into the application's environment.
#
# If the .env file is missing, the application continues by using existing
# operating system environment variables or the default values defined below.
load_dotenv()

# ==========================================================================
# Settings Class
# ==========================================================================


class Settings:
    """
    Centralized application configuration.

    Every module in the application should obtain configuration values
    through this class instead of reading environment variables directly.

    Benefits:
        - Centralized configuration management
        - Consistent default values
        - Easier maintenance
        - Improved readability
        - Single source of configuration
    """

    # ======================================================================
    # Large Language Model (LLM) Configuration
    # ======================================================================

    # Base URL of the local Ollama server.
    OLLAMA_BASE_URL = os.getenv(
        "OLLAMA_BASE_URL",
        "http://localhost:11434",
    )

    # Default Large Language Model used by the application.
    LLM_MODEL = os.getenv(
        "LLM_MODEL",
        "llama3.2",
    )

    # ======================================================================
    # Embedding Model Configuration
    # ======================================================================

    # Embedding model used for semantic search and vector generation.
    EMBEDDING_MODEL = os.getenv(
        "EMBEDDING_MODEL",
        "nomic-embed-text",
    )

    # ======================================================================
    # Vector Database Configuration
    # ======================================================================

    # Directory where the ChromaDB vector database is stored.
    CHROMA_DB_PATH = os.getenv(
        "CHROMA_DB_PATH",
        "./data/chroma_db",
    )

    # ======================================================================
    # Logging Configuration
    # ======================================================================

    # Default logging level used throughout the application.
    LOG_LEVEL = os.getenv(
        "LOG_LEVEL",
        "INFO",
    )


# ==========================================================================
# Shared Settings Object
# ==========================================================================

# Create a single shared Settings instance.
#
# Every application module should import and use this object instead of
# creating additional Settings objects.
#
# Example:
#
#     from app.config.settings import settings
#
settings = Settings()