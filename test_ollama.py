from ollama import Client

client = Client(host='http://localhost:11434')

response = client.chat(
    model='mistral',
    messages=[
        {"role": "system", "content": "Eres un programador senior experto en análisis de código y arquitectura de software."},
        {"role": "user", "content": "Explícame qué es un modelo de lenguaje Mistral 7B y para qué sirve."}
    ]
)

print("Respuesta de Mistral local:\n")
print(response['message']['content'])
