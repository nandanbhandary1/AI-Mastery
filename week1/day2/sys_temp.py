import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError('API Key not found')

client = Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"

role="user"

prompt="Suggest a name for my clothing company with its explanation"

msg_system = {
    "role":"system",
    # "content": "You are my best friend" system role
    "content":"You are a brand manager who suggests name for my clothing company, in 1 word"
}

msg = {
    "role":role,
    "content":prompt
}

response = client.chat.completions.create(model=model, messages=[msg_system, msg], temperature=2)
print(response)

ans = response.choices[0].message.content
print(ans)

