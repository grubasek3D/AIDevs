import json
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": "You are a helpful assistant designed to output JSON.."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
        ]
)

# print(response)

for choice in response.choices:
    print(choice.message.content)
# print(response.choices[0].message.content)