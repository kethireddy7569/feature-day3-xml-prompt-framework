import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic(
    api_key=os.getenv("OPENROUTER_API_KEY"),
      base_url="https://openrouter.ai/api"

  )
sample_resume_text = """
Akhila Kethireddy
Contact: +91 9876543210
Email: akhila@example.com

Skills:
Python
JavaScript
Anthropic API
Firebase Firestore
"""

system_instruction = """
You are a strict data extraction engine.

Extract only:
1. Full Name
2. Email
3. Primary Skills

Return only this format:

<data>
Full Name: ...
Email: ...
Primary Skills: ...
</data>

Do not add any extra text.
"""

def extract_structured_payload(raw_text):

    response = client.messages.create(
        model="anthropic/claude-3-haiku",
        max_tokens=1000,
        temperature=0,
        system=system_instruction,
        messages=[
            {
                "role": "user",
                "content": f"Parse this resume:\n{raw_text}"
            }
        ]
    )

    return response.content[0].text


if __name__ == "__main__":

    print("Executing Day 3 Task")

    result = extract_structured_payload(sample_resume_text)

    print(result)