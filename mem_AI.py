import os
import json
from mem0 import Memory
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")
NEO4J_URL = os.getenv("NEO4J_URL")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

config = {
    "version": "v1.1",
    "embedder": {
        "provider": "gemini",
        "config": {
            "model": "models/text-embedding-004",
        }
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "collection_name": "test",
            "embedding_model_dims": "768",
            "host": "localhost",
            "port": 6333,
        }
    },
    "llm": {
        "provider": "gemini",
        "config": {
            "model": "gemini-2.0-flash",
            "temperature": 0.2,
            "max_tokens": 2000,
            "top_p": 1.0
        }
    },
    "graph_store": {
        "provider": "neo4j",
        "config": {
            "url": NEO4J_URL,
            "username": NEO4J_USERNAME,
            "password": NEO4J_PASSWORD
        }
    }
}

memory_client =  Memory.from_config(config)
# print("Setup done")

client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def chat(message):
    mem_result = memory_client.search(query=message, user_id="a123")

    memories = ""

    for memory in mem_result.get("results"):
        memories += f"{memory.get('memory')}\n"

    SYSTEM_PROMPT = f""" 
        You are a Memory-Aware Fact Extraction Agent, an advanced AI designed to
        systematically analyze input content, extract structured knowledge, and maintain an
        optimized memory store. Your primary function is information distillation
        and knowledge preservation with contextual awareness.

        Tone: Professional analytical, precision-focused, with clear uncertainty signaling
        
        Memory
        {memories}
        
        NOTE: When the user provides new information that should be stored in memory, 
        acknowledge it with a short confirmation (e.g., “Got it”, “Understood”, or “Noted”). 
        Do not print or summarize existing memory entries unless explicitly asked.
    """
    # print(f"\nMEMORY:\n{memories}")

    messages=[
        { "role": "user", "content": message },
        { "role": "system", "content": SYSTEM_PROMPT }
    ]

    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=messages
    )
    message_content = response.choices[0].message.content

    messages.append(
        {"role":"assistant", "content": message_content}
    )
    memory_client.add(messages, user_id="a123")

    return message_content

while True:
    message = input(">> ")
    if(message == "q"):
        break
    print("BOT🤖: ",chat(message=message))