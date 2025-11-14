import os
import csv
import requests
from pathlib import Path
from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.config import CHROMA_PATH, EMBED_MODEL  # cargamos desde config.py

# Crear carpeta si no existe
os.makedirs(CHROMA_PATH, exist_ok=True)

print(f"🔹 Usando base de datos persistente en: {CHROMA_PATH}")
print(f"🔹 Usando modelo de embeddings: {EMBED_MODEL}")

# Inicializar cliente y colección
client = PersistentClient(path=CHROMA_PATH)
collection = client.get_or_create_collection("football_kb")

# Cargar modelo de embeddings y splitter
encoder = SentenceTransformer(EMBED_MODEL)
splitter = RecursiveCharacterTextSplitter(
    chunk_size=600,
    chunk_overlap=80,
    separators=["\n\n", "\n", ". ", " "]
)

def load_txt(path: Path):
    """Carga texto desde archivos .txt"""
    return path.read_text(encoding="utf-8")

def load_csv(path: Path):
    """Convierte archivos CSV con columnas [question, answer] a texto"""
    text = ""
    with open(path, newline='', encoding="utf-8") as f:
        for row in csv.DictReader(f):
            text += f"Pregunta: {row['question']}\nRespuesta: {row['answer']}\n\n"
    return text

def download_nfl_rules():
    """(Opcional) Descargar reglas desde una API si existe"""
    return ""

def build_kb():
    """Crea la base de conocimiento dividiendo y vectorizando documentos"""
    docs = []
    data_dir = Path("data")

    if not data_dir.exists():
        print("⚠️ Carpeta 'data/' no encontrada. Crea una y agrega tus archivos .txt o .csv.")
        return

    for file in data_dir.rglob("*"):
        if file.suffix == ".txt":
            docs.append(load_txt(file))
        elif file.suffix == ".csv":
            docs.append(load_csv(file))

    docs.append(download_nfl_rules())

    all_splits = []
    for d in docs:
        all_splits += splitter.split_text(d)

    ids = [f"chunk-{i}" for i in range(len(all_splits))]
    embs = encoder.encode(all_splits, show_progress_bar=True).tolist()

    collection.upsert(documents=all_splits, ids=ids, embeddings=embs)
    print(f"✅ {len(all_splits)} chunks indexados correctamente.")

if __name__ == "__main__":
    build_kb()
