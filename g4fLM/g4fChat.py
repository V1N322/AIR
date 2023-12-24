import g4f
import fasterProvider
import asyncio

import g4f
import fasterProvider
import asyncio

class g4fChat:
    def __init__(self, getFasterProviders=False, saveDialog=False):
        self.history = [{"role": "user", "content": "Имя пользователя: Ваня. Имя ассистента (тебя): Рендольф"}]
        self.getProviders = fasterProvider.GetProviders()
        self.getFasterProviders = getFasterProviders
        self.saveDialog = saveDialog

    async def get_fasters(self):
        await self.getProviders.run_all()

    def get_provider(self):
        for provider in self.getProviders.fasters:
            yield provider

    def request(self, provider):
        try:
            completion = g4f.ChatCompletion.create(
                model=g4f.models.gpt_35_long,
                messages=self.history,
                stream=True,
                provider=provider
            )

            new_message = {"role": "assistant", "content": ""}
            
            for chunk in completion:
                if chunk:
                    print(chunk, end="", flush=True)
                    new_message["content"] += chunk

            if len(new_message["content"]) <= 5:
                return self.request(next(self.get_provider()))

            return new_message
        
        except:
            return self.request(next(self.get_provider()))

    def run(self):
        if self.getFasterProviders:
            asyncio.run(self.getProviders.run_all())

        while True:
            userMessage = input("> ")
            if userMessage == "exit":
                break

            self.history.append({"role": "user", "content": userMessage})

            new_message = self.request(next(self.get_provider()))

            self.history.append(new_message)

            print()

        if self.saveDialog:
            with open("dialog.txt", "w", encoding="utf-8") as f:
                f.write(str(self.history))

def main():
    chat = g4fChat(getFasterProviders = True, saveDialog = False)
    chat.run()

if __name__ == "__main__":
    main()