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
#exemple chat
usage={
    "prompt_tokens":0,"completion_token":0,
    "total_tokens":0,"model":None
}
prompt = "Hi can you explain me what is AI"

response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {"role": "user", "content": prompt},
        
    ],stream=True
)

for x in response:
    if x.usage:
        usage["completion_token"]+=x.usage.completion_tokens
        usage["prompt_tokens"]+=x.usage.prompt_tokens
        usage["total_tokens"]+=x.usage.total_tokens
        usage["model"]=x.model
    if x.choices:
        content=x.choices[0].delta.content
        if content:
            print(content,end="",flush=True)
print(usage)