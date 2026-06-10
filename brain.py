import ollama

messages = [
    {
        "role": "system",
        "content": """
You are PANDA, an intelligent AI assistant created by Pavan.

Rules:
- Answer the user's question directly.
- Be concise unless details are requested.
- Don't introduce yourself in every response.
- Only introduce yourself when asked who you are.
"""
    }
]

def ask_panda(prompt):

    messages.append({
        "role": "user",
        "content": prompt
    })

    response = ollama.chat(
        model="llama3",
        messages=messages
    )

    answer = response["message"]["content"]

    messages.append({
        "role": "assistant",
        "content": answer
    })

    return answer