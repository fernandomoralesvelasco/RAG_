import google.generativeai as genai
import os, textwrap
from src.prompts import SYSTEM_PROMPT
from src.config import GEMINI_API_KEY
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")   # ajusta nombre exacto

def ask_gemini(question: str, context: str) -> str:
    prompt = f"{SYSTEM_PROMPT}\n\nContexto:\n{context}\n\nPregunta: {question}\nRespuesta:"
    r = model.generate_content(prompt)
    return r.text.strip()