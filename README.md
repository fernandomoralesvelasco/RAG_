# RAG_GEMINI
Sistema RAG(Retrieval-Augmented Generation) en Python que permite crear una base de conocimiento inteligente usando archivos .txt y .csv. Incluye ingestión de datos, chunking, embeddings con SentenceTransformers y almacenamiento persistente en ChromaDB. Ideal para asistentes inteligentes, chatbots especializados basados en recuperación semántica.

# RAG Knowledge Base 

Este proyecto implementa un **sistema RAG (Retrieval-Augmented Generation)** diseñado para crear un asistente inteligente capaz de responder preguntas sobre un tema en especifico.

El sistema permite:

- Ingerir archivos **TXT** y **CSV** con conocimiento.
- Dividir la información en *chunks* optimizados.
- Generar **embeddings semánticos** usando SentenceTransformer.
- Almacenar el conocimiento en **ChromaDB** de forma persistente.
- Realizar consultas con recuperación semántica (*vector search*).
- Complementar modelos como **Gemini**, **GPT**, **Claude**, etc.

# ***Este repositorio puede adaptarse fácilmente a **cualquier tema** cambiando los archivos dentro de `/data`.***

---

## 📂 Estructura del Repositorio
.
├── data/                 # Archivos TXT o CSV con conocimiento

├── src/

│   ├── ingest.py         # Construcción de la base vectorial (RAG ingestion)

│   ├── rag.py            # Motor de búsqueda semántica y recuperación

│   ├── config.py         # Configuración del proyecto

│   └── server.py         # API o interfaz (opcional)

├── chroma/               # Base vectorial persistente

├── venv/                 # (Opcional) Entorno virtual yo recomiendo más crearlo y usar python 3.11.9 o inferior no soporta 3.12 jeje

├── requirements.txt

├── .env (este archivo no lo subo por cuestiones de seguridad pero ustedes lo pueden crear es un archivo formato .env y dentro de el ponen el anexo de abajo)

└── README.md

 # Tecnologías Utilizadas

| Componente | Tecnología |
|-----------|------------|
| Base vectorial | **ChromaDB (Persistent mode)** |
| Embeddings | **SentenceTransformers** |
| División inteligente de texto | **LangChain Text Splitters** |
| Lenguaje | **Python 3.10+** |
| LLM recomendado | Gemini 2.5 Flash o GPT-4.1 |

# ANEXO
Dentro de .env ponen : 

GEMINI_API_KEY=XXXXXXXX-AQUÍ-TU-API-SIN-COMILLAS

CHROMA_PERSIST=db

EMBEDDING_MODEL=all-MiniLM-L6-v2

TOP_K=6

RERANK_TOP=3


