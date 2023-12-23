import g4f

history = [
    {"role": "user", "content": "Имя пользователя: Ваня. Имя ассистента (тебя): Рендольф"}
]


def get_provider():
    yield g4f.Provider.Liaobots
    yield g4f.Provider.AiChatOnline
    yield g4f.Provider.FakeGpt
    yield g4f.Provider.ChatgptAi
    yield g4f.Provider.DeepInfra

def request(history, provider = g4f.Provider.OnlineGpt):
    try:
        completion = g4f.ChatCompletion.create(
                    model=g4f.models.gpt_35_long,
                    messages=history,
                    stream=True,
                    provider=provider
        )


        new_message = {"role": "assistant", "content": ""}
        
        for chunk in completion:
            if chunk:
                print(chunk, end="", flush=True)
                new_message["content"] += chunk

        if len(new_message["content"]) <= 5 :
            return request(history, next(get_provider()))

        
        return new_message
    
    except:
        return request(history, next(get_provider()))

while True:

    userMessage = input("> ")
    if userMessage == "exit":
        break

    history.append({"role": "user", "content": userMessage})
    
    new_message = request(history)

    history.append(new_message)
    
    print()


with open("dialog.txt", "w", encoding="utf-8") as f:
    f.write(str(history))