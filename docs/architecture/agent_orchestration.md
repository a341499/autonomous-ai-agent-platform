\# Agent Orchestration Flow



```mermaid

flowchart LR



&#x20;   %% ==========================================================

&#x20;   %% User Interaction

&#x20;   %% ==========================================================



&#x20;   USER\["👤 User"]



&#x20;   UI\["Streamlit UI"]



&#x20;   %% ==========================================================

&#x20;   %% Orchestrator

&#x20;   %% ==========================================================



&#x20;   ORCH\["Agent Orchestrator"]



&#x20;   ROUTER\["Intent Router"]



&#x20;   MEMORY\["Conversation Memory"]



&#x20;   %% ==========================================================

&#x20;   %% AI Agents

&#x20;   %% ==========================================================



&#x20;   PLAN\["Planning Agent"]



&#x20;   KNOW\["Knowledge Agent"]



&#x20;   EXEC\["Execution Agent"]



&#x20;   VALID\["Validation Agent"]



&#x20;   REPORT\["Reporting Agent"]



&#x20;   %% ==========================================================

&#x20;   %% AI Services

&#x20;   %% ==========================================================



&#x20;   VECTOR\["Vector Database"]



&#x20;   LLM\["LLM (Ollama / Llama)"]



&#x20;   %% ==========================================================

&#x20;   %% Response

&#x20;   %% ==========================================================



&#x20;   RESPONSE\["Final Response"]



&#x20;   %% ==========================================================

&#x20;   %% Flow

&#x20;   %% ==========================================================



&#x20;   USER --> UI



&#x20;   UI --> ORCH



&#x20;   ORCH --> ROUTER



&#x20;   ROUTER --> MEMORY



&#x20;   ROUTER --> PLAN

&#x20;   ROUTER --> KNOW

&#x20;   ROUTER --> EXEC

&#x20;   ROUTER --> VALID

&#x20;   ROUTER --> REPORT



&#x20;   PLAN --> VECTOR

&#x20;   KNOW --> VECTOR

&#x20;   EXEC --> VECTOR

&#x20;   VALID --> VECTOR

&#x20;   REPORT --> VECTOR



&#x20;   VECTOR --> LLM



&#x20;   LLM --> RESPONSE



&#x20;   RESPONSE --> UI



&#x20;   UI --> USER

```

