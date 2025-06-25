# Kafka + LangChain + FAISS Question-Answering Bot

This project demonstrates a production-grade pipeline combining:

- **Apache Kafka**: Real-time messaging system (for question producer-consumer flow)
- **LangChain**: Framework for building LLM-powered apps
- **Groq LLM API**: For fast and cheap LLM inference
- **HuggingFace Embeddings**: For turning text into vectors
- **FAISS**: Fast vector search and storage
- **CSV Document Loader**: Load your knowledge base from CSV
- **Docker**: Run Kafka locally with Docker Compose

---

## 📦 Features

- Embeds CSV knowledge base into FAISS vector store
- Sends questions via Kafka topic
- Answers questions using Groq + LangChain
- End-to-end architecture: CSV → FAISS → Kafka → LLM → Answer

---

## 🧰 Prerequisites

- Python 3.9 or above
- Docker + Docker Compose
- Git
- Groq API Key: https://console.groq.com/

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/kafka-langchain-qa-bot.git
cd kafka-langchain-qa-bot

### 2. make virtual env
python -m venv venv
venv\Scripts\activate

##Install Dependencies
pip install -r requirements.txt

#create .env file in root directory and paste here like that below but add your real api key
GROK_API_KEY=gsksdjfkkfsdfjsdfkjkfdjfdjfkdjfkjf

#Start Kafka with Docker
docker-compose up -d

#Embed CSV Documents to FAISS
python run_embed.py

#Start Kafka Consumer (Answer Bot)
python run_consumer.py
#Start Kafka Producer in new terminal
python run_producer.py



