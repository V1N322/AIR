import g4f

class GPT:
    def __init__(self, model = g4f.models.default, provider = g4f.Provider.FakeGpt, prePrompt= None) -> None:
        self.model = model
        self.provider = provider

        self.history = []

        if prePrompt:
            self._system_message(prePrompt)

        

    def _system_message(self, message: str) -> None:
        self.history.append({'role': 'system', 'content': message})

    def send_message(self, request: dict) -> str:

        self.history.append(request)

        completion = g4f.ChatCompletion.create(
                model=self.model,
                messages=self.history,
                provider=self.provider
            )
        
        self.history.append({'role': 'assistant', 'content': completion})

        return completion
    

def main():
    
    gpt = GPT(prePrompt='Ты - ИИ ассистент по имени Неро. У тебя есть доступ к истории чата. Ты способен ее читать и делать на ее основе выводы. Так же ты можешь передавать эту историю пользователь при необходимости.')

    while True:
        message = input()
        print(gpt.send_message({'role': 'user', 'content': message}))

if __name__ == '__main__':
    main()