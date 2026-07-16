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




text = "Hello my name is Nandan. I got MacBook before 2 months in Banglore, My email is nandan@gmail.com, and my phone no is 0001. It is in Warranty period pls replace the display"

prompt=f""" 
This is a customer ticket. Please extract the personal information from this.{text}
"""

msg = {
    "role":role,
    "content":prompt
}

response = client.chat.completions.create(model=model, messages=[msg])
print(response)

ans = response.choices[0].message.content
print(ans)

