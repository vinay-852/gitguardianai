---
title: GITGuardianAI
app_file: app.py
sdk: gradio
sdk_version: 5.34.0
---
# GITGuardianAI

GITGuardianAI is an automated code review tool that leverages multiple specialized agents to analyze code for quality, performance, and security issues. It is designed to streamline the code review process by running dedicated agents in parallel and merging their findings into a single, comprehensive report.

## Features
- **Parallel Code Review:** Runs Code Quality, Performance, and Security agents simultaneously on changed code.
- **Automated Merging:** Synthesizes results from all agents into a unified report for easy review.
- **Extensible Architecture:** Built using modular agents, making it easy to add or customize review criteria.

## Architecture
![Architecture](https://github.com/user-attachments/assets/278698e8-6c6e-48d5-9616-324793e6e9c9)

## How It Works
1. **Parallel Analysis:** The tool uses three main agents:
   - **CodeQualityAgent:** Checks for code quality and best practices.
   - **PerformanceAgent:** Identifies performance bottlenecks and inefficiencies.
   - **SecurityAgent:** Detects potential security vulnerabilities.
2. **Result Merging:** The results from all agents are merged by a language model agent into a single, actionable report.
3. **Orchestration:** The process is coordinated by an orchestrator agent, ensuring a smooth and efficient review workflow.

## Usage
- The main application entry point is `app.py`.
- The tool uses [Gradio](https://gradio.app/) for its interface (see `app.py`).
- To run the app, ensure all dependencies are installed (see `requiremnts.txt`) and execute:
  ```bash
  python app.py
  ```

## Requirements
- Python 3.12+
- Gradio 5.34.0
- Google ADK agents (see code for details)

## Project Structure
- `agent.py`: Sets up and orchestrates the review agents.
- `agents/`: Contains the specialized agent implementations.
- `app.py`: Gradio app interface.
- `prompt.py`: Prompt templates for agents.

## Links
- **Deployed App:** [https://vinay-pepakayala-gitguardianai.hf.space](https://vinay-pepakayala-gitguardianai.hf.space)
- **GitHub Repository:** [https://github.com/vinay-852/gitguardianai.git](https://github.com/vinay-852/gitguardianai.git)

---
GITGuardianAI helps automate and improve the code review process, making your codebase more robust, performant, and secure.
