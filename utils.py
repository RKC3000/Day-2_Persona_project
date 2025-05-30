import openai
from personas import PERSONAS
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(persona_name, user_input):
    persona = PERSONAS[persona_name]
    system_prompt = f"{persona['description']} {persona['style']}"

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content