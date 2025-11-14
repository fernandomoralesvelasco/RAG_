# RAG_GEMINI
Sistema RAG(Retrieval-Augmented Generation) en Python que permite crear una base de conocimiento inteligente usando archivos .txt y .csv. Incluye ingestión de datos, chunking, embeddings con SentenceTransformers y almacenamiento persistente en ChromaDB. Ideal para asistentes inteligentes, chatbots especializados basados en recuperación semántica.

# RAG Knowledge Base – Football AI Assistant

Este proyecto implementa un **sistema RAG (Retrieval-Augmented Generation)** diseñado para crear un asistente inteligente capaz de responder preguntas sobre **fútbol americano**, reglas, jugadas, escenarios y situaciones del juego.

El sistema permite:

- Ingerir archivos **TXT** y **CSV** con conocimiento.
- Dividir la información en *chunks* optimizados.
- Generar **embeddings semánticos** usando SentenceTransformer.
- Almacenar el conocimiento en **ChromaDB** de forma persistente.
- Realizar consultas con recuperación semántica (*vector search*).
- Complementar modelos como **Gemini**, **GPT**, **Claude**, etc.

# ***Este repositorio puede adaptarse fácilmente a **cualquier tema** cambiando los archivos dentro de `/data`.***

---

##  Demo del proyecto (ejemplo)
> *“¿Qué pasa si un jugador toma el balón fuera de la zona?”*  
→ El asistente recupera información precisa desde la base vectorial y construye una respuesta completamente contextualizada.

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

└── README.md

 # Tecnologías Utilizadas

| Componente | Tecnología |
|-----------|------------|
| Base vectorial | **ChromaDB (Persistent mode)** |
| Embeddings | **SentenceTransformers** |
| División inteligente de texto | **LangChain Text Splitters** |
| Lenguaje | **Python 3.10+** |
| LLM recomendado | Gemini 2.5 Flash o GPT-4.1 |

##  Obtención de los Datos

El archivo de conocimiento utilizado en este proyecto fue generado mediante un proceso de **web scraping controlado** sobre contenido público disponible en el sitio oficial de la NFL.  
El objetivo del scraping fue reunir información educativa relacionada con reglas, jugadas y situaciones del juego, con el único propósito de construir una base de conocimiento para un sistema de RAG.

**Importante:**
- No se incluye en este repositorio ningún contenido protegido por derechos de autor.
- Los archivos de texto generados por scraping **no se distribuyen**, solo se procesan localmente para convertirlos en *embeddings*, los cuales no permiten reconstruir el texto original.
- El scraping se realizó respetando la disponibilidad pública del contenido y exclusivamente con fines educativos y de experimentación técnica.

Si deseas recrear el dataset, puedes ejecutar tu propio proceso de recolección siguiendo las políticas del sitio correspondiente.
