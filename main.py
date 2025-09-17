import os

from groq import Groq

from dotenv import load_dotenv

load_dotenv(dotenv_path="/home/bipin/Documents/genai/g25-aug/genai_25_sept/.env")

client = Groq()


chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "what is the capital of india",
        }
    ],
    model="openai/gpt-oss-20b",
)

print(chat_completion.choices[0].message.content)