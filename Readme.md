# Memory-aware-AI-chatbot

<p align="center">
  <img src="https://img.shields.io/badge/AI-Chatbot-blueviolet?style=for-the-badge&logo=ai" alt="AI Chatbot"/>
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" alt="Python"/>
  <img src="https://img.shields.io/badge/Neo4j-GraphDB-green?style=for-the-badge&logo=neo4j" alt="Neo4j"/>
  <img src="https://img.shields.io/badge/Qdrant-VectorDB-orange?style=for-the-badge&logo=qdrant" alt="Qdrant"/>
</p>

---

## 🚀 Memory-aware-AI-chatbot

A cutting-edge, memory-augmented AI chatbot that leverages advanced LLMs, vector search, and graph databases to deliver contextually rich, fact-aware conversations. Designed for knowledge distillation, information preservation, and professional-grade dialogue.

---

## 🧠 Features

- **Memory-Aware Chat**: Remembers and retrieves past interactions for contextually relevant responses.
- **Fact Extraction**: Extracts and stores structured knowledge from conversations.
- **Vector Search**: Uses Qdrant for high-performance semantic search.
- **Graph Database**: Integrates Neo4j for knowledge graph storage and reasoning.
- **LLM Integration**: Utilizes Gemini/OpenAI models for natural, professional dialogue.
- **Environment Configurable**: Easily set up with `.env` for API keys and database credentials.

---

## 📦 Tech Stack

- **Python 3.10+**
- **Qdrant** (Vector Database)
- **Neo4j** (Graph Database)
- **Gemini/OpenAI** (LLM & Embeddings)
- **Docker Compose** (for local DB setup)

---

## 🛠️ Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd Memory-aware-AI-chatbot
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  
   # On Windows: .venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure environment variables:**
   - Copy `.env.example` to `.env` and fill in your API keys and DB credentials.
5. **Start databases with Docker Compose:**
   ```bash
   docker-compose -f docker-compose.graph.yml up -d
   ```
6. **Run the chatbot:**
   ```bash
   python mem_AI.py
   ```

---

## ⚡ Usage

- Interact with the chatbot in your terminal.
- Type your message and receive memory-aware, fact-enriched responses.
- Type `q` to exit.

---

## 📚 Example

```
>> What is the capital of France?
BOT🤖: The capital of France is Paris.
>> Remember that my favorite color is blue.
BOT🤖: Noted.
```
## 📝 Sample .env

Create a `.env` file in your project root with the following content:

```env
GOOGLE_API_KEY=your-google-api-key
NEO4J_URL=neo4j://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your-neo4j-password
```
---

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to fork the repo and submit a pull request.

---

<p align="center">
  <b>Memory-aware-AI-chatbot</b> &mdash; Professional, Contextual, Intelligent.
</p>
