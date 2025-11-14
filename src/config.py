# src/config.py
import os
from pathlib import Path
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parents[1]
ENV_PATH = ROOT_DIR / ".env"

print(f"📁 Buscando .env en: {ENV_PATH}")
if not ENV_PATH.exists():
    print("❌ El archivo .env no existe en esa ruta.")
else:
    print("✅ Archivo .env encontrado.")

# Cargar variables desde ese archivo
loaded = load_dotenv(dotenv_path=ENV_PATH)
print(f"📦 load_dotenv retornó: {loaded}")

# Mostrar valor leído
print("CHROMA_PERSIST:", os.getenv("CHROMA_PERSIST"))

CHROMA_PATH = os.getenv("CHROMA_PERSIST")
EMBED_MODEL = os.getenv("EMBEDDING_MODEL")
TOP_K = int(os.getenv("TOP_K", 6))
RERANK_TOP = int(os.getenv("RERANK_TOP", 3))
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
