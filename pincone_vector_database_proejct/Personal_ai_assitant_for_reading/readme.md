# MR. X — AI-Powered Document Intelligence Assistant

MR. X is a document intelligence system built using Streamlit and Pinecone Assistant API that enables users to create a searchable knowledge base from their personal documents and interact with that knowledge through natural language conversations.

The application combines document ingestion, semantic retrieval, and conversational AI to transform static files into an interactive source of information.

---

## Overview

Traditional document storage systems allow users to store information but provide limited capabilities for extracting insights efficiently. MR. X addresses this problem by allowing users to upload documents and query them conversationally.

Instead of manually searching through large PDFs, notes, reports, or study materials, users can ask questions in natural language and receive context-aware responses generated from the uploaded knowledge base.

---

## Key Capabilities

### Document Ingestion

The system supports uploading multiple document formats including:

- PDF
- TXT
- DOCX
- Markdown

Uploaded files are processed and added to the assistant's knowledge base where they become available for retrieval and question answering.

### Conversational Retrieval

Users can interact with uploaded documents through a chat interface.

Examples:

- Summarize this document
- What are the main findings?
- Explain chapter 4
- What recommendations were made?
- Compare two concepts discussed in the file

### Knowledge Base Management

The application provides:

- File upload workflow
- Knowledge base monitoring
- Uploaded file listing
- Processing status visibility

### Source Attribution

Responses include references to the originating documents, providing transparency and allowing users to verify generated answers against source material.

### Persistent Conversation Context

The assistant maintains conversational history during a session, enabling follow-up questions and contextual interactions.

---

## System Architecture

```text
User Documents
      │
      ▼
Document Upload
      │
      ▼
Pinecone Assistant
      │
      ▼
Knowledge Base Creation
      │
      ▼
Semantic Retrieval
      │
      ▼
Context Generation
      │
      ▼
Conversational Response
```

The application leverages Pinecone's Assistant API to manage document indexing, retrieval, and contextual response generation.

---

## Technology Stack

### Frontend

- Streamlit

### Backend

- Python

### AI Infrastructure

- Pinecone Assistant API
- Vector-Based Retrieval
- Semantic Search

### Supporting Libraries

- pinecone
- streamlit
- python-dotenv

---

## User Interface

The application includes a custom-designed interface featuring:

- Glassmorphism-inspired visual design
- Real-time chat interaction
- Dynamic document management sidebar
- Responsive layout
- Session-based conversation history

The UI was built to provide a modern user experience while maintaining simplicity and readability.

---

## Project Structure

```text
Personal_ai_assistant_for_reading/
│
├── app.py
├── pinecone_client.py
├── requirements.txt
├── .gitignore
└── README.md
```

### app.py

Contains:

- User Interface
- Chat Workflow
- File Upload Handling
- Session State Management

### pinecone_client.py

Contains:

- Pinecone Configuration
- Assistant Connection Logic
- File Upload Functions
- Query Processing Functions
- Knowledge Base Operations

---

## Installation

### Clone Repository

```bash
git clone https://github.com/harshu078600-tech/Database-projects.git
```

### Navigate to Project

```bash
cd Personal_ai_assistant_for_reading
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
PINECONE_API_KEY=YOUR_API_KEY
```

### Launch Application

```bash
streamlit run app.py
```

---

## Deployment

The application is designed to be deployed on Streamlit Community Cloud.

Required Secret:

```toml
PINECONE_API_KEY="YOUR_API_KEY"
```

No local environment file is required after deployment.

---

## Security Considerations

Sensitive credentials are never committed to source control.

Security measures include:

- Environment variable configuration
- Streamlit Secrets integration
- Git ignore protection for local credentials
- API key rotation support

---

## Challenges Addressed

During development, several engineering challenges were solved:

- Secure credential management after API key exposure
- Pinecone Assistant integration and configuration
- Document ingestion workflow design
- Streamlit cloud deployment
- Knowledge base synchronization
- Conversational context management

---

## Future Enhancements

Planned improvements include:

- User authentication
- Multi-user workspaces
- Conversation persistence
- Advanced document analytics
- Multi-assistant architecture
- Knowledge base categorization
- Citation visualization
- Hybrid retrieval strategies

---

## Learning Outcomes

This project provided practical experience with:

- Retrieval-Augmented Generation (RAG)
- Vector Databases
- Semantic Search Systems
- AI Application Deployment
- Cloud-Based Secret Management
- Conversational User Interfaces
- Production-Oriented Python Development

---

## Author

Harsh

GitHub:
https://github.com/harshu078600-tech
