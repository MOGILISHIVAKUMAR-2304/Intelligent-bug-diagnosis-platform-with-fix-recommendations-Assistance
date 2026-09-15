# System Architecture

## Project

AI-Based Software Defect Analysis and Root Cause Detection System

## Architecture Overview

The system accepts a bug report from the user, processes the submitted information, retrieves similar historical defects using RAG and semantic search, analyzes the defect using multiple AI agents, and provides structured diagnosis and recommendations.

## Main Components

### 1. Bug Submission / User Interface

Allows users to:
- Enter bug descriptions
- Paste stack traces
- Paste error logs
- Upload bug report or log files
- View analysis results

### 2. Backend / API Layer

Handles communication between the user interface and backend services.

Responsibilities:
- Receive bug submissions
- Validate requests
- Send data to processing modules
- Return analysis results

### 3. Bug Report Upload & Storage

Stores submitted bug reports and uploaded files for processing and future reference.

### 4. Bug Report Processing Module

Processes submitted bug reports.

Responsibilities:
- Extract text from files
- Clean input data
- Identify bug description, logs, and stack traces
- Prepare data for analysis

### 5. Bug Report Database

Stores submitted bug reports and their metadata.

### 6. Historical Defect Knowledge Base

Contains cleaned historical defects collected from sources such as Mozilla, Apache, and Eclipse.

### 7. Data Cleaning & Chunking Pipeline

Cleans historical defect data and divides large reports into meaningful chunks.

Possible chunks:
- Bug description
- Stack trace
- Error logs
- Comments
- Resolution
- Fix information

### 8. Embedding Generation Module

Converts bug report chunks into numerical vector embeddings.

### 9. Vector Database / Semantic Search

Stores embeddings and searches for historical defects that are semantically similar to a newly submitted bug.

### 10. RAG Retrieval Pipeline

Retrieves the most relevant historical defect information and provides it as context to the AI system.

### 11. LLM

Uses the submitted bug information and retrieved historical context to generate useful analysis and recommendations.

### 12. AI Agent Layer

The system contains multiple specialized AI agents:

- Triage Agent
- Log Analysis Agent
- Root Cause Agent
- Duplicate Detection Agent
- Remediation Agent

### 13. Agent Orchestr
