# AI Agent Responsibilities

## Overview

The AI defect analysis system uses multiple specialized agents. Each agent has a specific responsibility and contributes to the overall defect diagnosis.

## 1. Triage Agent

Responsibilities:
- Classify the submitted defect.
- Identify the affected component or module.
- Estimate severity and priority.
- Summarize the issue for downstream agents.
- Extract important fields from the bug report.

Input:
- Bug description
- Environment information
- Error information

Output:
- Bug category
- Severity
- Priority
- Affected component
- Structured summary

## 2. Log Analysis Agent

Responsibilities:
- Analyze error logs and stack traces.
- Identify relevant error messages.
- Identify files, functions, modules, or components mentioned in the trace.
- Detect patterns that may indicate the source of failure.
- Produce structured log findings.

Input:
- Stack trace
- Error logs
- Error messages

Output:
- Key errors
- Relevant stack-trace locations
- Suspected components
- Log analysis findings

## 3. Duplicate Detection Agent

Responsibilities:
- Compare the new defect with retrieved historical defects.
- Identify potentially duplicate or highly similar issues.
- Consider semantic similarity and relevant metadata.
- Provide similarity evidence.

Input:
- Current bug report
- Retrieved historical defects

Output:
- Similar defect candidates
- Similarity assessment
- Supporting evidence

## 4. Root Cause Agent

Responsibilities:
- Combine bug report, log analysis, and retrieved historical knowledge.
- Identify possible root causes.
- Explain the reasoning in a structured way.
- Distinguish evidence from hypotheses.

Input:
- Bug report
- Log Analysis Agent findings
- Retrieved historical defects
- Triage findings

Output:
- Possible root causes
- Supporting evidence
- Confidence assessment

## 5. Remediation Agent

Responsibilities:
- Use the diagnosis and historical resolutions to suggest possible remediation.
- Provide practical next steps for developers.
- Reference relevant historical fixes when available.
- Avoid presenting an unverified fix as certain.

Input:
- Root cause findings
- Historical resolutions
- Bug information

Output:
- Recommended remediation
- Suggested next steps
- Relevant historical resolutions

## Agent Collaboration

The agents work together through an Agent Orchestrator.

Proposed flow:

Triage Agent  
↓  
Log Analysis Agent  
↓  
Duplicate Detection Agent  
↓  
Root Cause Agent  
↓  
Remediation Agent  
↓  
Structured Diagnosis

The exact orchestration can be refined in later milestones after testing.
