# Data Model

## Overview

The data model defines the main information stored and processed by the AI defect analysis system.

## 1. Bug Report

A Bug Report represents a newly submitted software defect.

Fields:
- Bug ID
- Title
- Description
- Steps to Reproduce
- Expected Behavior
- Actual Behavior
- Error Message
- Stack Trace
- Logs
- Environment
- Severity
- Priority
- Component
- Submission Date

## 2. Historical Defect

A Historical Defect represents a previously reported software issue stored in the knowledge base.

Fields:
- Defect ID
- Title
- Description
- Component
- Severity
- Priority
- Error Information
- Stack Trace
- Resolution
- Status
- Source
- Date

## 3. Document Chunk

A Document Chunk represents a smaller section of a historical defect document.

Fields:
- Chunk ID
- Defect ID
- Chunk Text
- Chunk Position
- Metadata

Chunking allows large defect reports to be divided into smaller pieces for efficient retrieval.

## 4. Embedding

An Embedding represents the numerical vector generated from a document chunk.

Fields:
- Embedding ID
- Chunk ID
- Vector
- Embedding Model

Embeddings are used for
