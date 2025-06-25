from producer.send_question import ask_question

questions = [
    "What is FAISS?",
    "What is LangChain?",
    "What does Kafka do?",
]

for q in questions:
    try:
        ask_question(q)
        print(f"📤 Question sent: {q}")
    except Exception as e:
        print(f"❌ ERROR sending question: {q} – {e}")
