"""
===========================================================================
Project     : Autonomous AI Agent Platform
Module      : constants.py

Description:
    Centralized application constants.

Purpose:
    This module defines reusable constants that are shared across the
    entire application.

Responsibilities:
    - Define workflow status values
    - Define task status values
    - Define agent names
    - Define application constants
    - Eliminate hard-coded values

Author      : Lokesh Kumar
Version     : v1.0.0
===========================================================================
"""

# ==========================================================================
# Workflow Status Constants
# ==========================================================================

# Workflow has been created.
WORKFLOW_CREATED = "CREATED"

# Workflow is being planned.
WORKFLOW_PLANNING = "PLANNING"

# Workflow is ready for execution.
WORKFLOW_READY = "READY"

# Workflow is currently running.
WORKFLOW_RUNNING = "RUNNING"

# Workflow is waiting for approval or input.
WORKFLOW_WAITING = "WAITING"

# Workflow is under review.
WORKFLOW_REVIEWING = "REVIEWING"

# Workflow completed successfully.
WORKFLOW_COMPLETED = "COMPLETED"

# Workflow failed.
WORKFLOW_FAILED = "FAILED"

# Workflow was cancelled.
WORKFLOW_CANCELLED = "CANCELLED"

# ==========================================================================
# Task Status Constants
# ==========================================================================

# Task has not started.
TASK_PENDING = "PENDING"

# Task is currently executing.
TASK_RUNNING = "RUNNING"

# Task completed successfully.
TASK_COMPLETED = "COMPLETED"

# Task failed.
TASK_FAILED = "FAILED"

# ==========================================================================
# Agent Names
# ==========================================================================

# Orchestrator Agent
ORCHESTRATOR_AGENT = "OrchestratorAgent"

# Knowledge Agent
KNOWLEDGE_AGENT = "KnowledgeAgent"

# Planning Agent
PLANNING_AGENT = "PlanningAgent"

# Research Agent
RESEARCH_AGENT = "ResearchAgent"

# Execution Agent
EXECUTION_AGENT = "ExecutionAgent"

# Reviewer Agent
REVIEWER_AGENT = "ReviewerAgent"

# ==========================================================================
# Memory Types
# ==========================================================================

# Startup memory.
MEMORY_TYPE_STARTUP = "startup"

# Completed workflow summary.
MEMORY_TYPE_WORKFLOW = "workflow"

# User interaction.
MEMORY_TYPE_USER = "user"

# Agent-generated knowledge.
MEMORY_TYPE_KNOWLEDGE = "knowledge"

# ==========================================================================
# Default Application Constants
# ==========================================================================

# Default application title.
APPLICATION_NAME = "Autonomous AI Agent Platform"

# Current application version.
APPLICATION_VERSION = "1.0.0"

# ==========================================================================
# End of File
# ==========================================================================