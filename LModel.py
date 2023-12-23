# Chat with an intelligent assistant in your terminal
from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

def request(context):
    completion = client.chat.completions.create(
        model="local-model", # this field is currently unused
        messages=context,
        temperature=0.7,
        stream=True,
    )

    new_message = {"role": "assistant", "content": ""}
    
    for chunk in completion:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
            new_message["content"] += chunk.choices[0].delta.content

    context.append(new_message)
    return context

def chat():

    history = [
    {"role": "system", "content": "You are an intelligent assistant. You always provide well-reasoned answers that are both correct and helpful."},
    {"role": "user", "content": "Hello, introduce yourself to someone opening this program for the first time. Be concise."},
]

    while True:

        print()
        history.append({"role": "user", "content": input("> ")})

        history.append(request(history))

def main():
    chat()

if __name__ == "__main__":
    main()