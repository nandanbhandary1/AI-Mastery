import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel
load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError('API Key not found')

client = Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"

#SYSTEM REQUIREMENTS
class Ticket(BaseModel):
    name:str
    email:str
    issue:str

schema = Ticket.model_json_schema()


system_prompt = f"""
Extract information from the ticket.
Return ONLY a valid JSON object.
The JSON must exactly match this schema:
{schema}
""" # mandatory to tell give in json obj

message_system = {
    "role":"system",
    "content":system_prompt
}

# USER INFO
role="user"


text = "Hello my name is Nandan. I got MacBook before 2 months in Banglore, My email is nandan@gmail.com, and my phone no is 0001. It is in Warranty period pls replace the display"

prompt=f""" 
This is a customer ticket. Please extract the personal information from this.{text}
"""

msg = {
    "role":role,
    "content":prompt
}

response_format = {
    "type":"json_object"
}

response = client.chat.completions.create(model=model, messages=[message_system, msg], temperature = 0, response_format=response_format)
# print(response)

ans = response.choices[0].message.content
print(ans) 

print("-----------------------------------")
# HOW TO READ THIS??

import json

raw_json = ans
data_file = json.loads(raw_json)
ticket = Ticket(**data_file)
# ticket = Ticket.model_validate(data_file)

print(ticket.name)
print(ticket.email)
print(ticket.issue)