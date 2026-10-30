from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
api_key = os.getenv("OPEN_ROUTER_KEY")
if not api_key:
    raise ValueError("A777AA")

try:
    client = OpenAI(api_key=api_key, base_url="https://openrouter.ai/api/v1")
except Exception as e:
    print("Errror saret waqtili sn3t elclient", e)

prompt = "Hi can you explain me what is AI"

response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print(response.choices[0].message.content)
