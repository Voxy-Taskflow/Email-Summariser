# 📧 AI Email Summarizer

A work-in-progress Python project to fetch emails from Gmail and generate concise AI-powered summaries.

> **Goal:** Build the project from scratch to improve Python skills while learning how to work with real-world APIs, authentication, and AI integrations.

---

## Current Progress

- [x] Gmail OAuth Authentication
- [x] Gmail API Integration
- [x] Fetch latest emails
- [x] Extract sender and subject
- [ ] Extract email body
- [ ] Handle HTML & multipart emails
- [ ] AI summarization
- [ ] CLI interface
- [ ] Error handling
- [ ] Unit tests

---

## Tech Stack

- Python 3.13+
- Gmail API
- Google OAuth 2.0
- Google API Python Client
- uv (package management)

---

## Project Structure

```
email-summarizer/
│
├── src/
│   ├── __init__.py
│   ├── mailExtractor.py
│   ├── mailSummarizer.py
│   └── basicCli.py
│
├── prompts/
│
├── tests/
│
├── credentials.json      # Google OAuth credentials (not committed)
├── token.json            # Generated after authentication (ignored)
├── config.py
├── main.py
├── pyproject.toml
└── README.md
```

---

## Features (Planned)

- Authenticate with Gmail
- Fetch recent emails
- Extract clean email content
- Summarize emails using an LLM
- Support multiple summary styles
- Prioritize important emails
- Simple command-line interface

---

## Setup

### Clone the repository

```bash
git clone <repository-url>
cd email-summarizer
```

### Install dependencies

```bash
uv sync
```

### Configure Gmail API

1. Create a Google Cloud Project.
2. Enable the Gmail API.
3. Create OAuth Desktop credentials.
4. Download `credentials.json`.
5. Place it in the project root.

### Run

```bash
python main.py
```

On the first run, a browser window will open for Google authentication. A `token.json` file will be generated for future sessions.

---

## Current Output

```
---- Fetching the last 1 emails ----
From: Google <no-reply@accounts.google.com>
Subject: Security alert
```

---

## Learning Goals

This project is primarily being built to practice:

- Working with REST APIs
- OAuth authentication
- Python project organization
- Error handling
- Parsing structured data
- Integrating Large Language Models
- Writing maintainable Python code

---

## Roadmap

- [ ] Extract email body
- [ ] Clean HTML content
- [ ] Connect to an LLM
- [ ] Generate summaries
- [ ] Add CLI commands
- [ ] Add configuration options
- [ ] Improve testing
- [ ] Package the application

---

## Status

🚧 **Work in Progress**

This project is under active development and is intended as a learning project. Features and structure may change as development progresses.