import json
import re
from groq import Groq

# 🔥 Paste your Groq API key here
client = Groq(api_key="GROQ_API_KEY")

def analyze_prescription(text):

    prompt = f"""
You are a medical AI assistant.

Extract:
1. Medicine names
2. Dosage instructions
3. Simple English explanation
4. Telugu translation
5. Hindi translation
6. Safety warnings

Return ONLY valid JSON in this format:

{{
  "medicines": [
    {{
      "name": "",
      "dosage": "",
      "english_explanation": "",
      "telugu_explanation": "",
      "hindi_explanation": ""
    }}
  ],
  "warnings": []
}}

Prescription:
{text}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
    )

    result_text = response.choices[0].message.content

    # Extract JSON safely
    match = re.search(r"\{.*\}", result_text, re.DOTALL)

    if match:
        try:
            return json.loads(match.group())
        except:
            pass

    return {
        "medicines": [],
        "warnings": ["Could not parse AI response"]
    }