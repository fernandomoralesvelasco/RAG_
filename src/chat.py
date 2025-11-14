from src.retriever import retrieve
from src.llm import ask_gemini

def chat():
    print("🤖 Asistente de Fútbol Americano (escribe 'salir' para terminar)")
    while True:
        q = input("\nTú: ").strip()
        if q.lower() in {"salir", "exit"}:
            break
        ctx = retrieve(q)
        ans = ask_gemini(q, ctx)
        print("Bot:", ans)

if __name__ == "__main__":
    chat()