# Historical Defect Datasets

## Overview

Historical defect datasets contain previously reported software bugs.

These datasets are useful for our project because they provide real examples of bug descriptions, comments, resolutions, and other defect information.

The project will use historical defect data from Mozilla, Apache, and Eclipse repositories.

## 1. Mozilla Dataset

Mozilla is an open-source software organization known for projects such as Firefox.

Mozilla bug reports can contain information such as:

- Bug ID
- Bug summary
- Description
- Comments
- Product
- Component
- Severity
- Status
- Resolution
- Timestamps

This information can be used to study historical software defects and find similar bugs.

## 2. Apache Dataset

Apache Software Foundation hosts many open-source software projects.

Apache historical bug reports may contain:

- Issue ID
- Summary
- Description
- Comments
- Project
- Component
- Priority
- Status
- Resolution
- Fix information

Apache defect data can provide examples from different software projects.

## 3. Eclipse Dataset

Eclipse is a large open-source software ecosystem.

Historical Eclipse defect reports can contain:

- Bug ID
- Summary
- Description
- Comments
- Product
- Component
- Severity
- Priority
- Status
- Resolution

These reports can be used as another source of historical defect knowledge.

## Data Cleaning

Before using the datasets, the data should be cleaned and standardized.

Possible cleaning operations include:

- Removing duplicate records
- Handling missing values
- Removing irrelevant fields
- Standardizing field names
- Cleaning unnecessary text
- Normalizing bug status and resolution values

## Chunking Strategy

Large historical bug reports can be divided into smaller meaningful chunks.

Possible chunks include:

1. Bug description
2. Stack trace
3. Error logs
4. Comments
5. Resolution
6. Fix information

Chunking makes it easier to retrieve relevant information during semantic search.

## Embedding Generation

After cleaning and chunking, each useful text chunk will be converted into an embedding using an embedding model.

The embeddings will represent the semantic meaning of the defect information.

## Vector Database

The generated embeddings will be stored in a vector database.

Each vector should also contain useful metadata such as:

- Dataset source
- Bug ID
- Project
- Component
- Severity
- Status
- Resolution
- Original text

## Use in Our Project

When a new bug is submitted, its embedding will be compared with historical defect embeddings.

The system will retrieve the most similar historical bugs.

The retrieved information will be provided to the RAG pipeline and AI agents to support:

- Bug triage
- Duplicate detection
- Root cause analysis
- Remediation recommendations

## Data Pipeline

The proposed historical defect knowledge pipeline is:

Historical Datasets
        ↓
Data Cleaning
        ↓
Data Standardization
        ↓
Chunking
        ↓
Embedding Generation
        ↓
Vector Database
        ↓
Semantic Retrieval
        ↓
RAG Pipeline
        ↓
AI Agents
