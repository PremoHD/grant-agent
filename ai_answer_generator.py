import openai
import json

openai.api_key = "YOUR_OPENAI_KEY"

def generate_answer(question, business_profile):
    prompt = f"Using this business profile {json.dumps(business_profile)}, answer: {question}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=300
    )
    return response.choices[0].text.strip()