import os 
From groq import Groq

# Defina a chave da API diretamente no código ou garanta que ela esteja configurada corretamente no ambiente
os.environ["GROQ_API_KEY"] = "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"

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# Inicializa a lista de mensagens para manter o texto da conversa
messages = []

while True:
    usuario = input("digite uma mensagem ou 'sair' para encerrar")

    if usuario.lower() == 'sair':
        print("conversa encerrada")
        break

    # adiciona a mensagem do usuário á lista de mensagens
    messages.append({"role": "user", "content": usuario})

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama-3.1-70b-versatile",
    )

    resposta = chat_completion.choices[0].message.content
    print("Resposta", resposta)

    # Adiciona a resposta do assistente á lista de mensagens para manter o contextp
    messages.append({"role": "assistant", "content": resposta})