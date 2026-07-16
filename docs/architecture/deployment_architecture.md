\# Deployment Architecture



```mermaid

flowchart TB



&#x20;   %% ==========================================================

&#x20;   %% Client Layer

&#x20;   %% ==========================================================



&#x20;   USER\["👤 User Browser"]



&#x20;   %% ==========================================================

&#x20;   %% Application Host

&#x20;   %% ==========================================================



&#x20;   subgraph HOST\["Application Host"]



&#x20;       STREAMLIT\["Streamlit Application"]



&#x20;       ORCH\["Agent Orchestrator"]



&#x20;       MEMORY\["Conversation Memory"]



&#x20;       AGENTS\["Specialized AI Agents"]



&#x20;   end



&#x20;   %% ==========================================================

&#x20;   %% AI Services

&#x20;   %% ==========================================================



&#x20;   subgraph AI\["AI Runtime"]



&#x20;       LLM\["Ollama Runtime"]



&#x20;       MODEL\["Llama 3.x Model"]



&#x20;   end



&#x20;   %% ==========================================================

&#x20;   %% Knowledge Layer

&#x20;   %% ==========================================================



&#x20;   subgraph KNOWLEDGE\["Knowledge Services"]



&#x20;       CHROMA\["ChromaDB"]



&#x20;       EMBEDDINGS\["Embedding Model"]



&#x20;   end



&#x20;   %% ==========================================================

&#x20;   %% Enterprise Resources

&#x20;   %% ==========================================================



&#x20;   subgraph STORAGE\["Enterprise Resources"]



&#x20;       DOCS\["Project Documents"]



&#x20;       CONFIG\["Configuration"]



&#x20;       LOGS\["Application Logs"]



&#x20;   end



&#x20;   %% ==========================================================

&#x20;   %% Connections

&#x20;   %% ==========================================================



&#x20;   USER --> STREAMLIT



&#x20;   STREAMLIT --> ORCH



&#x20;   ORCH --> MEMORY



&#x20;   ORCH --> AGENTS



&#x20;   AGENTS --> CHROMA



&#x20;   CHROMA --> EMBEDDINGS



&#x20;   AGENTS --> LLM



&#x20;   LLM --> MODEL



&#x20;   AGENTS --> DOCS



&#x20;   AGENTS --> CONFIG



&#x20;   AGENTS --> LOGS

```

