import g4f
import asyncio
import threading
import time

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
    
class GPT_asynco:
    def __init__(self, model = g4f.models.default, prePrompt= None, debug = False, logging = None) -> None:
        self.model = model
    

        self.logging = logging
        self._debug = debug

        self._providers = [
    g4f.Provider.GeekGpt,
    g4f.Provider.FakeGpt,
    g4f.Provider.OnlineGpt,
    g4f.Provider.AiChatOnline,
    g4f.Provider.ChatBase,
    g4f.Provider.AiAsk,
    g4f.Provider.Aichat,        
    g4f.Provider.AItianhu,      
    g4f.Provider.AItianhuSpace, 
    g4f.Provider.base_provider, 
    g4f.Provider.Berlin,        
    g4f.Provider.Bing,
    g4f.Provider.ChatAnywhere,      
    g4f.Provider.ChatForAi,     
    g4f.Provider.Chatgpt4Online,
    g4f.Provider.ChatgptAi,     
    g4f.Provider.ChatgptDemo,   
    g4f.Provider.ChatgptDemoAi,
    g4f.Provider.ChatgptFree,
    g4f.Provider.ChatgptLogin,
    g4f.Provider.ChatgptNext,
    g4f.Provider.ChatgptX,
    g4f.Provider.DeepInfra,
    g4f.Provider.FreeGpt,
    g4f.Provider.GPTalk,
    g4f.Provider.GptChatly,
    g4f.Provider.GptForLove,
    g4f.Provider.GptGo,
    g4f.Provider.GptGod,
    g4f.Provider.GptTalkRu,
    g4f.Provider.Hashnode,
    g4f.Provider.Koala,
    g4f.Provider.Liaobots,
    g4f.Provider.Llama2,
    g4f.Provider.MyShell,
    g4f.Provider.Opchatgpts,
    g4f.Provider.PerplexityAi,
    g4f.Provider.Phind,
    g4f.Provider.Pi,
    g4f.Provider.retry_provider,
    g4f.Provider.TalkAi,
    g4f.Provider.Vercel,
    g4f.Provider.Ylokh,
    g4f.Provider.You,
    g4f.Provider.Yqcloud
]

        self.history = []

        if prePrompt:
            self._system_message(prePrompt)

        if self.logging:
            self._load_log()

        self.requestIsDone = False
        self.systemRequestIsDone = False

    def _system_message(self, message: str) -> None:
        self.history.append({'role': 'system', 'content': message})

    def _timer(self, sleep) -> None:
        pass

    async def _send_system_async_request(self, provider, prompt: dict) -> None:
        try:
            result = await g4f.ChatCompletion.create_async(
                    model=self.model,
                    messages=self.history+[prompt],
                    provider=provider
                )
            
            if len(result) >= 5:
                self.systemRequestIsDone = True
                self.switch_chhat_history({'role': 'user', 'content': result})
            
        except:
            pass

    def _send_system_message(self, request: dict):
        for provider in self._providers:
            
            asyncio.run(self._send_system_async_request(provider, request))
            if self.systemRequestIsDone:
                
                self.systemRequestIsDone = False
                break

    def stenographer(self, lvl: int, listenerType: str) -> None:
        if lvl == 1:
            self._send_system_message({'role': 'user', 'content': 'Напиши краткую сводку по нашему диалогу.'})

    def _load_log(self):
        try:
            print(f'load from {self.logging}') if self._debug else None
            with open(self.logging, 'r', encoding='utf-8') as log_file:
                self.history = log_file.read()

        except:
            print(f'file {self.logging} not found. History will be empty.') if self._debug else None

    def log_history(self):
        with open(self.logging, 'w', encoding='utf-8') as log_file:
            log_file.write(f'{self.history}\n')


    def add_to_chat_history(self, request: list) -> None:
        self.history.append(request)

    def switch_chhat_history(self, request: list) -> None:
        self.history = request

    async def _send_async_request(self, provider) -> None:
        try:
            result = await g4f.ChatCompletion.create_async(
                    model=self.model,
                    messages=self.history,
                    provider=provider
                )
            
            if len(result) >= 5:
                print(provider.__name__) if self._debug else None
                self.requestIsDone = True
                self.history.append({'role': 'assistant', 'content': result})
            
        except:
            print('Error in provider', provider.__name__) if self._debug else None
        

    def send_message(self, request: dict) -> str:
        import time

        startTime = time.time()
        self.history.append(request)

        for provider in self._providers:
            
            asyncio.run(self._send_async_request(provider))
            if self.requestIsDone:
                
                self.requestIsDone = False
                break

        completion = self.history[-1]['content']

        endTime = time.time()
        print(round(endTime - startTime, 2), 'секунд') if self._debug else None
        self.log_history() if self.logging else None

        return completion
    
DND_prePrompt = """
Ты - ИИ помощник мастера подземелий в настоьной ролевой игре. Тебе будет приходить задание и вопросы по НРИ, а ты будешь проявлять креативность и помогать пользователю.
"""

def main():
    
    # gpta = GPT_asynco(prePrompt='Ты - ИИ ассистент по имени Анви. Я - Ваня (Иван). У тебя есть доступ к истории чата. Ты способен ее читать и делать на ее основе выводы. Так же ты можешь передавать эту историю пользователь при необходимости.', debug=True)
    gpta = GPT_asynco(prePrompt=DND_prePrompt, logging='DND.log', debug=True)

    while True:
        print(gpta.send_message({'role': 'user', 'content': input('>>> ')}))



if __name__ == '__main__':
    main()