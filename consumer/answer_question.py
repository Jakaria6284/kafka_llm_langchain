from kafka import KafkaConsumer
import json
from config.kafka_config import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC

from langchain_app.qa_chain import answer_question

consumer=KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='grok_group'
)

def consume_and_answer():
    for msg in consumer:
        try:
            question = msg.value["question"]
            print(f"\n🧑 User Question: {question}")
            answer = answer_question(question)
            print(f"🤖 Groq Answer: {answer}")
        except Exception as e:
            print(f"❌ ERROR in consumer loop: {e}")
