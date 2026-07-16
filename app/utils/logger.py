"""
===========================================================================
Project     : Autonomous AI Agent Platform
Module      : logger.py

Description:
    Centralized application logging framework.

Purpose:
    This module creates and configures application loggers that provide
    consistent logging behavior throughout the project.

Responsibilities:
    - Configure application logging
    - Create module-specific loggers
    - Maintain consistent log formatting
    - Prevent duplicate logger configuration

Author      : Lokesh Kumar
Version     : v1.0.0
===========================================================================
"""

# ==========================================================================
# Standard Library Imports
# ==========================================================================

# Import Python's built-in logging framework.
import logging

# ==========================================================================
# Application Imports
# ==========================================================================

# Import centralized application settings.
from app.config.settings import settings

# ==========================================================================
# Logging Configuration
# ==========================================================================

# Configure the root logger only once.
#
# This establishes a consistent logging format that will be inherited
# by all loggers created throughout the application.
logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL.upper()),
    format=(
        "%(asctime)s | "
        "%(levelname)-8s | "
        "%(name)s | "
        "%(message)s"
    ),
)

# ==========================================================================
# Logger Factory
# ==========================================================================


def get_logger(module_name: str) -> logging.Logger:
    """
    Create and return a logger for the specified module.

    Parameters
    ----------
    module_name : str
        Name of the module requesting the logger.

    Returns
    -------
    logging.Logger
        Configured logger instance.

    Notes
    -----
    Every application module should obtain its logger through
    this function rather than calling logging.getLogger()
    directly. This ensures consistent logging behavior across
    the entire application.
    """

    # Return a configured logger for the requested module.
    return logging.getLogger(module_name)