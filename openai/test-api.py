from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
import os

api_key = os.getenv("API_KEY")
print(f"api_key: {api_key}")

# Todo: Fix the following error
# openai.RateLimitError: Error code: 429 - {'error': {'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors.', 'type': 'insufficient_quota', 'param': None, 'code': 'insufficient_quota'}}
client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
    ],
)
print(response.choices[0].message.content)
