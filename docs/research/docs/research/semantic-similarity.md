# Semantic Similarity and Embeddings

## What is Semantic Similarity?

Semantic similarity measures how closely two pieces of text are related in meaning.

For example:

- "Application crashes during login"
- "System fails when the user tries to sign in"

These sentences use different words but have a similar meaning.

## What are Embeddings?

An embedding is a numerical representation of text.

An embedding model converts text into a vector of numbers that represents the meaning of the text.

For example:

Bug Report A → [0.21, 0.45, 0.78, ...]

Bug Report B → [0.23, 0.43, 0.76, ...]

If two bug reports have similar meanings, their vectors will usually be close to each other in vector space.

## Similarity Search

The system can compare the embedding of a new bug report with embeddings of historical defects.

A similarity measure such as cosine similarity can be used to determine how closely two vectors are related.

## Use in Our Project

When a new bug is submitted:

1. The bug report is converted into an embedding.
2. The embedding is compared with historical defect embeddings.
3. The most semantically similar defects are retrieved.
4. These defects are provided to the RAG pipeline and AI agents.
5. The retrieved information helps with duplicate detection, root cause analysis, and remediation recommendations.

## Why Semantic Similarity is Important

Traditional keyword matching may fail when two bugs use different words.

Semantic similarity focuses on meaning rather than only exact keywords.

Therefore, it is useful for finding similar historical software defects.

## Proposed Approach

The project will use an embedding model to convert historical defect reports and new bug reports into vectors.

These vectors will be stored in a vector database and searched using semantic similarity.
