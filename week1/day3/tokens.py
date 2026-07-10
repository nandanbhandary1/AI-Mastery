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

# prompt="Suggest a name for my clothing company with its explanation"
prompt1 = "Hi"
prompt2 = "Explain Time travel in 100 words"
prompt3 = "Write 1000 word essay on AI/ML"

prompts = [prompt1, prompt2, prompt3]

for prompt in prompts:
    msg = {
        "role":role,
        "content":prompt
    }
    response = client.chat.completions.create(model=model, messages=[msg], max_tokens=50)
    # ans = response.choices[0].message.content
    usage = response.usage # Contains full token
    print(f"Prompt:{prompt} --> prompt_token: {usage.prompt_tokens}\ncompletion_token: {usage.completion_tokens} \nTotal_Tokens:{usage.total_tokens} Finish Reason: {response.choices[0].finish_reason}")
    print()
