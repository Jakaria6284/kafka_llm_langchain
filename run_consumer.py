from consumer.answer_question import consume_and_answer

try:
    print("📡 Kafka Consumer started. Waiting for questions...\n")
    consume_and_answer()
except Exception as e:
    print(f"❌ ERROR in run_consumer.py: {e}")
