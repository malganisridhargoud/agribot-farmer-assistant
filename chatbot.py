import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
API_URL = "https://api.groq.com/openai/v1/chat/completions"

def chat_response(prompt):
    if not API_KEY:
        return "âŒ Groq API key not found. Please set GROQ_API_KEY in your .env file."

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": "You are a helpful farming assistant for Indian farmers."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content'].strip()
    except requests.HTTPError as e:
        err = ""
        try:
            err = e.response.json().get("error", {}).get("message", "")
        except Exception:
            err = e.response.text if e.response is not None else ""
        return f"❌ API Error: {err or str(e)}"
    except Exception as e:
        return f"❌ Error: {str(e)}"

