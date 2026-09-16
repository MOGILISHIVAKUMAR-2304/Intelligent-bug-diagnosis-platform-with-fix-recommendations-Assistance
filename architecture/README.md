# Architecture Documentation

## Project

AI-Based Software Defect Analysis and Root Cause Detection System

## Purpose

This directory contains the system architecture and design documentation for the project.

## Architecture Documents

- `system-architecture.md` — Overall system architecture and data flow.
- `agent-responsibilities.md` — Responsibilities of each AI agent.
- `agent-orchestration.md` — Communication and execution flow between agents.
- `data-model.md` — Main data structures and relationships used by the system.

## Main Architecture Components

1. Bug Submission Interface
2. Backend/API Layer
3. Bug Report Processing
4. Historical Defect Knowledge Base
5. Data Cleaning and Chunking
6. Embedding Generation
7. Vector Database
8. RAG Retrieval Pipeline
9. Large Language Model
10. AI Agent Layer
11. Agent Orchestrator
12. Structured Diagnosis
13. Results and Recommendations Interface

## AI Agents

The system uses five specialized agents:

- Triage Agent
- Log Analysis Agent
- Duplicate Detection Agent
- Root Cause Agent
- Remediation Agent

## Overall Flow

User submits a bug report.

↓

Bug Report Processing

↓

Triage and Log Analysis

↓

Historical Defect Retrieval

↓

Duplicate Detection

↓

Root Cause Analysis

↓

Remediation Suggestions

↓

Structured Diagnosis

↓

Results Interface

## Documentation Status

Milestone 1 architecture documentation is under development.

Future milestones will implement the documented architecture and integrate the individual components.
