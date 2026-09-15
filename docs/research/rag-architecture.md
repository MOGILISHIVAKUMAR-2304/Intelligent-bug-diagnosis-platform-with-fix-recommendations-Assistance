# RAG Architecture

## What is RAG?

RAG stands for Retrieval-Augmented Generation. It combines information retrieval with a Large Language Model (LLM).

Instead of depending only on the knowledge stored in the LLM, RAG first retrieves relevant information from an external knowledge base and then provides that information to the LLM to generate a better answer.

## RAG Pipeline

The basic RAG pipeline is:

User Query
↓
Query Processing
↓
Embedding Generation
↓
Vector Search
↓
Retrieve Relevant Documents
↓
Context + User Query
↓
LLM
↓
Generated Response

## RAG in Our Project

In our AI defect analysis system, RAG will be used to retrieve similar historical software defects.

When a user submits a new bug report:

1. The bug report is processed.
2. An embedding is generated for the bug.
3. The vector database searches for similar historical defects.
4. Relevant historical bug reports are retrieved.
5. The retrieved information is provided to the AI agents and LLM.
6. The system generates a diagnosis and recommendations.

## Main Components

### 1. Bug Report

The user submits a bug description, stack trace, error log, or bug report file.

### 2. Embedding Model

The bug report is converted into a numerical vector called an embedding.

### 3. Vector Database

The embeddings of historical defects are stored in a vector database.

### 4. Retriever

The retriever searches the vector database for historically similar defects.

### 5. Context

The most relevant historical defect information is collected as context.

### 6. LLM

The Large Language Model uses the user's bug report and retrieved context to generate an analysis.

## Benefits of RAG

- Uses historical project knowledge
- Helps find similar defects
- Provides relevant context to the LLM
- Can reduce unsupported answers
- Allows the knowledge base to be updated with new defects

## RAG for Defect Analysis

The proposed system will use RAG to connect new bug reports with historical Mozilla, Apache, and Eclipse defect data.

The retrieved historical defects will support triage, duplicate detection, root cause analysis, and remediation recommendations.
