from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("❌ No se encontró la API KEY de OpenRouter. Verifica tu archivo .env")

client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

modelo = "deepseek/deepseek-chat-v3-0324:free"

def responder_pregunta_stream(pregunta, contexto):
    prompt = f"""
Eres un asistente experto en analizar código de proyectos. A partir del siguiente resumen, responde con claridad y precisión:

Resumen del proyecto:
\"\"\"
{contexto}
\"\"\"

Pregunta:
\"\"\"
{pregunta}
\"\"\"
"""

    respuesta = client.chat.completions.create(
        model=modelo,
        messages=[{"role": "user", "content": prompt}],
        stream=True
    )

    for chunk in respuesta:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content
