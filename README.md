<div align="center">

# 🚀 PRism AI
### Intelligent AI-Powered Pull Request Review Platform

Analyze Pull Requests using AI Agents, RAG, and Large Language Models to generate comprehensive code reviews, security insights, architecture suggestions, and developer-friendly summaries.

[![Next.js](https://img.shields.io/badge/Next.js-15-black?logo=next.js)](https://nextjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Supabase](https://img.shields.io/badge/Supabase-Database-3ECF8E?logo=supabase)](https://supabase.com/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5-blue?logo=typescript)](https://www.typescriptlang.org/)
[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)]
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

</div>

---

# 📌 Overview

PRism AI is an AI-powered Pull Request Intelligence Platform that helps developers understand pull requests faster through automated AI analysis.

Instead of simply summarizing code changes, PRism AI performs intelligent reasoning over Pull Requests using multiple AI-powered analysis stages to identify:

- ✅ Code Quality Issues
- 🔒 Security Vulnerabilities
- ⚡ Performance Improvements
- 🧹 Maintainability Suggestions
- 🧠 AI Generated Review Summary
- 📖 Pull Request Explanation
- 🏗 Architecture Insights

The goal is to reduce review time while improving code quality for both maintainers and contributors.

---

# 🌐 Live Demo

## Frontend

> **Vercel Deployment**

**🔗 https://p-rism-ai.vercel.app/**

---

## Backend API

> **Railway Deployment**

**🔗 prism-production-b0e0.up.railway.app**

Swagger Documentation:

**🔗 prism-production-b0e0.up.railway.app/docs**

---

# ✨ Features

- GitHub OAuth Authentication
- Repository Browser
- Pull Request Explorer
- AI-powered PR Analysis
- Multi-Agent Analysis Pipeline
- Retrieval-Augmented Generation (RAG)
- Security Review
- Performance Review
- Code Quality Review
- AI Generated Summary
- Architecture Suggestions
- Responsive Modern UI
- Dark Mode
- Production Deployment

---

# 🏗 Architecture

```
                        GitHub

                           │
                           ▼

                  GitHub OAuth Login

                           │

                           ▼

                     Next.js Frontend
                     (Vercel Deployment)

                           │

                 REST API (FastAPI)

                           │

                           ▼

                   AI Analysis Engine

        ┌────────────┬────────────┬────────────┐
        │            │            │            │
        ▼            ▼            ▼            ▼

 Security      Code Review    RAG Engine   AI Summary

        │            │            │            │

        └────────────┴────────────┴────────────┘

                           │

                           ▼

                     Ollama Cloud API

```

---

# 🛠 Tech Stack

## Frontend

- Next.js
- TypeScript
- Tailwind CSS
- React
- Framer Motion

---

## Backend

- FastAPI
- Python
- Pydantic
- Uvicorn

---

## AI

- GROQ API
- RAG
- Embeddings
- Vector Search

---

## Database

- Supabase

---

## Deployment

- Vercel
- Railway

---

# 📂 Project Structure

```
PRISM/

├── ai/
├── backend/
├── frontend/
├── docs/
├── rag/
├── scanners/
├── ml/
├── tests/
├── supabase/
└── README.md
```

---

# 🚀 Getting Started

## Clone Repository

```bash
git clone https://github.com/<username>/PRISM.git

cd PRISM
```

---

# Backend Setup

```bash
cd backend

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

Copy the environment variables

```bash
cp .env.example .env
```

Fill your credentials inside:

```
backend/.env
```

Run the backend

```bash
uvicorn main:app --reload
```

---

# Frontend Setup

```bash
cd frontend

npm install
```

Copy

```bash
cp .env.example .env.local
```

Fill the environment variables.

Run

```bash
npm run dev
```

---

# Environment Variables

Backend

```
backend/.env
```

Frontend

```
frontend/.env.local
```

Refer to the provided `.env.example` files.

---


# API Documentation

Swagger UI

```
prism-production-b0e0.up.railway.app/docs
```

---

# Deployment

## Frontend

Vercel

## Backend

Railway

---

# Future Improvements

- AI Chat with Pull Requests
- Multi-Repository Dashboard
- Team Workspaces
- CI/CD Integration
- GitHub Checks API
- Slack Notifications
- Email Reports
- PDF Report Export
- Repository Analytics
- PR Risk Scoring

---

# Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature/amazing-feature
```

3. Commit your changes

```bash
git commit -m "Add amazing feature"
```

4. Push

```bash
git push origin feature/amazing-feature
```

5. Open a Pull Request

---

# License

Distributed under the MIT License.

---

# Authors

**Yashwanth Abhishek**

---

<div align="center">

Made with ❤️ using AI, FastAPI, Next.js & Ollama Cloud

⭐ Star this repository if you found it useful!

</div>
