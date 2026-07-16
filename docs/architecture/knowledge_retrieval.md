\# Knowledge Retrieval (RAG) Flow



```mermaid

flowchart LR



&#x20;   %% ==========================================================

&#x20;   %% User Request

&#x20;   %% ==========================================================



&#x20;   USER\["👤 User"]



&#x20;   QUERY\["User Query"]



&#x20;   %% ==========================================================

&#x20;   %% Retrieval Pipeline

&#x20;   %% ==========================================================



&#x20;   EMBED\["Generate Embedding"]



&#x20;   VECTOR\["ChromaDB Vector Search"]



&#x20;   CONTEXT\["Relevant Context"]



&#x20;   %% ==========================================================

&#x20;   %% Prompt Construction

&#x20;   %% ==========================================================



&#x20;   PROMPT\["Prompt Builder"]



&#x20;   %% ==========================================================

&#x20;   %% AI Runtime

&#x20;   %% ==========================================================



&#x20;   LLM\["Ollama / Llama"]



&#x20;   RESPONSE\["Generated Response"]



&#x20;   %% ==========================================================

&#x20;   %% Flow

&#x20;   %% ==========================================================



&#x20;   USER --> QUERY



&#x20;   QUERY --> EMBED



&#x20;   EMBED --> VECTOR



&#x20;   VECTOR --> CONTEXT



&#x20;   CONTEXT --> PROMPT



&#x20;   QUERY --> PROMPT



&#x20;   PROMPT --> LLM



&#x20;   LLM --> RESPONSE



&#x20;   RESPONSE --> USER

```

